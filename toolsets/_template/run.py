from codeart.benchmarks.__FRAMEWORK import *


if __name__ == "__main__":
    import os
    server = os.getenv('SERVER', None)
    port = int(os.environ.get('PORT', 8000))
    if server:
        run(host='0.0.0.0', port=port, server=server)
    else:
        run(host='0.0.0.0', port=port)
