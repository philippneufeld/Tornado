# Philipp Neufeld, 2022

import os

import tornado.web
import tornado.httpserver
import tornado.websocket
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args) -> None:
        self.render("content/index.html")

class WSHandler(tornado.websocket.WebSocketHandler):

    def open(self) -> None:
        pass

    def on_message(self, msg) -> None:
        self.write_message(f"You wrote: {msg}")

    def on_close(self) -> None:
        pass


if __name__ == "__main__":

    content_dir = os.path.join(os.path.dirname(__file__), "content")

    port = 8888

    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/websocket", WSHandler),
        (r"/content/(.*)", tornado.web.StaticFileHandler, {"path": content_dir}),
        ])

    server = tornado.httpserver.HTTPServer(app)
    server.listen(port)
    print(f"Server started on port {port}")

    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        pass

