# Install the gensim library if you haven't already
# !pip install gensim

import gensim
from gensim import corpora
from gensim.models import LdaModel
import random

# Sample text data (synthetic example)
documents = [
    'Estimates show that the Iranian stock market is progressive and bullish.',
    'The point here is that if the fever of risks increases and their effect on the economy increases, there is even a possibility that the stock market will not grow.'
]

# Preprocess the text data
tokenized_documents = [document.split() for document in documents]

# Create a dictionary mapping words to unique IDs
dictionary = corpora.Dictionary(tokenized_documents)

# Create a bag-of-words representation of the documents
corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

# Train the LDA model
lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=10, random_state=42)

# Extract representative sentences for each topic
topic_sentences = {}

for topic_id, topic in lda_model.print_topics():
    topic_sentences[topic_id] = []

for i, doc in enumerate(corpus):
    topic_distribution = lda_model.get_document_topics(doc)
    dominant_topic = max(topic_distribution, key=lambda x: x[1])
    topic_id = dominant_topic[0]
    topic_sentences[topic_id].append(documents[i])

# Print representative sentences for each topic
for topic_id, sentences in topic_sentences.items():
    print(f"Topic {topic_id + 1} - Representative Sentences:")
    for sentence in sentences:
        print(f"- {sentence}")
    print()
