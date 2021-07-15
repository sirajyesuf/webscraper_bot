from requests.sessions import session
from requests_html import HTMLSession


class Voa:
    BASE_URL = "https://www.voanews.com/silicon-valley-technology"
    BASE_URL1 = "https://www.voanews.com"
    asession = HTMLSession()

    def today(self):
        return self.asession.get(self.BASE_URL).html
