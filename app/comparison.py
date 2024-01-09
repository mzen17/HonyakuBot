# Sentence Comparison class to compare sentences
# Uses sentencepiece for embedding
# Cosine Similarity for sentence comparison

from sentence_transformers import SentenceTransformer, util

class Comparator:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def compare_sentences(self, sentence1, sentence2):
        embeddings = self.model.encode([sentence1, sentence2])
        cosine_scores = util.pytorch_cos_sim(embeddings[0], embeddings[1])
        return cosine_scores.item()
    
