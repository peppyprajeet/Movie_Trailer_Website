import webbrowser

#Class
class Movie():
    """ This is an example for documentation """
    
    #Class Varibales - declared outside init function - declared in CAPS as it is constant
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] 

    #Constructor : the init fucntion is instantiated here associated to class Movie
    #This function takes the input values that are associated with the movie titles, movie storylines, poster image and trailer. 
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        #Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Instance Methods : the oinstance method with refernce to self is declared so that calling the function to open the trailer in web browser
    def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
