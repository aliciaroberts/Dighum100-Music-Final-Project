# this is for making the final data set: 

# libraries: 

import pandas as pd
from project_functions import *

# notes: add a cache 
# >>> (is that stored locally or each itteration tho?)

# data sets:
songs = (pd.read_csv('music_dh100_group.csv')
            .drop('Album', axis = 1))
cities = pd.read_csv('uscities.csv')


# so plan is to create a song dictionary and that's all I need to query!

# we could do it by wave?

# cache: 

def artist_cache(a):
    '''storing queried artists'''
    artists = {}
    if a in artists:
        return artists[a]
    else:
        artists[a] = get_artist(a)
        return artists[a]
    
    
def song_cache(s):
    '''storing queried songs'''
    songs = {}
    if s in songs:
        return songs[s]
    else:
        songs[s] = song_dictionary(s)
        return songs[s]