# Pygen - A Python Based Spotify Song Recommendation Program

Pygen is a program that analyzes a Spotify user’s listening history and generates a list of recommended tracks. It builds on top of Spotify’s recommendation algorithm to generate tracks outside of a user’s immediate taste.

<h3>Motivation </h3>

My motivation for this project stemmed from my ambivalent experience with Spotify's recommendation algorithm. Every Monday morning, Spotify provides each user with a personalized playlist of 30 recommended songs in a playlist called Discover Weekly. While I have found excellent songs in this playlist, I've often found the songs I'm recommended are often 'knockoff' versions of the artists I listen to. 

<p align="center">
<img src="https://raw.githubusercontent.com/connorobrien/Pygen/main/DiscoverWeeklyExample.png"width="700">
</p>

When I discover a new artist I’m enamoured with, it’s rarely an artist in the same styles I listen to. Rather, it’s an artist whose music shares stylistic similarities with my favorite artists, while offering some unique and distinct characteristics. My most successful artist recommendations are ones that are similar to the artists I enjoy, but not too similar. This program implements this idea, creating customizable song recommendations that ‘step further’ away from a person’s music taste.

The general approach for this program is to create chained recommendations from an user’s Spotify listening history. It starts with their 30 most listened to songs on Spotify, recommends ten songs they might enjoy from one of these 30 songs, chooses one of the recommended ten songs to recommend another ten songs from, and repeats this process for several iterations. My proposal is that more iterations will provide recommendations that are more distinct from a user’s listening history, and by using their listening history as a starting point, these recommendations might provide new and exciting music recommendations.

<p align="center">
<img src="https://raw.githubusercontent.com/connorobrien/Pygen/main/WorkflowDiagram.png"width="700">
</p>


<h3> What You'll Need To Run This Program </h3>

To run this program, you'll need the four python files provided in this repository, which includes the main file pygen.py, as well the supplementary files outlier.py, config.py, and playlistgen.py.

In order to run pygen.py, you’ll need Spotipy, a lightweight Python library for the Spotify API. [You can download it here](https://github.com/plamere/spotipy), or install it with the command line prompt ‘pip install spotipy’.

<h3> Authentication </h3>

In order to run this program, you must register it as an app in a Spotify for Developers account. [You can create an account here](https://developer.spotify.com/dashboard/).

Once you’ve registered it as an app, Spotify will provide you with a unique “Client ID”, “Client Secret”, and 'Redirect URI' for the app. These are necessary to authorize your application to fetch data from Spotify. [More details about Spotify’s authorization process can be found here.](https://developer.spotify.com/documentation/general/guides/authorization-guide/)

<p align="center">
<img src="https://developer.spotify.com/assets/WebAPI_intro.png"width="500">
</p>

You’ll need to enter your App’s Client ID, Client Secret, and Redirect URI in Lines 13-15 of ‘config.py’. When running pygen.py, you'll need to enter your Spotify username. Currently this program only supports the Spotify username associated with your Spotify for Developers account. The first time you enter your username, you'll need to paste the Redirect URI that is created. After that, you'll be set to run the program.

<h3> How It Works </h3>

Below is a summary of the workflow for this program. There are various ways to customize the way recommended songs are chosen in each iteration, as outlined below.

<strong>Program Workflow</strong>

- Prompt for the user's Spotify username.
- Authenticate the user’s information (via the Spotify API).
- Prompt the user for info about how Pygen will operate (time period, iterations, random/outlier search, and genre seeds).
- Analyze their top 30 tracks over a specified time period.
- Given the user input, select either a random track from the 30 selected above or use a custom outlier function to return the track whose audio attributes are least like the average attributes in that group.
- Use Spotify’s recommendation algorithm to search for 10 songs similar to the random/outlier track chosen above. This search function also searches for tracks with audio characteristics similar to the average values of the previous list, scaled by 20-40% to push Spotify to move further away from the current seed track.
- Re-perform the previous two steps given the chosen amount of iterations. 
- Print out the results.
- Offer to create a playlist with the final ten songs in the user's Spotify library.
  
<h3> Example </h3>

Below is an example of this program in action [(click here if the GIF isn't loading)](https://media.giphy.com/media/TV1jwAn2EPOqfzL5Pq/giphy.gif).
 
<p align="center">
<img src="https://media.giphy.com/media/TV1jwAn2EPOqfzL5Pq/giphy.gif">
</p>

How did the program do? Four of the ten artists I had never heard of, and nine out of ten songs were brand new to me. The only song I was familiar with, Lazy Eye by the Silversun Pickups, I hadn't listened to since high school (before I used Spotify), so overall I'd say the program did a great job. It took an unexpected path into mid 2000's alternative rock that I was pleasantly suprised with. The playlist from this example (pictured below) [can be found here.](https://open.spotify.com/playlist/1crgYKiOXQ2DAliZBnrsW2?si=wdM5shPHRCKBery5wQYjPQ).

<p align="center">
<img src="https://raw.githubusercontent.com/connorobrien/Pygen/main/PlaylistExample.png"width="700">
</p>


<h3> Reflections </h3>

One of the core problems I encountered in this project was how to practically skew the song recommendations; i.e., how do I make them more or less similar to a user's taste?

The first step was to optimize the functions that lead to the final list of recommended tracks. Doing so took refinement and experimentation to have Pygen create recommendations that are similar, but not too similar.

Second, Pygen allows the user to input custom settings that affect the trajectory of Pygen. The user can control how far back Spotify looks into their listening history, how many playlist iterations it performs, whether it uses a random track from the previous playlist as the seed or it chooses the audio attribute outlier, and whether to add a genre into the seeding process.

I found the most 'successful' recommendations used 10+ iterations with random seeds for each iteration. The outlier method was a fun experiment using the audio attribute data provided by Spotify (such as the 'danceability' or 'acousticness' of a song), but its path is inherently less random and results in a similar final list of song recommendations. 

The random seed method has more variability, which produces more unique playlists each time through. In my experience, it may grab one of the  acoustic folk tracks from my listening history as the initial seed, or it may grab a dancier electronic track. Both initial seeds will result in vastly different final recommendations.

<h3> Comments </h3>

Please reach out with any comments/questions/complaints about this program! 


