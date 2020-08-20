from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def generate_freq_table(text):
    '''
    Create a dictionary for the word frequency not counting stopwords

    :return: a dictionary of words and the corresponding value
    '''
    stop_words = set(stopwords.words('english')) 
    words = word_tokenize(text)

    ps = PorterStemmer()

    freq_table = {}
    for word in words:
        word = ps.stem(word)
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table

def generate_sentences(text):
    '''
    Split the text into sentences

    :return: a list of sentences 
    '''
    return sent_tokenize(text)
    
def score(sentences, freq_table):
    '''
    Score each sentence based on the total sum value of its words

    :return: a dictionary 
    '''
    sentence_value = {} 
    
    for sentence in sentences:
        total_words_in_sentence = (len(word_tokenize(sentence)))
        
        for word_value in freq_table:
            if word_value in sentence.lower():
                if sentence[:10] in sentence_value:
                    sentence_value[sentence[:10]] += freq_table[word_value]
                else:
                    sentence_value[sentence[:10]] = freq_table[word_value]

        sentence_value[sentence[:10]] = sentence_value[sentence[:10]] // total_words_in_sentence

    return sentence_value

def generate_threshold(sentence_value):
    threshold_sum = 0
    for sentence in sentence_value:
        threshold_sum += sentence_value[sentence]

    calcuate_average = int(threshold_sum / len(sentence_value))

    return calcuate_average

def generate_final_summary(sentences, sentence_scores, threshold):
    '''
    Concatenate the sentence in the final summary if the sentence value
    is greater than the calculated threshold

    :return: A string which represents the final summary
    '''
    count = 0
    final_summary = ''

    for sentence in sentences:
        if sentence[:10] in sentence_scores and sentence_scores[sentence[:10]] > threshold:
            final_summary += ' ' + sentence
            count += 1

    return final_summary

def call_summary(text, weight):
    '''
    Called by the Flask application

    :return: the string which represents the final summary
    '''
    freq_table = generate_freq_table(text)
    sentences = generate_sentences(text)
    sentence_scores = score(sentences, freq_table)
    threshold = generate_threshold(sentence_scores)
    summary = generate_final_summary(sentences, sentence_scores, weight * threshold)
    
    return summary
