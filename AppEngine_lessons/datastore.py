from google.appengine.ext import ndb

class Movie(ndb.Model):
  title = ndb.StringProperty(required = True)
  rating = ndb.FloatProperty(required = False)
  runtime = ndb.IntegerProperty(required = False)
  def AutoPlay():
    if runtime <= 120 and rating > 9:
      print("Up Next: " + title)
    else:
      print("Not worth your time")

endgame = Movie(title = "Avengers: Endgame", runtime = 130, rating = 9.1)
antman = Movie(title = "Antman", runtime = 20, rating = 8.0)
ironman = Movie(rating = 9.7, title = "Iron Man", runtime = 119)
spidey = Movie(title = "Spiderman", runtime = 120, rating = 9.0)

def PrettyPrint(single_movie):
  print(single_movie)
  print(single_movie.AutoPlay())


movies = [endgame, antman, ironman, spidey]
for n in movies:
  #PrettyPrint(m)
  movie_key = n.put()
  #print(m.title + "Key: " + str(movie_key))
  #print(m.title + "Key id: " + str(movie_key.id())

#look up every Movie in the datastore
movies_query = Movie.query()
print(movies_query)
all_movies = movies_query.fetch()
print(all_movies)
for mov in all_movies:
  PrettyPrint(mov)

spideys_query = Movie.query().filter(Movie.title == 'Spiderman')
spideys = spideys_query.fetch()
#print(spideys)

short_query = Movie.query().filter(Movie.runtime <= 120)
shorts = short_query.fetch()
really_short_query = Movie.query().filter(Movie.runetime <= 30)
really_short_movies = really_short_query.fetch()
really_short_and_ok_movies = []
for m in really_short_movies:
  if m.rating > 5:
    really_short_and_ok_movies.append(m)
print(really_short_and_ok_movies)
