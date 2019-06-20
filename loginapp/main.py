import webapp2
from google.appengine.api import users #to access to google api

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user() #if no have user, returns "Null"
        if user:
            self.redirect("/loggedin")
            #self.response.write("To be or not to be")
        else:
            self.redirect("/nouser")
            #self.response.write("You are not logged in")

class LoggedInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        email = user.nickname()

        logout_url = users.create_logout_url("/")
        self.response.write("Hello " + email +
                            '! Login successful <a href="' +
                            logout_url+ '">Click here to log out' )

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/") #login to gmail the "/" is when logged in, where the user is at"
        self.response.write('Please log in <a href= "' +
                            login_url + '"> here</a>')


app = webapp2.WSGIApplication({
    ('/', MainHandler),
    ('/loggedin', LoggedInHandler),
    ('/nouser', NoUserHandler),

}, debug=True)
