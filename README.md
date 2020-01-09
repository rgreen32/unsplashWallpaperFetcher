# wallpaperFetcher
A Python script and a batch script for fetching a random photo from user-specified https://unsplash.com/ collections and setting the photo to desktop background automatically.


# fetchImage.py
Youll need to get an unsplash api key from https://unsplash.com/developers. then add that key as an envronment variable named API_KEY or plug it into fetchImage.py. Then pick out some collection ids from https://unsplash.com/collections and plug them into fetchImage.py. 

If everything is set up correctly, when fetchImage.py is run, it should save a random image from one of the collections as image.jpg.


# wallpaperScript.bat
the wallpaperScript.bat runs fetchImage.py and attempts to save the image file produced by it as the Desktop background picture. (Its not very reliable yet.)
