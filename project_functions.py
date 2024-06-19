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

# this is my personal token, so if you want to use this you'll have to 
# change this to be yours
# maybe I should make this a method then? 

token = 'HLRORyLWz4776M-RCyF_dAOMBQe9q84xenZadvnQgSO-nO9XOhlqkz5Bc-LH5PlY'
genius = (lyricsgenius.Genius(token, 
                              skip_non_songs = True, 
                              verbose = False, # turns on or off the text responses, should turn off when done debugging
                              remove_section_headers = False,
                              sleep_time = 3, # for the lyrics: no chorus or bridge listed
                              retries = 1) ) # the number of times search should try in event of crashes or timeouts 


# functions time: 
    
def get_artistID(artist):
    '''given the artist name return the artist ID'''
    return genius.search_artist(artist, max_songs = 0).id


def get_lyrics(song = None, s_ID = None):
    '''given a song title or song ID, return the lyrics in plain text
    can print this method to get the website version of the lyrics!
    If given both song title and ID, use the ID for query'''

    if type(s_ID) == int: # ie, user submitted the song ID as opposed to the song title
        lyrics = (genius.search_song(get_full_info = False, 
                   song_ID = s_ID).lyrics)
        return lyrics 
         
    elif type(song) == str: # user submitted sone title instead:
        lyrics = (genius.search_song(title = song,
                    get_full_info = False,).lyrics)
    else:
        # this means nothing was submitted or the type of the 
        # variables is incorrect 
        if song == None and s_ID == None:
            raise Exception('Please enter a song title or song ID')
        if type(s_ID) != int:
            raise Exception('Please enter a number for song ID')
        if type(song) != str:
            raise Exception('Wrong data type for song title: looking for STRING')
    return lyrics 

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
        

def get_year(song):
    '''given SONG, return the year the song came out
    OUTPUT: INT'''
    year = get_release_date(song)['year']
    return year

def get_artist_ID(artist):
    '''given an artist, reaturn their artist ID 
    OUTPUT: INT'''
    artist_info = genius.search_artist(artist, max_songs = 0)
    if artist_info == None:
        return -1
    return artist_info.id


def song_dictionary(artist_ID, song_title, most_popular_only = True):
    '''returns the dictionary of keywords and information about a song
    INPUTS: artist_ID: an integer value
            song_title: the title of the song, not case sensitive
    caveat: will return all songs of that artist with the same or similar title 
    (eg the 10 minute version or Taylor's version vs the original, new features, etc. . . 
    to account for this, the term: most_popular_only can be set to true to only return the most popular 
    version of the song we want''' 
    dictionary = (genius.search_artist_songs(artist_id = artist_ID, 
                            search_term =song_title, 
                                            sort = 'popular'))
    if most_popular_only:
        return dictionary['songs'][0]
    return dictionary['songs']

def get_song_ID(song):
    return song['id']



