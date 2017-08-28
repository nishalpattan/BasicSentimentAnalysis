import nltk
import numpy as np
import csv
positiveWords=[]
negativeWords=[]
comments = []
#Loading all negative words to a list
with open("G:\DIGI_Learning\UDEMY\Natural_Language_Processing\words-negative.csv","rb") as file:
    reader = csv.reader(file)
    for row in reader:
        #print row
        for i in row:
            negativeWords.append(i)
#negativeWords = negativeWords[:10]
#print "Negative ==>",negativeWords
#Loading all positive words to a list
with open("G:\DIGI_Learning\UDEMY\Natural_Language_Processing\words-positive.csv","rb") as file:
    reader = csv.reader(file)
    for row in reader:
        #print row
        for i in row:
            positiveWords.append(i)
#positiveWords = positiveWords[:10]
#print "Positive ==>",positiveWords
with open("G:\\DIGI_Learning\\UDEMY\\Natural_Language_Processing\\reviews.csv","rb") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row)
#print comments
def sentimentOfText(text):
    temp=[]
    #toeknizing all the sentences
    sent_tokens = nltk.sent_tokenize(text)
    #tokenizing all sentences to words
    for sentence in sent_tokens:
        negativeCount = 0
        positiveCount = 0
        word_tokens=nltk.word_tokenize(sentence)
    #print word_tokens
        for item in word_tokens:
            for positem in positiveWords:
                if item == positem:
                    positiveCount += 1
            for negitem in negativeWords:
                if item == negitem:
                    negativeCount+=1
        if positiveCount > 0 and negativeCount==0:
            temp.append(1)
        elif negativeCount > 0 and negativeCount %2 == 0:
            temp.append(1)
        elif negativeCount > 0 :
            temp.append(-1)
        else:
            temp.append(0)
    return temp
for review in comments:
    print "\n"
    decisionScale=np.average(sentimentOfText(str(review)))
    print decisionScale
    if decisionScale < 0:
        print "Negative review"
    elif decisionScale > 0:
        print "Positive Review"
    else:
        print "Neutral Review"
    print review
