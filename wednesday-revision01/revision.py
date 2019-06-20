import webapp2

##----------
## 1. This file is called revision.py. Examine the app.yaml file.
## Where is this file mentioned? what happens if I change the name?
## 2. **BEFORE** YOU TEST THIS PROJECT ON YOUR LAPTOP
## PREDICT WHAT WILL YOU SEE ON YOUR SCREEN?
## 2a. when localhost:8080 is entered in the browser?
## 2b. what other paths are available and what will you see?
## 3. Test your project on your laptop and see if your predictions in 2 is correct.
## (Remember: go to the appropriate folder in the terminal and type in:
##  dev_appserver.py app.yaml )
## 4. Now, write code such that when the following paths are executed, you see the following text
## localhost:8080 --> "I love bananas"
## localhost:8080/chiku --> "Give me a chiku"
## ----------------

class Banana(webapp2.RequestHandler):
    def get(self):
        pass

class Chiku(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        ss = """<h4>Give me some chiku<h4>"""
        self.response.write(ss)

class Durian(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        ss = """<h1>Here is some default text<h1>"""
        self.response.write(ss) #the response

app = webapp2.WSGIApplication([
    ('/', Durian),
    ('/a', Durian),
    ('/chiku', Chiku),
], debug=True)
