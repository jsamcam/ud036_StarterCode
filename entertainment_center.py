#!/usr/bin/python
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media
import movie_data_importer
from api_key import api_key

# for each id in array, get the movie data
# Return an two dimensional array of movie data, each inner array will contain the data for each movie
# for each movie data in the array create an object and store it in an array
# call the fresh_tomatoes.open_movies_page() function and pass the array of movie objects

# API movie ID's

movie_ids = [
    '197',
    '1417',
    '563',
    '769',
    '19995',
    '333339',
    '20526',
    '680',
    '120',
    '6977',
    '9509',
    '672',
    ]

# getting movie data from the API for each id that is provided

imported_movie_data = movie_data_importer.query_movie_api(movie_ids,
        api_key)

movie_objects = []

# A movie object will be created for each movie data array

for movie_data in imported_movie_data:
    movie_objects.append(media.Movie(movie_data[0], movie_data[1],
                         movie_data[2], movie_data[3]))

# call to the function that will use the Movie objects to populate an HTML page that displays the Movies in a gallery

fresh_tomatoes.open_movies_page(movie_objects)
