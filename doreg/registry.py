import requests
from os import environ


DEFAULT_REGISTRY = "https://registry.hub.docker.com"
DEFAULT_NAMESPACE = "library"


class DummyProgressIndicator(object):
    def __init__(self, total):
        pass

    def zzzz(self, something):
        pass

    def __enter__(self):
        return self.zzzz

    def __exit__(self, type, value, traceback):
        pass


class DockerRegistry:
    def __init__(self, registry_url: str = None, progress_cls=DummyProgressIndicator):
        self._progress_cls = progress_cls
        self._registry_url = registry_url or DEFAULT_REGISTRY
        self._namespace = environ.get("DOCKER_NAMESPACE", DEFAULT_NAMESPACE)

    def _get_resource(self, resource: str = None, cache_method=None):
        """ Get all the entries for a given resource type, following pages """
        resource_url = f"{self._registry_url}/v2/{resource}"
        reply = self._get(resource_url)
        results = reply["results"]
        total = reply["count"]
        with self._progress_cls(total) as progress_object:

            for n in reply["results"]:
                progress_object(f"Downloading {resource}")
                yield (n)

            while reply["next"]:
                reply = self._get(reply["next"])
                results += reply["results"]
                for n in reply["results"]:
                    progress_object(f"Downloading {resource_url}")
                    yield (n)

    def get_repositories(self, namespace: str = None, show_progress: bool = False):
        namespace = namespace or self._namespace
        return self._get_resource(f"repositories/{namespace}")

    def get_tags(self, image):
        if "/" not in image:
            image = f"{self._namespace}/{image}"
        return self._get_resource(f"repositories/{image}/tags")

    def _get(self, url):
        reply = requests.get(url)
        reply.raise_for_status()
        return reply.json()
