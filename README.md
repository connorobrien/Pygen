# Pygen - A Python Based Song Recommendation Program

Pygen is a program that analyzes a Spotify user’s listening history and generates a list of recommended tracks. It builds on top of Spotify’s recommendation algorithm to generate tracks outside of that user’s immediate taste.

It’s basic workflow is to:
	- Grab the user’s top 30 tracks 
	- Create a playlist of 10 tracks from one of their top 30 tracks.
	- Generate another playlist of 10 tracks from one of the previous 10.
	- Continue to generate new playlists to step further away from the user’s top tracks
	- Display the final list of 10 songs and offer to put them into a Spotify playlist in their account. 

<h3>Motivation </h3>

My motivation for this project stemmed from a dissatisfaction with the song recommendations provided to me by Spotify. Spotify  

<h3> What you'll need </h3>

In order to run Pygen.py, you’ll need Spotipy, a lightweight Python Library for the Spotify API.

You can download it at https://github.com/plamere/spotipy, or install it with the command line prompt ‘pip install spotipy’.

Further, you’ll need three supplementary Python files in the same folder as pygen.py, which are outlier.py, config.py, and playlistgen.py.

<h3> Authentication </h3>

In order to run the this program, you’ll need to register it as an app in a Spotify Developer account. You can create an account here https://developer.spotify.com/dashboard/.

Once you’ve registered it as an app, Spotify will provide you with a unique “Client ID” and “Client Secret” for this app. These are necessary to authorize your application to fetch data from Spotify. More details about Spotify’s authorization process can be found here https://developer.spotify.com/documentation/general/guides/authorization-guide/.

You’ll need to enter you App’s Client ID and Client Secret in ‘config.py’ under the client_id and client_secret, respectively. REDIRECT URI

<h3> How It Works </h3>

My overall approach was to experiment and optimize the various ways I could generate seeded playlists from a user’s listening history. 

A more detailed version of the Pygen workflow is:

	- Prompt user for username
	- Authenticate the user’s information (via the Spotify API)
	- Prompt the user for info about how Pygen will operate (time period, iterations, random/outlier search, and genre seeds)
	- Analyze their top 30 tracks over a specified time period	 
	- Given the user input, either grab a random track or use a custom outlier function to return the track who’s audio attributes are least like the average attributes in that group.
	- Use Spotify’s recommendation algorithm to search for 10 songs that are similar to the random/outlier track from above. This search function also searches for tracks with audio characteristics similar to the average values of the previous list, scaled by 20-40% to push Spotify to move further away from the original seed.
	- Re-perform the previous two steps given the inputted iterations. 
	- Print out the results
	- Offer to put those tracks into a playlist in that user’s Spotify library.
  
<h3> Example </h3>

Coming soon...

<h3> Reflections </h3>

One of the core subproblems I encountered was how do I skew the recommendations in the way of my choosing - I.e. how do I make it more similar to a user’s taste or take it further away from a listener’s taste.

The first step was to optimize the functions that lead to the final list of tracks. Doing so took refinement and experimentation to have Pygen create playlists that are similar, but not too similar.

Second, Pygen allows the user to input custom data that allows them to affect the trajectory of Pygen. The user can control how far back Spotify looks into their user history, how many playlist iterations it performs, whether it uses a random track from the previous playlist as the seed or it chooses the audio attribute outlier, and whether or not to add a genre into the seeding process.
