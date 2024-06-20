# this is for making the final data set: 

# libraries: 

import pandas as pd
from project_functions import *

# notes: add a cache 
# >>> (is that stored locally or each itteration tho?)

# data sets:
data = (pd.read_csv('music_dh100_group.csv')
            .drop('Album', axis = 1))
cities = pd.read_csv('uscities.csv')

wave1 = data[data['Wave'] == 1]
wave2 = data[data['Wave'] == 2]
wave3 = data[data['Wave'] == 3]


# so plan is to create a song dictionary and that's all I need to query!

# we could do it by wave?

# cache: 
artists = {}
songs = {}

def artist_cache(a):
    '''storing queried artists'''
    if a in artists:
        return artists[a]
    else:
        artists[a] = get_artist(a)
        return artists[a]
    
def song_cache(s):
    '''storing queried songs'''
    if s in songs:
        return songs[s]
    else:
        songs[s] = song_dictionary(s)
        return songs[s]
    

# now the cleaning: 
    

def data_cleaning(df):
    dictionaries = song_dictionary(df)
    df['Lyrics'] = [s['lyrics'] if s else s for s in dictionaries]
    df['Description'] = [get_description(get_artist(s['artist_names'])) if s else s for s in dictionaries]
    df['Year'] = [get_year(s) if s else s for s in dictionaries]


def clean_rows(df):
    '''removes artists that don't exist in the data set'''
    df['Artist ID'] = df['Artist'].apply(lambda s: get_artist_ID(s))
    df = df[df['Artist_ID'] >= 0]


# test: 
    
cleaned_data = data_cleaning(data.sample(5))

cleaned_data.to_csv('test_data_cleaning1.csv')