import re
#turns whatever text input you give it into tweets
fname = 'tweets.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
tweetinp = input('enter the text to turn into tweets')
words = re.findall(r"\w(?<!\d)[\w'-]*)", tweetinp)
tweetnum = []
#for word in words:
#
#    if len(tweetnum) < 250 and len(word) < 15 :
#
print(words)