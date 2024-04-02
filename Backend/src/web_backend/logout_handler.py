from base_handler import BaseHandler
class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("_xsrf")
        self.redirect(self.get_argument("next", "/"))
