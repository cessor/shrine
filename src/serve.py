import os
import secrets
from secrets import SystemRandom
from shrines import shrines
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, StaticFileHandler, url


random = SystemRandom()


class Home(RequestHandler):
    def get(self):
        shrine, message = random.choice(shrines)
        shrine += ' shrine'
        self.render("index.html", shrine=shrine, message=message)


class Text(RequestHandler):
    def get(self):
        _, message = random.choice(shrines)
        self.finish(message)


def directory(path):
    return os.path.join(os.path.dirname(__file__), path)


def main():
    HTTPServer(
        Application(
            handlers=[
                url(
                    pattern=r"/",
                    handler=Home,
                ),
                url(
                    pattern=r"/shrine.txt",
                    handler=Text,
                ),
                url(
                    pattern=r'/(favicon\.ico)',
                    handler=StaticFileHandler,
                    kwargs={
                        "path": directory(
                            'static'
                        )
                    }
                )
            ],
            debug=False,
            compress_response=True,
            static_path=directory(
                'static'
            ),
            template_path=directory(
                'templates'
            ),
            xheaders=True,
            xsrf_cookies=True,
        ),
        xheaders=True
    ).listen(
        port=8888
    )
    IOLoop.current().start()


if __name__ == '__main__':
    main()
