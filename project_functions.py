# im gonna build a library that can do all the lil things I need for my project: 
# find artist information
# find song information
# maybe some text analysis component 

# need to install this first, so I'll put the steps here somewhere
# okay yeah so basically 1: go into your terminal or wherever you install
# your packages. 
# then 2: make sure that you set your path to the one that leads to PATH
# this is for windows, so im not sure how it works on mac or linux, but for me
# it was called PATH_Programs
# 3: then do this command:
# < py -m pip install lyricsgenius > <- py is for windows, python for mac
# if it installs properly then you can inport the library fine and 
# this code shouldn't error 

import lyricsgenius
import numpy as np

# this is my personal token, so if you want to use this you'll have to 
# change this to be yours
# maybe I should make this a method then? 

token = 'HLRORyLWz4776M-RCyF_dAOMBQe9q84xenZadvnQgSO-nO9XOhlqkz5Bc-LH5PlY'
genius = (lyricsgenius.Genius(token, 
                              skip_non_songs = True, 
                              verbose = True, # turns on or off the text responses, should turn off when done debugging
                              remove_section_headers = False, # for the lyrics: no chorus or bridge listed
                              sleep_time = 20, # extend this to avoid usage limits default 0.2
                              retries = 1) ) # the number of times search should try in event of crashes or timeouts 


    

# functions time: 

def get_artist(artist):
    dic = (genius.search_artist(artist, 
                                    max_songs = 0, 
                                    get_full_info = False, # should speed up the process 
                                    allow_name_change = True)) # could find the right artist or the totally wrong one who knows. . .
    if dic != None:
        dic =  dic.to_dict()
    return dic


def song_dictionary(df):
    '''given a data frame that contains artist name and song title (or optionally artist ID),
    return a dictionary that contains information on that song
    CURRENT ISSUE: sometimes returns the totally wrong song :(('''
    dicts = [] # list of dictionaries that can be added to the data frame 
    for i in range(len(df)):
        # so itterate through each row if done properly:
        dictionary = genius.search_song(title = df['Song'].iloc[i],artist = df['Artist'].iloc[i])
        if dictionary == None:
            dicts.append(dictionary)
        else:
            dicts.append(dictionary.to_dict())
    return dicts


def get_lyrics(song):
    '''given a song dictionary, return the lyrics in plain text'''
    return song['lyrics']


def get_release_date(song_dict, form = 'd'):
    '''given a song dictionary, return the date the song came out.
    if form == r, then return the readable option
    otherwise return the dictionary version
    OUTPUT: either INT or DICT'''
    if form == 'd':
        return song_dict['release_date_components'] # this one is better
    if form == 'r':
        return song_dict['release_date_for_display']
    else:
        raise Exception('Wrong form selected, please choose d for DICTIONARY or r for plain text')
        

# ERROR HERE : 
#         year = get_release_date(song)['year']
#            ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
# TypeError: 'NoneType' object is not subscriptable
def get_year(song):
    '''given SONG, return the year the song came out
    OUTPUT: INT'''
    year = -1 # default value for no data 
    if song != None:
        year = get_release_date(song)['year']
    return year


def get_artist_ID(artist):
    '''given an artist, reaturn their artist ID 
    OUTPUT: INT'''
    artist_info = get_artist(artist)
    if artist_info == None:
        return -1
    return artist_info.id


def get_description(artist_dic):
    '''returns the description of an artist if applicable'''
    if artist_dic != None:
        return artist_dic['description']['plain']
    return -1





