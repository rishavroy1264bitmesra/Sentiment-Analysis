import numpy as np
import re
import itertools
from collections import Counter

class DataPreprocessor(object):

    def clean_data(self,string):
        """
        Tokenization/string cleaning for all datasets.
        """
        string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " ( ", string)
        string = re.sub(r"\)", " ) ", string)
        string = re.sub(r"\?", " ? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        return string.strip().lower()

    def load_data_and_labels(self,dataset_path):
        """
        Loads data from files, splits the data into words and generates labels.
        Returns split sentences and labels.
        """
        # Load data from files
        input_lines = list(open(dataset_path).readlines())
        input_lines = [s.strip() for s in input_lines]
        # Split by words
        x_y_separated=dict()
        x_text=list()
        y_label=list()
        for sentence in input_lines:
            temp=sentence.split(',,,')
            x_text.append(temp[0])
            y_label.append(temp[1])

        x_text = [self.clean_data(sent) for sent in x_text]
        x_text = [s.split(" ") for s in x_text]
        # Generate labels
        return [x_text, y_label]


if __name__ == '__main__':
    str="../../dataset/test/labelled_test_data.txt"
    preprocessor=DataPreprocessor()
    print (str)
    for x in preprocessor.load_data_and_labels(str):
        print x

