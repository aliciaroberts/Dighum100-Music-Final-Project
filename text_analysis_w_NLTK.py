# using NLTK 
# import nltk 
# nltk.download('punkt')

# for creating tokens:
from nltk.tokenize import word_tokenize

# for removing stop words:
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) # this sets the language of our stop words and creates a default list 

# for stemming (getting root words)
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# for getting pairs of words (bigrams):
from nltk.util import bigrams

# for regular expressions !
import re 

you_dont_own_me = """[Verse 1]
You don't own me
I'm not just one of your many toys
You don't own me
Don't say I can't go with other boys

[Chorus]
And don't tell me what to do
Don't tell me what to say
And please, when I go out with you
Don't put me on display 'cause

[Verse 2]
You don't own me
Don't try to change me in any way
You don't own me
Don't tie me down 'cause I'd never stay

[Chorus]
I don't tell you what to say
I don't tell you what to do
So just let me be myself
That's all I ask of you

[Bridge]
I'm young and I love to be young
I'm free and I love to be free
To live my life the way I want
To say and do whatever I please
 [Chorus]
And don't tell me what to do
Oh, don't tell me what to say
And please, when I go out with you
Don't put me on display
I don't tell you what to say
Oh, don't tell you what to do
So just let me be myself
That's all I ask of you

[Outro]
I'm young and I love to be young
I'm free and I love to be"""

def remove_notation(str):
    '''given a string of song lyrics, remove any formatting such as verse, intro, chorus, etc. . .
    given that the lyrics come from lyrics genius API'''
    pattern = '(\[\w*\s?\d?\])' # this is the segement to be removed
    repl = '' # just get rid of it! 
    return re.sub(pattern, repl, str)

# test:

# print(you_dont_own_me, '\n\n\n')
# print('new version: \n\n',remove_notation(you_dont_own_me))
# spoiler alert it works: 

# now let's do some text analysis 

you_dont_own_me_cleaned = remove_notation(you_dont_own_me)

you_dont_own_me_tokenized = word_tokenize(you_dont_own_me_cleaned)

# print(you_dont_own_me_tokenized)

# let's see the distribution of words:

import matplotlib.pyplot as plt 



you_dont_own_me_word_counts = {x: you_dont_own_me_tokenized.count(x) for x in set(you_dont_own_me_tokenized)}


# plt.bar(x = you_dont_own_me_word_counts.keys(), height = you_dont_own_me_word_counts.values(), label = 'you_dont_own_me_bar_plot')
# plt.xticks(rotation=55)
# plt.yticks(range(0,max(you_dont_own_me_word_counts.values()),1))
# plt.title("Distribution of Word Counts in Leslie Gore's You Don't Own Me")
# # plt.show()

import pandas as pd


data = {'Word': you_dont_own_me_word_counts.keys(), 'Count':you_dont_own_me_word_counts.values()}

you_dont_own_me_table = pd.DataFrame.from_dict(data, orient = 'columns')

you_dont_own_me_table['Word'] = you_dont_own_me_table['Word'].str.lower()

data_filtered = you_dont_own_me_table[you_dont_own_me_table['Count'] > 3]

print(data_filtered.head())

import seaborn as sns 

sns.countplot(x = you_dont_own_me_tokenized)
plt.show()