import codeart.benchmarks.servers
import codeart.benchmarks.servers.meinheld
from codeart.benchmarks._flask import *

# app.config['DEBUG'] = True

codeart.benchmarks.servers.disable_logs()
codeart.benchmarks.servers.meinheld.disable_logs()
codeart.benchmarks.servers.meinheld.configure()
