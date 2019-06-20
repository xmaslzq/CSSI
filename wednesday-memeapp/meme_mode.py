from google.appengine.ext import ndb
#Storing in all strings
#username/top text/btm text/image opt/image option/datestring

class Meme(ndb.Model):
    top_line = ndb.StringProperty(required=False)
    btm_line = ndb.StringProperty(required=False)
    img_opt = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    date_str = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)
    if img_opt == 'old-class':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif img_opt == 'college-grad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif img_opt == 'thinking-ape':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif img_opt == 'coding':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
