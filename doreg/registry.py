import requests
from os import environ


DEFAULT_REGISTRY = "https://registry.hub.docker.com"
DEFAULT_NAMESPACE = "library"


class DockerRegistry:
    def __init__(self, registry_url: str = None):
        self._registry_url = registry_url or DEFAULT_REGISTRY
        self._namepsace = environ.get("DOCKER_NAMESPACE", DEFAULT_NAMESPACE)

    def get_repositories(self, _namespace: str = None):
        _namespace = _namespace or self._namepsace
        reply = self._get(f"repositories/{_namespace}")
        results = reply["results"]
        total = reply["count"]
        while reply["next"]:
            print(f"{len(results)}/{total}")
            reply = self._get(reply["next"])
            results += reply["results"]

        return results

    def _get(self, url):
        # Use absolute url or compose using part for v2
        if url.startswith(self._registry_url):
            full_url = url
        else:
            full_url = f"{self._registry_url}/v2/{url}"
        reply = requests.get(full_url)
        reply.raise_for_status()
        return reply.json()
