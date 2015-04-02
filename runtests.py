#!/usr/bin/env python
import logging
import os
import sys
from os.path import dirname, abspath
from optparse import OptionParser
from distutils.version import StrictVersion

logging.getLogger('CodeArt').addHandler(logging.StreamHandler())

sys.path.insert(0, dirname(abspath(__file__)))


def runtests(*test_args, **kwargs):
    kwargs.setdefault('interactive', False)
    test_runner = NoseTestSuiteRunner(**kwargs)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    try:
        os.remove('test_:memory:')
    except:
        pass
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=2, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)

