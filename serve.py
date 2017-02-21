import os
import random

from tornado import gen
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler, StaticFileHandler, url

from pep20 import pep20

define('debug', default=False)
define('port', default=8888)


class Home(RequestHandler):
    def initialize(self, pep20):
        self.pep20 = pep20

    @gen.coroutine
    def get(self):
        message = random.choice(self.pep20)
        self.render("index.html", shrine="pep20", message=message)


class Text(RequestHandler):
    def initialize(self, pep20):
        self.pep20 = pep20

    @gen.coroutine
    def get(self):
        message = random.choice(self.pep20)
        self.finish(message)


def directory(path):
    return os.path.join(os.path.dirname(__file__), path)


routes = [
    url(r"/", Home, dict(pep20=pep20)),
    url(r"/pep20.txt", Text, dict(pep20=pep20)),
    url(r'/(favicon\.ico)', StaticFileHandler, dict(path=directory('static')))
]


def configure():

    options.parse_command_line()

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
