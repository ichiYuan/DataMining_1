import sys
import string
import re
import MapReduce

mr = MapReduce.MapReduce()
scores = {}
counter = 1

def mapper(each_tweet):
    # Mapper code goes in here
    text = each_tweet['text']
    text = text.encode('utf-8')
    text = re.sub('https?://\S+', '', text)
    text = re.sub('[#@]\S+', '', text)
    text = text.translate(None,string.punctuation).lower()
    keys = text.split()
    global counter
    flag = False
    for k in keys:
    	if k in scores:
    		flag = True
    		mr.emit_intermediate(counter, scores[k])
    if not flag:
    	mr.emit_intermediate(counter,0)
    counter += 1

def reducer(key, list_of_values):
    # Reducer code goes in here
    total = 0
    for v in list_of_values:
    	total += v
    mr.emit((key, total))


if __name__ == '__main__':
    afinnfile = open(sys.argv[1])       # Make dictionary out of AFINN_111.txt file.
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. #\t means the tab character.
        scores[term] = int(score)  # Convert the score to an integer.
    tweet_data = open(sys.argv[2])
    mr.execute(tweet_data, mapper, reducer)


