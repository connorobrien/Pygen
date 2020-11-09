## Program that calculates the audio attribute 'outlier' from a list of track id's

import config
import os
import spotipy
import random
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import statistics
import sys


# Grab auth info from config.py
username = config.username
sp = config.sp
token = config.token

# Function that returns the outlier songs from a list of songs
def lstOutlier(lst):
    # Initial attribute lists    
    lstAcousticness = []
    lstDanceability = []
    lstEnergy = []
    lstInstrumentalness = []
    lstLiveness = []
    lstValence = []
    # Initial dictionary for storing cumulative standard deviations
    dictA = dict()
    # Grab attribute values for each item (id) in list
    for item in lst:
            feat =  sp.audio_features([item])
            # Pull those attributes into lists
            lstAcousticness = lstAcousticness + [feat[0]['acousticness']]
            lstDanceability = lstDanceability + [feat[0]['danceability']]
            lstEnergy = lstEnergy + [feat[0]['energy']]
            lstInstrumentalness = lstInstrumentalness + [feat[0]['instrumentalness']]
            lstLiveness = lstLiveness + [feat[0]['liveness']]
            lstValence = lstValence + [feat[0]['valence']]
    # Average those attributes out to use for std
    averageAcousticness = averageValue(lstAcousticness)
    averageDanceability = averageValue(lstDanceability)
    averageEnergy = averageValue(lstEnergy)
    averageInstrumentalness = averageValue(lstInstrumentalness)
    averageLiveness = averageValue(lstLiveness)
    averageValence = averageValue(lstValence)
    #####
    # Counter for grabbing id's from lst
    idx3 = 0
    # Create a dictionary with std dev's for each list item
    for item in lst:
        # Calculate the standard deviation of Acousticness
        stdA = statistics.stdev(lstAcousticness)
        # Calculate std dev of each value
        itemstd = abs((lstAcousticness[idx3]-averageAcousticness)/stdA)
        # Add that value to a dictionary w/track id as key
        dictA[item] = itemstd
        # Add one to counter
        idx3 = idx3 + 1
    # Reset Counter
    idx3 = 0
    # Calculate the remaining standard deviations, add them to dictionary value for given key (id)
    for item in dictA:
        # Calc std dev of the remaining attributes
        stdD = statistics.stdev(lstDanceability)
        stdE = statistics.stdev(lstEnergy)
        stdI = statistics.stdev(lstInstrumentalness)
        stdL = statistics.stdev(lstLiveness)
        stdV = statistics.stdev(lstValence)
        # Calculate std dev of each value
        valueD = abs((lstDanceability[idx3]-averageDanceability)/stdD)
        valueE = abs((lstEnergy[idx3]-averageEnergy)/stdD)
        valueI = abs((lstInstrumentalness[idx3]-averageInstrumentalness)/stdD)
        valueL = abs((lstLiveness[idx3]-averageLiveness)/stdD)
        valueV = abs((lstValence[idx3]-averageValence)/stdD)
        # Add those values to a dictionary
        dictA[item] = dictA[item] + valueD + valueE + valueI + valueL + valueV
        # Add one to counter
        idx3 = idx3 + 1
    # Grab the max value
    outlier = max(dictA, key=dictA.get)
    # Return that track id
    return outlier 

# Function that grabs the average value of a list
def averageValue(lst):
    total = 0
    for items in lst:
        total = total + items
    average = total/len(lst)
    return average
