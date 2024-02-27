import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import re

data= pd.read_excel("DatasetKabarOnline.xlsx")


# Get the English stop words list from NLTK
stop_words = set(stopwords.words("english"))
stop_words = list(stop_words)
stop_words = stop_words + ['a','an','irna','isna','khabarfori','seda','sima','wrote','ekhtizidi','macroeconomist','said','tasnim',"Seda and Sima's"]
word_freq = {}
bigram_freq = {}
trigram_freq = {}

# Tokenize the text into words
news=data['News'].loc[2]
text = nltk.word_tokenize(news)  # Tokenize using NLTK's word_tokenize function
words=[word for word in text if (word.lower() not in stop_words) and (word.isalpha())]


# Iterate through the words and count their frequencies
for word in words:
    # Remove punctuation and convert to lowercase for accurate counting
    word = word.strip('.:,!?()[]{}"\' ').lower()

    # Update the word frequency in the dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the word frequencies in descending order by frequency
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Print the sorted word frequencies
#for word, freq in sorted_word_freq[:50]:
#    print(f"{word}: {freq}")

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels and ticks
plt.show()


for i in range(len(words) - 1):
    word1 = words[i].strip('.,!?()[]{}"\'').lower()
    if (word1.lower() not in stop_words) and (word1.isalpha()):
        word2 = words[i + 1].strip('.,!?()[]{}"\'').lower()
        if (word2.lower() not in stop_words) and (word2.isalpha()):
            bigram = word1+ ' ' + word2  # Create a tuple to represent the bigram
        else:
            continue
    else:
        continue

    # Update the bigram frequency in the dictionary
    if bigram in bigram_freq:
        bigram_freq[bigram] += 1
    else:
        bigram_freq[bigram] = 1



# Sort the bigrams by frequency in descending order
sorted_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)

bigram, freq = sorted_bigrams[0]
print('finded bigram is :'+bigram)
for sentence in re.split(r'[.,:]', news):
    #print(sentence)
    index=sentence.find(bigram)
    if index>=0:
       print("topicSentence : "+ sentence)




# Print the sorted word frequencies
#for bigram, freq in sorted_bigrams[:50]:
#    print(f"{bigram}: {freq}")
    
# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(bigram_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels and ticks
plt.show()

# Iterate through the words, remove punctuation, and convert to lowercase for accurate counting
for i in range(len(words) - 2):
    word1 = words[i].strip('.,!?()[]{}"\'').lower()
    if (word1.lower() not in stop_words) and (word1.isalpha()):
        word2 = words[i + 1].strip('.,!?()[]{}"\'').lower()
        if (word2.lower() not in stop_words) and (word2.isalpha()):
            word3 = words[i + 2].strip('.,!?()[]{}"\'').lower()
            if (word3.lower() not in stop_words) and (word3.isalpha()):
                trigram = word1+ ' ' + word2+ ' ' + word3  # Create a tuple to represent the bigram4
            else:
                continue
        else:
            continue
    else:
        continue

    # Update the bigram frequency in the dictionary
    if trigram in trigram_freq:
        trigram_freq[trigram] += 1
    else:
        trigram_freq[trigram] = 1



# Sort the bigrams by frequency in descending order
sorted_trigram = sorted(trigram_freq.items(), key=lambda x: x[1], reverse=True)


# Print the sorted word frequencies
#for bigram, freq in sorted_trigram[:50]:
#    print(f"{bigram}: {freq}")
    
# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(trigram_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels and ticks
plt.show()
