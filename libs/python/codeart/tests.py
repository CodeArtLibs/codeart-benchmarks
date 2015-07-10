# coding: utf-8
import unittest

import codeart.benchmarks
import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._meinheld as _meinheld
import codeart.benchmarks.servers._tornado as _tornado
from codeart.benchmarks._bottle import *
from codeart.benchmarks._falcon import *
from codeart.benchmarks._flask import *
from codeart.benchmarks._tornado import *
from codeart.benchmarks._tornado_async import *
from codeart.benchmarks._wheezy_http import *
from codeart.benchmarks._wheezy_web import *
from codeart.benchmarks._wsgi import *
from codeart.benchmarks._wsgi_py3 import *
from codeart.benchmarks.responses import *


class CodeArtBenchmarksTests(unittest.TestCase):
    def test_x(self):
        pass
