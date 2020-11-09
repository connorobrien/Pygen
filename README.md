# Pygen - A Python Based Song Recommendation Program

Pygen is a program that analyzes a Spotify user’s listening history and generates a list of recommended tracks. It builds on top of Spotify’s recommendation algorithm to generate tracks outside of that user’s immediate taste.

<h3>Motivation </h3>

My motivation for this project stemmed from a dissatisfaction with the song recommendations provided to me by Spotify. Every Monday morning, Spotify users are given a personalized playlist of 30 recommended songs in a playlist called Discover Weekly. While I have found excellent songs in this playlist, I've often found that the songs I'm recommended are more or less 'knockoff' versions of the artists I frequent. 

<p align="center">
<img src="https://raw.githubusercontent.com/connorobrien/Pygen/main/DiscoverWeeklyExample.png"width="700">
</p>

When I do discover a new artist I'm enamoured with, its rarely an artist in the same styles that I listen to. Rather, its one who's music shares some stylistic similarities with my favorite artists, but offers some unique and distinct characteristics. In other words, my favorite artists recommendations are one's that are similar to the artists I enjoy, but not too similar. This program impliments this idea, creating customizable song recommendations that 'step further' away from a user's Spotify listening history. 


The general approach for this program is to create chained recommendations from an user's listening history. It start's with their most listened to songs on Spotify, recommends ten songs they might enjoy, chooses one of the latest ten songs to recommend another ten songs from, and repeats this process for a number of iterations. My proposal is that more iterations will provide recommendations that are more 'dissimilar' from a user's listening history, but by using their listening history as a starting point these recommendations might offer new and exiciting music recommendations.

<p align="center">
<img src="https://raw.githubusercontent.com/connorobrien/Pygen/main/WorkflowDiagram.png"width="700">
</p>


<h3> What You'll Need To Run This Program </h3>

In order to run Pygen.py, you’ll need Spotipy, a lightweight Python Library for the Spotify API. [You can download it here](https://github.com/plamere/spotipy), or install it with the command line prompt ‘pip install spotipy’.

Further, you’ll need three supplementary Python files provided in this repository in the same folder as pygen.py, which are outlier.py, config.py, and playlistgen.py.

<h3> Authentication </h3>

In order to run the this program, you’ll need to register it as an app in a Spotify Developer account. [You can create an account here](https://developer.spotify.com/dashboard/).

Once you’ve registered it as an app, Spotify will provide you with a unique “Client ID”, “Client Secret”, and 'Redirect URI' for this app. These are necessary to authorize your application to fetch data from Spotify. [More details about Spotify’s authorization process can be found here](https://developer.spotify.com/documentation/general/guides/authorization-guide/).

<p align="center">
<img src="https://developer.spotify.com/assets/WebAPI_intro.png"width="500">
</p>

You’ll need to enter you App’s Client ID, Client Secret, and Redirect URI in Lines 13-15 of ‘config.py’. Lastly, when running pygen.py you'll need to enter in your Spotify username. Currently this program only supports the Spotify username associated with your Spotify for Developers account. The first time you enter your username you'll need to paste the Redirect URI that is created. After that, you'll be set to run the program.

<h3> How It Works </h3>

Below is an overview of the workflow for this program. There are various ways to customize the way recommended songs are chosen in each iteration, as outlined below.

<strong>Program Workflow</strong>

- Prompt user for username
- Authenticate the user’s information (via the Spotify API)
- Prompt the user for info about how Pygen will operate (time period, iterations, random/outlier search, and genre seeds)
- Analyze their top 30 tracks over a specified time period	 
- Given the user input, either grab a random track or use a custom outlier function to return the track who’s audio attributes are least like the average attributes in that group.
- Use Spotify’s recommendation algorithm to search for 10 songs that are similar to the random/outlier track from chosen above. This search function also searches for tracks with audio characteristics similar to the average values of the previous list, scaled by 20-40% to push Spotify to move further away from the original seed.
- Re-perform the previous two steps given the inputted iterations. 
- Print out the results
- Offer to put those tracks into a playlist in that user’s Spotify library.
  
<h3> Example </h3>

Coming soon...

<h3> Reflections </h3>

One of the core subproblems I encountered was how do I skew the recommendations in the way of my choosing - I.e. how do I make it more similar to a user’s taste or take it further away from a listener’s taste.

The first step was to optimize the functions that lead to the final list of tracks. Doing so took refinement and experimentation to have Pygen create playlists that are similar, but not too similar.

Second, Pygen allows the user to input custom data that allows them to affect the trajectory of Pygen. The user can control how far back Spotify looks into their user history, how many playlist iterations it performs, whether it uses a random track from the previous playlist as the seed or it chooses the audio attribute outlier, and whether or not to add a genre into the seeding process.
