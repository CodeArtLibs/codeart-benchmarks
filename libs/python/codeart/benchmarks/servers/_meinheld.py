import os

try:
    import meinheld
    import meinheld.server
except ImportError:
    print('Meinheld is not installed.')


def disable_logs():
    meinheld.set_access_logger(None)
    meinheld.set_error_logger(None)
    meinheld.server.set_access_logger(None)

def configure():
    meinheld.set_keepalive(int(os.getenv('KEEP_ALIVE', 120))) # timeout in seconds
