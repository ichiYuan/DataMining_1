import sys
import string
import re
import MapReduce

mr = MapReduce.MapReduce()
scores = {}


def mapper(each_tweet):
    # Mapper code goes in here


def reducer(key, list_of_values):

    # Reducer code goes in here


if __name__ == '__main__':
    afinnfile = open(sys.argv[1])       # Make dictionary out of AFINN_111.txt file.
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. #\t means the tab character.
        scores[term] = int(score)  # Convert the score to an integer.
    tweet_data = open(sys.argv[2])
    mr.execute(tweet_data, mapper, reducer)


