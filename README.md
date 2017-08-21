# ud036_StarterCode
Source code for a Movie Trailer website that is generated by polling [The Movie DB](https://www.themoviedb.org/about "About The Movie DB") API for movie data.
## Features:
* Imports movie data from [The Movie DB](https://www.themoviedb.org/documentation/api "The Movie DB API Documentation")
* Creates a Movie Trailer Website that displays Movie Title, Poster Image and Overview.
* Clicking on the Movie trailer poster image will open and play the movie trailer in a modal

### Tech
You'll need [Python 2.7](https://docs.python.org/2/index.html "Python 2.7 Documentation") installed to run this project.


### How to get an API Key
Instructions on how to request a [The Movie DB API Key](https://www.themoviedb.org/talk/5695502cc3a3687170000443?language=en, "How to request an API Key") are listed on their forum.
For additional details on the [The Movie DB](https://www.themoviedb.org/documentation/api "The Movie DB API Documentation") API you can refer to their API documentation
### Installation

```sh
$ git clone https://github.com/jsamcam/ud036_StarterCode.git
```

### Getting Started
Update the api_key.py file with your API key
A short list of movie id's are provided in the entertainment_center.py file to get started
Follow these steps to run the script that imports the movie data and creates the HTML page for the movie trailer website

```sh
$ cd ud036_StarterCode
$ python entertainment_center.py
```
This will create, populate and open a fresh_tomatoes.html page.
The example.html file is a sample of the expected outpout

### Known bugs
Currenlty does not support non ASCII characters

### License
[MIT](https://choosealicense.com/licenses/mit/, "MIT License")