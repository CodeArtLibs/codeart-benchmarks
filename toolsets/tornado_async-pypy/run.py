import codeart.benchmarks.servers as _util
import codeart.benchmarks.servers._tornado as _tornado
from codeart.benchmarks._tornado_async import app


if __name__ == "__main__":
    _util.disable_logs()
    _tornado.disable_logs()

    import tornado
    import tornado.httpserver
    # simple multi-process
    server = tornado.httpserver.HTTPServer(app)
    server.bind(_util.get_port())
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop.instance().start()

    # simple single-process
    # app.listen(_util.get_port())
    # tornado.ioloop.IOLoop.instance().start()
