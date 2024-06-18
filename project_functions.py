# so im gonna build a library that can do all the lil things I need for my project: 
# find artist information
# find song information
# maybe some text analysis component 

# need to install this first, so I'll put the steps here somewhere 
import lyricsgenius

# this is my personal token, so if you want to use this you'll have to 
# change this to be yours
# maybe I should make this a method then? 

token = 'HLRORyLWz4776M-RCyF_dAOMBQe9q84xenZadvnQgSO-nO9XOhlqkz5Bc-LH5PlY'
genius = (lyricsgenius.Genius(token, 
                              skip_non_songs = True, 
                              verbose = False, # turns on or off the text responses, should turn off when done debugging
                              remove_section_headers = False, # for the lyrics: no chorus or bridge listed
                              retries = 3) ) # the number of times search should try in event of crashes or timeouts 


# functions time: 
    
def get_artistID(artist):
    '''given the artist name return the artist ID'''
    return genius.search_artist(artist, max_songs = 0).id


def get_lyrics(art = None, song = None, s_ID = None):
    '''given a song title or song ID, return the lyrics in plain text
    can print this method to get the website version of the lyrics!
    If given both song title and ID, use the ID for query'''
    
    if art == None:
        raise Exception("Please provide an artist name")
    if type(s_ID) == int: # ie, user submitted the song ID as opposed to the song title
        lyrics = (genius.search_song(artist = art,
                   get_full_info = False, 
                   song_ID = s_ID).lyrics)
        return lyrics 
         
    elif type(song) == str: # user submitted sone title instead:
        lyrics = (genius.search_song(title = song,
                    artist = art,
                    get_full_info = False, 
                   ))
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



