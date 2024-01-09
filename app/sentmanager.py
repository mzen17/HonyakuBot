# Sentence Manager class to pull sentences from tsv

import csv
import random

class SentManager:
    def __init__(self, tsv_path):
        self.tsv_path = tsv_path
        self.sentences = []
        self.load_sentences()

    def load_sentences(self):
        with open(self.tsv_path, newline='') as tsv_file:
            reader = csv.reader(tsv_file, delimiter='\t')
            for row in reader:
                self.sentences.append(row[0])

    def get_random_sentence(self):
        return random.choice(self.sentences)
    
    