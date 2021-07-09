import string
import random

def load_words():
    WORDLIST_FILENAME="words.txt"
    infile=open(WORDLIST_FILENAME,"r")
    line=infile.readline()
    word_list=line.split()
    return word_list    
    # Ye function kaafi jayada words ko load karne mai help karega
    
    # word_list = ["navgurukul", "somi", "computer"]
    # return word_list

def choose_word():
    
    # word_list (list): list of words (strings)
    # ye function ek word randomly return karega
    
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
