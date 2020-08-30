import sys
from optparse import OptionParser
from setuptools_scm import get_version


def arg_parse():
    usage = f"{sys.argv[0]}"
    parser = OptionParser(usage, version=get_version())
    (options, args) = parser.parse_args()
    return (options, args)
