from codeart.benchmarks._tornado import app


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8000))

    import tornado
    import tornado.httpserver
    # simple multi-process
    server = tornado.httpserver.HTTPServer(app)
    server.bind(port)
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop.instance().start()

    # simple single-process
    # app.listen(port)
    # tornado.ioloop.IOLoop.instance().start()
