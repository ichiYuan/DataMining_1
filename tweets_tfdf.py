import MapReduce
import sys
import re
import string


mr = MapReduce.MapReduce()
counter = 1
def mapper(each_tweet):
    # Mapper code goes in here
    text = each_tweet['text']
    text = text.encode('utf-8')
    text = re.sub('https?://\S+', '', text)
    text = re.sub('RT @\S+:','', text)
    text = re.sub('retweet','', text)
    text = re.sub('[#@]\S+', '', text)
    text = text.translate(None,string.punctuation).lower()
    keys = text.split()
    #MAP
    global counter
    key_dict = {}
    for k in keys:
    	if k not in key_dict:
    		key_dict[k] = 0
    	key_dict[k] += 1
    #COMBINER
    for k in key_dict:
    	mr.emit_intermediate(k,(counter,key_dict[k]))
    counter += 1

def reducer(key, list_of_values):
    #reducer code goes in here
    mr.emit((key,len(list_of_values),list_of_values))



if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

