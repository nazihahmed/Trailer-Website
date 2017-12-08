import webbrowser


class Movie():
    """ creates a new Movie instance with info about it """

    def __init__(self, movie_title, movie_type, movie_time, movie_year, poster_image, trailer_youtube, movie_storyline):
        """ all the info of the movie gets initialized into the properties for use with other modules"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # added functionality and info
        self.type = movie_type
        self.time = movie_time
        self.year = movie_year
