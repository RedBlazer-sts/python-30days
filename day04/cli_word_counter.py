from collections import Counter

def user_paragraph():
    paragraph= input("Write Down your paragraph: ")
    return paragraph

def word_frequency(paragraph):
    frequencis=Counter(paragraph.split())
    return frequencis

def unique_words(paragraph):
    unique_words_freq = set(paragraph.split())
    return unique_words_freq

def top_3_words(frequency):
   return frequency.most_common(3)

paragaph=user_paragraph()
word_frequency(paragaph)
unique_words(paragaph)
top_3_words(paragaph)