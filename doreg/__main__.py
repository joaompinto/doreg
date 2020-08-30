from .arg_parser import arg_parse
from doreg.registry import DockerRegistry


def main():
    options, args = arg_parse()
    registry = DockerRegistry()
    if len(args) == 0:
        for repo in registry.get_repositories():
            print(repo["name"])


if __name__ == "__main__":
    main()
