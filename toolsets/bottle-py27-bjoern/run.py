from bottle import run
from codeart.benchmarks._bottle import *


if __name__ == "__main__":
    import codecs
    import json
    import os
    if os.path.exists('benchmark_config.json'):
        with codecs.open('benchmark_config.json', 'r', 'utf-8') as f:
           data = json.loads(f.read())
           # print(data)

    import os
    port = int(os.environ.get('PORT', 8000))
    run(host='0.0.0.0', port=port, server='bjoern', quiet=True, reuse_port=True)
