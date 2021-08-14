from abc import ABC

import tornado.web as t_web
import tornado.ioloop as loop


class BasicRequestHandler(t_web.RequestHandler):

    def get(self):
        self.write("Backend get method initiated")


if __name__ == "__main__":
    app = t_web.Application([
        (r"/", BasicRequestHandler)
    ])

    port = 8080
    app.listen(port)
    print(f"backend up and running listing to port {port}")
    loop.IOLoop.current().start()
