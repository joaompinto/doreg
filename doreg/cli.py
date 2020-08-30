from tabulate import tabulate
from .registry import DockerRegistry


def list_repositories(registry: DockerRegistry):
    table = []
    repositories = sorted(
        registry.get_repositories(show_progress=True), key=lambda k: k["name"]
    )
    for repo in repositories:
        table.append((repo["name"], repo["description"]))
    print(tabulate(table, headers=["Name", "Description"]))


def list_tags(registry: DockerRegistry, image: str):
    table = []
    tags = sorted(registry.get_tags(image), key=lambda k: k["name"])
    for tag in tags:
        table.append((tag["name"], tag["full_size"], tag["last_updater_username"]))
    print(tabulate(table, headers=["Name", "Size", "Last updater"]))
