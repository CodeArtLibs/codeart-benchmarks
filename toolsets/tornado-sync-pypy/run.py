import codeart.benchmarks.servers
import codeart.benchmarks.servers.tornado
from codeart.benchmarks._tornado import app


if __name__ == "__main__":
    codeart.benchmarks.servers.disable_logs()
    codeart.benchmarks.servers.tornado.disable_logs()

    import tornado
    import tornado.httpserver
    # simple multi-process
    server = tornado.httpserver.HTTPServer(app)
    server.bind(PORT)
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop.instance().start()

    # simple single-process
    # app.listen(PORT)
    # tornado.ioloop.IOLoop.instance().start()
