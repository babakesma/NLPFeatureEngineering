import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# Sample text data (synthetic example)
def CollocationAndMeasures(text):
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)

    # Create a BigramCollocationFinder
    finder = BigramCollocationFinder.from_words(tokens)

    # Apply a scoring measure (e.g., PMI - Pointwise Mutual Information)
    # You can use different scoring measures based on your needs.
    scored_collocations = finder.score_ngrams(BigramAssocMeasures.chi_sq)

    # Sort the collocations by score (you can also use other criteria)
    sorted_collocations = sorted(scored_collocations, key=lambda x: x[1], reverse=True)

    # Print the top collocations
    return scored_collocations