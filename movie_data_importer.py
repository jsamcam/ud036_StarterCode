#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json

# in order to construct the poster image URL a size must be specified in the
# file path

api_poster_image_size = 'w500'


# this function takes in an array of movie ids and an API key, then retrieves
# movie data from the API for each id that has been provided

def query_movie_api(movie_ids, api_key):
    movie_data_list = []

# the API returns an image filepath, the full URL needs to be constructed
# from the API configurations

    connection = \
        urllib.urlopen('https://api.themoviedb.org/3/configuration?api_key='
                        + api_key)
    base_url_output = json.loads(connection.read())
    image_url_base = base_url_output['images']['secure_base_url']

# for each id in the passed array, a connection will be made to the API
# to retrieve the movie data.

    for movies in movie_ids:

        connection = \
            urllib.urlopen('https://api.themoviedb.org/3/movie/'
                           + movies + '?api_key=' + api_key
                           + '&append_to_response=videos,images')
        output = json.loads(connection.read())
        connection.close()

# Appending an array of movie data values to an array

        movie_data_list.append([output.get('original_title'),
                               output.get('overview'), image_url_base
                               + api_poster_image_size
                               + output.get('images').get('posters'
                               )[0].get('file_path'),
                               'https://www.youtube.com/watch?v='
                               + output.get('videos').get('results'
                               )[0].get('key')])

# returning the constructed array of movie data arrays

    return movie_data_list
