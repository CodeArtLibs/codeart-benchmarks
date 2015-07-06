import codeart.benchmarks.servers
import codeart.benchmarks.servers.meinheld
from codeart.benchmarks._wsgi import *
from codeart.benchmarks.requests import *


codeart.benchmarks.servers.disable_logs()
codeart.benchmarks.servers.meinheld.disable_logs()
codeart.benchmarks.servers.meinheld.configure()
