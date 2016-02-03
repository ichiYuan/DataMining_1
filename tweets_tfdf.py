import MapReduce
import sys
import re
import string


mr = MapReduce.MapReduce()

def mapper(each_tweet):
    # Mapper code goes in here


def reducer(key, list_of_values):
    #reducer code goes in here



if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

