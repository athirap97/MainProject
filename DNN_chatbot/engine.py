import sys
sys.path.append('/home/athira/Desktop/test16/')
import chatbot_config as cfg
import pickle
data = pickle.load( open( "../DNN_chatbot/training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']
# import json module to use dataset
import json
with open("../DNN_chatbot/"+cfg.dataset) as json_data:
    intents = json.load(json_data)
import tensorflow as tf
import tflearn
net = tflearn.input_data(shape=[None, len(train_x[0])]) #inputs data to a network
net = tflearn.fully_connected(net, 16) 
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)
# Definition of model to setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('../DNN_chatbot/model.tflearn')
import nltk
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
import numpy as np #converting input to numeric form
import random
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)	    # tokenize each sentence into words
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]    # stem each word in the words tokenized
    return sentence_words
# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)	    # tokenize the pattern
    bag = [0]*len(words)	    # bag of words
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))
context={}	#response generator
ERROR_THRESHOLD = cfg.error
def classify(sentence):
    results = model.predict([bow(sentence, words, True)])[0]	    # generate probabilities from the model
    print (results)
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]	    # filter out predictions below a threshold
    print (results)	    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    print(return_list)	    # return tuple of intent and probability
    return return_list
def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    print('results:' + str(results))
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']
                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        s=(random.choice(i['responses']))
                        if (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                            context[userID] = ""
                        print (s)
                        return s
            results.pop(0)
    return "Sorry, I am unable to reply to that question at the moment."
