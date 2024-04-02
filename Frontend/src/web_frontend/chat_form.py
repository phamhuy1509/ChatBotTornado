import tornado
from base_handler import BaseHandler

class ChatForm(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("../web_ui/chatbot.html")