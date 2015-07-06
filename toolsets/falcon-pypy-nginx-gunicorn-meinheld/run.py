import codeart.benchmarks.servers
import codeart.benchmarks.servers.meinheld
from codeart.benchmarks._falcon import *


codeart.benchmarks.servers.disable_logs()
codeart.benchmarks.servers.meinheld.disable_logs()
codeart.benchmarks.servers.meinheld.configure()
