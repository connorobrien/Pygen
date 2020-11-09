# Core program that generates a playlist of music based off of a user's top tracks

import os
import random
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import sys

import outlier # Python file for 'outlier' song detection
import playlistgen # Python file for playlist  generation
import config # Python file for authorization

# Grab authorization info from config.py

username = config.username
sp = config.sp
token = config.token

######## CLASSES ########

# Class that holds the attributes of a song

class Attribute:
    def __init__(self):
        self.attributeA = 0.5
        self.attributeD = 0.5
        self.attributeE = 0.5
        self.attributeI = 0.5
        self.attributeL = 0.5
        self.attributeV = 0.5

    # Functions to grab attribute values
    def getA(self):
        return self.attributeA
    def getD(self):
        return self.attributeD
    def getE(self):
        return self.attributeE
    def getI(self):
        return self.attributeI
    def getL(self):
        return self.attributeL
    def getV(self):
        return self.attributeV

    # Functions to update values
    def updateA(self, newA):
        self.attributeA = newA
        return newA
    def updateD(self, newD):
        self.attributeD = newD
        return newD
    def updateE(self, newE):
        self.attributeE = newE
        return newE
    def updateI(self, newI):
        self.attributeI = newI
        return newI
    def updateL(self, newL):
        self.attributeL = newL
        return newL
    def updateV(self, newV):
        self.attributeV = newV
        return newV

    # Function that applies the vary function to each attribute, then updates that attribute
    def varyAttribute(self):
        tempA = vary(self.attributeA)
        self.updateA(tempA)
        tempD = vary(self.attributeD)
        self.updateD(tempD)
        tempE = vary(self.attributeE)
        self.updateE(tempE)
        tempI = vary(self.attributeI)
        self.updateI(tempI)
        tempL = vary(self.attributeL)
        self.updateL(tempL)
        tempV = vary(self.attributeV)
        self.updateV(tempV)
        return

# Build out a feature class
features = Attribute()


######## FUNCTIONS #########

# Function that averages the values in a list (useful for averaging attributes across multiple songs)
def averageValue(lst):
    total = 0
    for items in lst:
        total = total + items
    average = total/len(lst)
    return average

# Function that changes the value of an attribute by 20-40%.
def vary(attribute):
    # Random binary number generator that says if it goes up or down
    updown = random.randint(0,1)
    if updown == 1:
        # Temporary variable incase number is greater than 1
        tempa = attribute
        # Random number generator 
        rando = random.uniform(1.2,1.4)
        # Multiply inputted attribute by scaler (rando)
        attribute = attribute*rando
        # Make sure attribute is between 0 and 1
        if attribute > 1 or attribute < 0:
            # If not, run the function again
            vary(tempa)
        return attribute
    else:
        rando1 = random.uniform(0.6,0.8)
        # multiply inputted attribute by scaler (rando)
        attribute = attribute*rando1
        return attribute

# Function that randomly chooses a track from a list of tracks
def randomTrack(lst):
    length = len(lst)
    rando4 = random.randint(0,length-1)
    choosentrack = lst[rando4]
    return choosentrack


# Function that prints out the items of a list with the track name and artist
def listPrint(lst):
    # Counter for going through lst
    idx = 0
    print("____________________")
    print("Based off of your listening history, "+str(len(lst))+" tracks you might like are:")
    print("")
    for item in lst:
        # Grab the track id
        trackid = lst[idx]
        # Grab the name
        name = sp.track(trackid)['name']
        # Grab the artist(s) name
        artists =  sp.track(trackid)['artists'][0]['name']
        # Print track name and artist
        print(name+" by "+artists)
        # add one to counter
        idx = idx + 1

# Test function that prints basic info for a single seed (track)
def printSeed(lst):
    print("")
    print("Current seed:")
    trackid = lst[0]
    name = sp.track(trackid)['name']
    artists =  sp.track(trackid)['artists'][0]['name']
    print(name+" by "+artists)
    print("")
        
