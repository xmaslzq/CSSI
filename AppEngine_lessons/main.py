import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request there is also post request
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8' #text file is text/
        self.response.write("<body style = 'background-color: blue; color: F9B700;'><h1>Hello, World!</h1></body>") #the response

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write("<body style = 'background-color: blue; color: F9B700;'><h1>Hello, Singapore!</h1></body>")

class NewsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write("<body style = 'background-color: blue; color: F9B700;'><h1>Hello, News in Singapore!</h1></body>")
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage),
    ('/news', NewsPage), #this maps the root url to the Main Page Handler
], debug=True)

# WARNING:
