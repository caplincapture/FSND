# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import fresh_tomatoes
import media



#print (toy_story.storyline)

one_flew_over_the_cuckoos_nest = media.Movie("One Flew Over the Cuckoo's Nest",
                     "A man is committed to a mental institution",
                     "https://upload.wikimedia.org/wikipedia/en/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg",
                     "https://www.youtube.com/watch?v=2WSyJgydTsA")

the_bourne_ultimatum = media.Movie("The Bourne Ultimatum",
                             "A former agent is on the run",
                             "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Bourne_Ultimatum_%282007_film_poster%29.jpg",
                             "https://www.youtube.com/watch?v=ohkW_xbPl9A")


interstellar = media.Movie("Interstellar",
                          "A team of explorers tries to ensure a humanity's survival",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                          "https://www.youtube.com/watch?v=0vxOhd4qlnA")


the_shawshank_redemption= media.Movie("The Shawshank Redemption",
                                "A banker is sent to prison",
                                "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                "https://www.youtube.com/watch?v=6hB3S9bIaco")

schindlers_list = media.Movie("Schindler's List",
                           "A man goes on a rescue mission during the Holocaust",
                           "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                           "https://www.youtube.com/watch?v=JdRGC-w9syA")
inception = media.Movie("Inception",
                        "A group attempts to rob a rich man",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [one_flew_over_the_cuckoos_nest, the_bourne_ultimatum, interstellar, the_shawshank_redemption, schindlers_list, inception]

#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)

# Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

#print (schindlers_list.storyline)

#interstellar.show_trailer()                       
#inception.show_trailer()
