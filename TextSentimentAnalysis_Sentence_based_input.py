
# coding: utf-8

# In[25]:

import nltk
import csv
positiveWords=[]
negativeWords=[]
#Loading all negative words to a list
with open("G:\DIGI_Learning\UDEMY\Natural_Language_Processing\words-negative.csv","rb") as file:
    reader = csv.reader(file)
    for row in reader:
        #print row
        negativeWords.append(row)
#negativeWords = negativeWords[:10]
#print "Negative ==>",negativeWords
#Loading all positive words to a list
with open("G:\DIGI_Learning\UDEMY\Natural_Language_Processing\words-positive.csv","rb") as file:
    reader = csv.reader(file)
    for row in reader:
        #print row
        positiveWords.append(row)
#positiveWords = positiveWords[:10]
#print "Positive ==>",positiveWords
def sentimentOfText(text):
    negativeCount = 0
    positiveCount = 0
    tokens = nltk.word_tokenize(text)
    #print tokens
    for item in tokens:
        for positem in positiveWords:
            if item in positem:
                positiveCount += 1
        for negitem in negativeWords:
            if item in negitem:
                negativeCount += 1
    if positiveCount > 0:
        print "positive"
    elif negativeCount > 0 and negativeCount %2 == 0:
        print "positive"
    elif negativeCount > 0 :
        print "negative"
    else:
        print "neutral"


# In[23]:

sentimentOfText("It was terribly bad")


# In[26]:

sentimentOfText("ACtually, it was not bad at all")


# In[27]:

sentimentOfText("This is sentence about nothing")


# In[29]:

sentimentOfText("God bless America")


# In[ ]:



