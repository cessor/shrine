import os
import random

from tornado import gen
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler, StaticFileHandler, url

from shrines import shrines

define('debug', default=False)
define('port', default=8888)


class Home(RequestHandler):
    def initialize(self, shrines):
        self.shrines = shrines

    @gen.coroutine
    def get(self):
        shrine = message = random.choice(self.shrines)
        self.render("index.html", shrine=shrine, message=message)


class Text(RequestHandler):
    def initialize(self, shrines):
        self.shrines = shrines

    @gen.coroutine
    def get(self):
        _, message = random.choice(self.shrines)
        self.finish(message)


def directory(path):
    return os.path.join(os.path.dirname(__file__), path)


routes = [
    url(r"/", Home, dict(shrines=shrines)),
    url(r"/shrine.txt", Text, dict(shrines=shrines)),
    url(r'/(favicon\.ico)', StaticFileHandler, dict(path=directory('static')))
]


def configure():
    settings = dict(
        debug=options.debug,
        compress_response=True,
        static_path=directory('static'),
        template_path=directory('templates'),
        xheaders=True,
        xsrf_cookies=True,
    )
    return Application(routes, **settings)


def main():
    app = configure()
    server = HTTPServer(app, xheaders=True)
    server.listen(options.port)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
