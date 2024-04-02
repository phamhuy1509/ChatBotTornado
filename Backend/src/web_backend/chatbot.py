import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.escape
import tornado.routing
import tornado.httpserver
import tornado.netutil
import tornado.process
import asyncio
from login_handler import LoginHandler
from chat_handler import ChatHandler

def make_app():
    settings = {
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "redirect_base_uri": f"http://localhost:6886/api",
        "debug": True
    }
    return tornado.web.Application([(r'/api/login', LoginHandler), 
                                    (r'/api/chat', ChatHandler)], **settings)

async def main(sockets):
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    await asyncio.Event().wait()

if __name__ == "__main__":
    port = 6886
    print(f"Listening backend on port {port}")
    sockets = tornado.netutil.bind_sockets(port, address="0.0.0.0")
    tornado.process.fork_processes(0)
    asyncio.run(main(sockets))
