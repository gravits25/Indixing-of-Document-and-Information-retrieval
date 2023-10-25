import nltk
from nltk import bigrams, trigrams, FreqDist
from nltk.corpus import stopwords


file_content = ""

for i in range(103):
    file_path = f'./Emails\\email_{i}.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content += file.read()


file_content = file_content.replace('\n', ' ')
file_content = file_content.replace('\\n', ' ')
file_content = file_content.replace('\n\n', ' ')
file_content = file_content.replace('>', ' ')
file_content = file_content.replace('<', ' ')
file_content = file_content.replace('/', ' ')
file_content = file_content.replace(':', ' ')
file_content = file_content.replace(')', ' ')
file_content = file_content.replace('(', ' ')
file_content = file_content.replace(',', ' ')

# print(file_content)


tokens = nltk.word_tokenize(file_content)

# print(tokens)

stoplist = set(stopwords.words('english'))

without_stopwords = [word for word in tokens if word.lower() not in stoplist]

# print(without_stopwords)

# Create bigram and trigram models
bigram_model = list(bigrams(without_stopwords))
trigram_model = list(trigrams(without_stopwords))

# for item in bigram_model:
#     print(item)


bigram_freq = FreqDist(bigram_model)
# trigram_freq = FreqDist(trigram_model)

# print(bigram_freq)

import random

def generate_random_text(model, seed, num_words=10):
    text = seed
    current_word = seed

    for _ in range(num_words - 1):
        next_words = [word2 for (word1, word2) in model if word1 == current_word]

        if next_words:
            next_word = random.choice(next_words)
            text += ' ' + next_word
            current_word = next_word
        else:
            break

    return text

def generate_random_text_trigram(trigram_model, seed, num_words=10):
    text = seed
    current_words = seed.split()  

    for _ in range(num_words - len(current_words)):
        
        next_words = [word3 for (word1, word2, word3) in trigram_model if (word1, word2) == tuple(current_words[-2:])]

        if next_words:

            next_word = random.choice(next_words)
            text += ' ' + next_word
            current_words.append(next_word)
        else:
            break

    return text

# Example usage
seed_word = 'Gaurav'
random_bigram_text = generate_random_text(bigram_model, seed_word, num_words=5)
random_trigram_text = generate_random_text_trigram(trigram_model, seed_word, num_words=5)
print(random_bigram_text)
print(random_trigram_text)

