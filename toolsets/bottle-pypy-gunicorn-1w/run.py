from codeart.benchmarks._bottle import *

import bottle
app = bottle.default_app()


# if __name__ == "__main__":
#     import os
#     port = int(os.environ.get('PORT', 8000))
#     from bottle import run
#     run(host='0.0.0.0', port=port, server='gunicorn', quiet=True, workers=1)
