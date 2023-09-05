# Playlist-Analysis

*This repository is a personal project and is not intended as an application or product. It is for personal use and educational purposes only*

This repository contains multiple files, with the general purpose to classify song data as either sunny or rainy. This goal allows me to get practice implementing different models and interacting with APIs, helps me better understand the Spotify API and the features that are used to quantify music, and enhance my own personal listening experience by leveraging my location and library together.

**mvspotifyhelper**: a package containing a collection of help navigate the Spotify API and make requests easier.

**sunnyvsrainy_classification_models.ipynb**: a file that reads in public spotify playlists that are either made for rainy or sunny situations. Different classification models are trained, tuned, and saved.

**generate_weather_playlists.ipynb**: a file that accesses my library of liked songs, implements the saved models to get probabilities of classification, and generates a weather-themed playlist from my library and spotify's recommendations.

**weather_api_test.ipynb** a file that accesses the open weather map API to get the current weather based on my location.

**generate_recs_test.ipynb**: Not a part of the project, but a file that helped me navigate the Spotify API and access and generate recommendations for my playlists

**convert_library_to_colors.ipynb**: Not a part of the project, but a file where I started to explore the relationship between song and primary color of album art using ColorThief package.







