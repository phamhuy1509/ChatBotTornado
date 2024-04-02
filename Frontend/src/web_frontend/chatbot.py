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
from chat_form import ChatForm
from logout_handler import LogoutHandler

def make_app():
    settings = {
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "redirect_base_uri": f"http://localhost:6885",
        "xsrf_cookies": True,
        "debug": True
    }
    return tornado.web.Application([(tornado.routing.HostMatches("localhost"), 
                                     [(r'/login', LoginHandler), 
                                      (r'/chatform', ChatForm), 
                                      (r'/chat', ChatHandler), 
                                      (r'/logout', LogoutHandler)])], **settings)

async def main(sockets):
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    await asyncio.Event().wait()

if __name__ == "__main__":
    port = 6885
    print(f"Listening frontend on port {port}")
    sockets = tornado.netutil.bind_sockets(port)
    tornado.process.fork_processes(0)
    asyncio.run(main(sockets))