# Function that updates the attributes in the feature class with the most recent track list
def updateAttributes(lst):
    # Initial attribute lists
    lstAcousticness = []
    lstDanceability = []
    lstEnergy = []
    lstInstrumentalness = []
    lstLiveness = []
    lstValence = []
    for item in lst:
        # Grabs the audio features for an id in lst
        feat =  sp.audio_features([item])      
        # Pull attributes into a lst, and add them up
        lstAcousticness = lstAcousticness + [feat[0]['acousticness']]
        lstDanceability = lstDanceability + [feat[0]['danceability']]
        lstEnergy = lstEnergy + [feat[0]['energy']]
        lstInstrumentalness = lstInstrumentalness + [feat[0]['instrumentalness']]
        lstLiveness = lstLiveness + [feat[0]['liveness']]
        lstValence = lstValence + [feat[0]['valence']]
    # Average those attributes out
    averageAcousticness = averageValue(lstAcousticness)
    averageDanceability = averageValue(lstDanceability)
    averageEnergy = averageValue(lstEnergy)
    averageInstrumentalness = averageValue(lstInstrumentalness)
    averageLiveness = averageValue(lstLiveness)
    averageValence = averageValue(lstValence)
    # Update attributes in features class
    features.updateA(averageAcousticness)
    features.updateD(averageDanceability)
    features.updateE(averageEnergy)
    features.updateI(averageInstrumentalness)
    features.updateL(averageLiveness)
    features.updateV(averageValence)
    # Vary those features for search
    features.varyAttribute()

# Functon that re-performs the recommendation calculation. 
def iterate(lst, iterations, cap):
    if token:
        # Authenticate
        sp = spotipy.Spotify(auth=token)
        ## Find the outlier from a user's top tracks
        # searchmethod = 1 grabs the outlier in each playlist
        if searchmethod == 1:
            track = [outlier.lstOutlier(lst)]
        # Else - grabs a random track
        else:
            track = [randomTrack(lst)]
        # Performs "recommendation" from above seed, using custom targets (attributes + genre) 
        results3 = sp.recommendations(seed_tracks=track, seed_genres = inp4, limit=10, target_acousticness=features.getA(), target_danceability=features.getA(), target_energy=features.getE(), target_instrumentalness=features.getI(), target_liveleness=features.getL(), target_valence=features.getV() )
        # Reset counter
        idx = 0
        # Build new list to store track ids
        lstNew = []
        # Grab the id's from the new seeded list 'results3'
        while idx < 10:
            # Grab a track id
            newrec = results3['tracks'][idx]['id']
            # Add to listNew
            lstNew = lstNew + [newrec]
            # Add one to counter
            idx = idx + 1
        # New variable to print iteration number while this function is running
        newiteration = iterations - 1
        # Update attributes in features class
        updateAttributes(lst)
        # Check if we've gone through all the iterations yet
        if 0 < iterations:
            print('Iteration #', cap - iterations,"...")
            lstNew = iterate(lstNew,newiteration, cap)
    return lstNew



# Empty lists #
        
songlist = [] # New list to keep track of song id's
lstNew = [] # New list for recommendations


########## START ########
print("")
print("____________________________________________________________")
print("Welcome to Pygen, a Python based Spotify Playlist Generator")
print("")
print("Pygen generates a playlist of 10 tracks based off your listening history and our custom algorithm.")
print("")
print("Would you like to customize your settings or use the default?")
inp1 = input("Default = 1, Custom = 2: ")


# Default case - set default search values
if inp1 == "1":
    # Set reasonable defaults
    inp2 = 2 # medium term
    inp3 = 5 # 5 iterations
    inp4 = [] # no genre seed
    # Add 1 to iteration to use as counter in iterate function
    counter1 = inp3 +1
    # Set search method to random
    searchmethod = 2
    print('')
    print("You've got it! Calculating now")

