# Text Summarizer

**Technologies Used**: Python, Flask, Wikipedia API, NLTK 

## Purpose and Reason
There is so much information now on the internet and on sites such as Wikipedia. However many sites including 
Wikipedia overwhelms you with loads of information, pictures and links. I find that many times, when I am on 
these sights, I am mostly looking for a general overview of the topic that I am searching. I bulit text-summarizer
to do just that.

I have implemented two different algorithms to summarize the text. The first uses simple maths. It calculates the count of each
word and stores them as values. Each sentence is then given a total value score and if a sentence scores higher than the 
weight * average score, it gets concatenated to the final summary string. This is a very trivial solution.The second algorithm is the well known TF-IDF algorithm which is short for term frequency–inverse document frequency. Finally, I have created low-level, mid-level, and high-level summarization options which simply change the value of the weight.