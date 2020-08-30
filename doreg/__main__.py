from alive_progress import alive_bar
from .arg_parser import arg_parse
from .registry import DockerRegistry

from . import cli


def main():
    options, args = arg_parse()
    registry = DockerRegistry(progress_cls=alive_bar)
    if len(args) == 1:
        repository = args[0]
        cli.list_tags(registry, repository)
    if len(args) == 0:
        cli.list_repositories(registry)


if __name__ == "__main__":
    main()
