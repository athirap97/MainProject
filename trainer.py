import sys
sys.path.append('/home/athira/Desktop/test16/servers/')
import chatbot_config as cfg
import nltk
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
with open(cfg.dataset) as json_data:
    print("here")
    intents = json.load(json_data)
    words = []
    classes = []
    documents = []
    ignore_words = ['?']
    c=0
    # loop across each intent patterns
    for intent in intents['intents']:

        for pattern in intent['patterns']:
            w = nltk.word_tokenize(pattern)  # tokenize each word and add to 'words'
            words.extend(w)
            documents.append((w, intent['tag'])) # add to documents
            if intent['tag'] not in classes:
                classes.append(intent['tag']) # add tag to classes list
    words = nltk.pos_tag(words) # stem and lower each word and remove duplicates
    tags = ['PRP','VBP', 'VBZ']
    words= [w for w in words if w[1] not in tags]
    words= [w[0] for w in words]
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes))) #remove duplicates
    print (len(documents), "documents",documents)
    print (len(classes), "classes", classes)
    print (len(words), "unique stemmed words", words)
    # reate an empty array for output for training data
    training = []
    output = []
    output_empty = [0] * len(classes)
    for doc in documents:		# bag of words for each sentence in training data
        # initialize bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    # create train and test lists
    train_x = list(training[:,0])#training set
    train_y = list(training[:,1])#test set
    tf.reset_default_graph()
    # Build model
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 16)
    net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
    net = tflearn.regression(net)
    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
    # Start training (apply gradient descent algorithm)
    model.fit(train_x, train_y, n_epoch=cfg.epochs, batch_size=cfg.batch_size, show_metric=True)
    model.save('model.tflearn')
    # save all of our data structures
    import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )
