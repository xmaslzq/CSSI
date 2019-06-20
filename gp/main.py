import webapp2
from google.appengine.api import urlfetch
import json
import random
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        load_template = the_jinja_env.get_template('template/load.html')
        self.response.write("Ho ho ho")
        gif_search = self.request.get("search-term")
        if gif_search is not None:
            giphy_key = "eJe7EvyU11b9fqcIAphGSxsSJP36EIt2"
            endpoint_url = "https://api.giphy.com/v1/gifs/search?q=" +\
                            gif_search + "&limit=25&offset=0&rating=G&lang=en&api_key=" +\
                            giphy_key
            print(endpoint_url)
            response = urlfetch.fetch(endpoint_url)
            content = response.content
            print(content)

            response_as_json = json.loads(content)
            rnum_gif = random.randint(0,24)
            image_url = response_as_json["data"][rnum_gif]["images"]["original"]["url"]
            print(image_url)

            gif = { "search" : gif_search,
                    "url" : iamge_url,
                    }
            self.response.write(load_template.render(gif))

    def post(self):
        load_template = the_jinja_env.get_template('templates/load.html')

        self.response.write(load_template.render(endpoint_url))

class MapHandler(webapp2.RequestHandler) {
    api_key = #AIzaSyCEneSUi1bSMZ03vNog-3HhzpP6stclafs
    url = "https://maps.googleapis.com/maps/api/staticmap?center"
}
app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
