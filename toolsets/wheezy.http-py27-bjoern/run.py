from codeart.benchmarks._wheezy_http import *


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8000))

    import bjoern
    bjoern.listen(app, 'localhost', port, reuse_port=True)
    bjoern.run()
