# main.py
# the import section
import webapp2
import jinja2
import os
import meme_mode
from datetime import datetime
# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        intro = {"greeting": "Hola",
                 "adjective": "Awesome",}
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render(intro))
    def post(self):
        self.response.write("A post request to the EnterInfoHandler") # the response

class MemeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        dimg = {"img_url": "https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2018/02/google-pacman-796x419.jpg",
                "line1": "have fun",
                "line2": "have fun",
                }
        welcome_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(welcome_template.render(dimg))  # the response

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_line1 = self.request.get('user-first-ln')
        meme_line2 = self.request.get('user-second-ln')
        meme_choice = self.request.get('meme-type')
        meme_author = self.request.get("username")
        meme_date = str(datetime.strptime(self.request.get("date"), "%Y-%m-%d"))

        meme = meme_mode.Meme(
            top_line = meme_line1,
            btm_line = meme_line2,
            date_str = meme_date,
            username = meme_author,
            img_opt = meme_choice,
        )
        
        print(meme_line1, type(meme_line1))
        print(meme_line2, type(meme_line2))
        print(meme_choice, type(meme_choice))

        if meme_choice == 'old-class':
            url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
        elif meme_choice == 'college-grad':
            url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
        elif meme_choice == 'thinking-ape':
            url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
        elif meme_choice == 'coding':
            url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'

        user_info = {"line1": meme_line1,
                     "line2": meme_line2,
                     "img_url": url,
                     "author": meme_author,
                     "date": meme_date,}



        meme.put()

        self.response.write(results_template.render(user_info))

class ShowLibrary(webapp2.RequestHandler):
    def get(self): #get is use for showing information post is for getting and showing information
        result_template = the_jinja_env.get_template('templates/library.html')
        meme_query = meme_mode.Meme.query()
        memes = meme_query.fetch()
        template_vars = {
            "memes": memes,
        }

        self.response.write(result_template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', MemeHandler),
    ('/library', ShowLibrary),
], debug=True)
# etc
