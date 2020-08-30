import sys
from optparse import OptionParser
from .version import version


def arg_parse():
    usage = f"{sys.argv[0]}"
    parser = OptionParser(usage, version=version)
    (options, args) = parser.parse_args()
    return (options, args)