#Custom case
else:
    print("")
    # Set the term length - how far back spotify looks in their library for top songs
    print("How far back in your music history would you like us to go?")
    inp2 = int(input("Not far = 1, Somewhat far = 2, As far as you can = 3: "))
    print("")
    # Set the iteration length - how many times this program re-seeds from the initial playlist
    print('')
    print("How many seeded iterations would you like to perform?")
    print("Larger iterations will result in a more 'obscure' playlist.")
    inp3 = float(input("Choose a integer value between 1 and 50: "))
    while inp3 > 50 or inp3 < 1 or inp3.is_integer() == False:
        print("")
        inp3 = float(input("Input unsuccessful. Choose a integer value between 1 and 50: "))
    print("")
    # Use the random or outlier search method
    print("Would you like Pygen to seed randomly or via outliers?")
    rm = input("Choose (outlier/random): ")
    if rm == 'outlier':
        searchmethod = 1
    else:
        searchmethod = 2
    # Check if the user wants to use a genre seed
    print("")
    inp4 = input("Would like you to add a genre seed? (Y/N): ")
    if inp4 == 'Y':
        print("")
        print("Choose from the following list (copy the genre exactly):")
        print("")
        print('"acoustic", "afrobeat","alt-rock","alternative","ambient","anime","black-metal","bluegrass","blues","bossanova","brazil","breakbeat","british,"')
        print('cantopop","chicago-house","children","chill","classical","club","comedy","country","dance","dancehall","death-metal","deep-house","detroit-techno,"')
        print('"disco","disney","drum-and-bass","dub","dubstep","edm","electro","electronic","emo", "folk","forro","french","funk","garage","german","gospel","goth",')
        print('"grindcore","groove","grunge","guitar","happy","hard-rock","hardcore","hardstyle","heavy-metal","hip-hop","holidays","honky-tonk","house","idm",')
        print('"indian","indie""indie-pop""industrial","iranian","j-dance","j-idol","j-pop","j-rock","jazz","k-pop","kids","latin","latino","malay","mandopop","metal",')
        print('"metal-misc","metalcore","minimal-techno","movies","mpb","new-age","new-release","opera","pagode","party","philippines-opm","piano","pop","pop-film",')
        print('"post-dubstep","power-pop","progressive-house","psych-rock","punk","punk-rock","r-n-b","rainy-day","reggae","reggaeton","road-trip","rock","rock-n-roll",')
        print('"rockabilly","romance","sad","salsa","samba","sertanejo","show-tunes","singer-songwriter","ska","sleep","songwriter","soul","soundtracks","spanish",')
        print('"study","summer","swedish","synth-pop","tango","techno","trance","trip-hop","turkish","work-out","world-music"')
        print("")
        inp5 = input("Choose: ")
    else:
        inp5 = ''
    # Set the genre list to the input
    genrelst = [inp5]
    # Add 1 to the iteration to use as counter in the iterate function
    counter1 = inp3 +1
    print("")
    print("You've got it! Calculating now...")



#### Grab the top 30 tracks of user ####
if token:
    # Authentication
    sp = spotipy.Spotify(auth=token)
    # Create a dictionary with the user's top tracks given limit term limit
    if inp2 == 1:
          term = "short_term"
    if inp2 == 2:
          term = "medium_term"
    if inp2 == 3:
          term = "long_term"
    if token:
        results = sp.current_user_top_tracks(limit=30, time_range=term)
        # Counter for grabbing the track id from the results list
        idx = 0
        for item in results['items']:
            # Grab the song ids for each track, adds them to list
            x = item['id']
            songlist = songlist + [x]
            idx = int(idx)
            idx = idx + 1
    # Add attributes to feature class using songlist
    updateAttributes(songlist)
else:
    print ("Can't get token for", username)

#  Call the iterate function with user info and generated playlist

lstfinal = iterate(songlist,inp3, counter1)

print("Done!")

# Call listPrint to print final list of songs
listPrint(lstfinal)
print("")

# Ask the user whether or not they'd like to create a playlist with these tracks

play = input("Would you like to add these tracks to a playlist (Y/N)? ")
if play == "Y":
    print("")
    playname = input("Give your playlist a new name: ")
    playlistgen.createPlaylist(lstfinal, playname)
    print("")
    print("Done!")
if play =="N":
    print("")
    print("Done!")
