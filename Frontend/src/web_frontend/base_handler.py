from tornado.web import RequestHandler
class BaseHandler(RequestHandler):
    def get_current_user(self):
        user_cookie = self.get_secure_cookie("_xsrf")
        if user_cookie:
            return user_cookie
        return None
    def check_xsrf_cookie(self) -> None:
        return super().check_xsrf_cookie()