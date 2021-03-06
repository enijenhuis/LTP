__author__ = "bplank"
"""
Exercise: sentiment classification with logistic regression

1) Examine the code. What are the features used?
   All tokens.
2) What is the distribution of labels in the data?
   50/50
3) Add code to train and evaluate the classifier. What accuracy do you get? What is weird?
   Todo...
4) How could you improve the representation of the data?
   Not sure yet...
5) Implement cross-validation.
   Yep...

"""
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import numpy as np
#from sklearn.cross_validation import train_test_split
#from sklearn.cross_validation import cross_val_score


def load_sentiment_sentences_and_labels():
    """
    loads the movie review data
    """
    # Q1: What are the features used?
    # A1: All tokens from each sentence.
    # Q4: How could you improve the representation of the data?
    # A4: Perhaps represent the text using word embeddings.
    positive_sentences = [line.strip().split(" ") for line in open("rt-polaritydata/rt-polarity.pos").readlines()]
    negative_sentences = [line.strip().split(" ") for line in open("rt-polaritydata/rt-polarity.neg").readlines()]

    # Q2: What is the label distribution?
    # A2: 50/50, 5331 POS and 5331 NEG.
    positive_labels = [1 for sentence in positive_sentences]
    negative_labels = [0 for sentence in negative_sentences]

    sentences = np.concatenate([positive_sentences, negative_sentences], axis=0)
    labels = np.concatenate([positive_labels, negative_labels], axis=0)
    return sentences, labels


def main():
    # read input data
    print("load data..")
    sentences, labels = load_sentiment_sentences_and_labels()
    sentences = [" ".join(sentence) for sentence in sentences]

    # Q: What accuracy do you get when you run the code? What is weird?
    # A: Accuracy: 0.575768942236 this is because we have the split point at 75%
    print("split data..")
    split_point = int(0.75*len(sentences))
    X_train, X_test = sentences[:split_point], sentences[split_point:]
    y_train, y_test = labels[:split_point], labels[split_point:]

    print("#train instances: {} #test instances: {}".format(len(X_train), len(X_test)))
    assert(len(X_train) == len(y_train))
    assert(len(X_test) == len(y_test))

    # Explain to your neighbor, what happens here?
    majority_label = Counter(labels).most_common()[0][0]
    majority_prediction = [majority_label for label in y_test]

    print("vectorize data..")
    vectorizer = CountVectorizer()

    classifier = Pipeline([('vec', vectorizer), ('clf', LogisticRegression())])

    # Q2: add code to train and evaluate your classifier
    print("train model..")
    # your code here:
    classifier.fit(X_train, y_train)
    #
    print("evaluate model..")
    # your code here:
    y_predicted = classifier.predict(X_test)
    #
    print("Accuracy:", accuracy_score(y_test, y_predicted))

    print("Majority baseline:", accuracy_score(y_test, majority_prediction))

if __name__ == "__main__":
    main()
