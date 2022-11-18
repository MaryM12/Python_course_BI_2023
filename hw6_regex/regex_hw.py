### Regex HW

import re
import matplotlib.pyplot as plt

#download the input file
# !wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references

# Task 1

with open('/content/references') as inp_file, open('ftps', "w") as file_with_ftps:
    pattern = r"ftp\.[\w./#]*"  #matches links either with or without file extentions
    for line in inp_file:
        for link in re.findall(pattern, line):
            print(link.strip().replace(';', ''), file=file_with_ftps, sep = '\n') # write the output into a file


# Task 2
#download the input file
# !wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD

with open("/content/2430AD") as inp_file, open('numbers', "w") as file_with_nums:
    pattern_num = r"((\d+(\.\d+)?)|(\.\d+))" # a pattern that matches all numbers
    for line in inp_file:
        match = re.findall(pattern_num, line)
        for num in match:
            print(num[0], file=file_with_nums, sep = '\n')  # write the output into a file




# Task 3

with open("/content/2430AD") as inp_file, open('a_words', "w") as file_a:
    pattern_a = r"\w*[a]\w*" # a pattern for words with letter "a"
    for line in inp_file:
        match = re.findall(pattern_a, line, re.IGNORECASE)
        for word in match:
            print(word, file=file_a, sep = '\n') # write the output into a file


# Task 4

with open("/content/2430AD") as inp_file, open('exclamations', "w") as file_excl:
    pattern_excl = r"([A-Z][^\.!?]*!)" # a pattern for exclamations
    for line in inp_file:
        match = re.findall(pattern_excl, line)
        for sentence in match:
            print(sentence, file=file_excl, sep = '\n') # write the output into a file

# Task 5

# 5. Постройте гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте. 

pattern_words = r"[a-zA-Z\'\-]+"  #not including numbers; a word may contain "-" and "'" symbols
with open("/content/2430AD") as inp_file:
    story = inp_file.read()       #read the whole file

word_list = re.findall(pattern_words, story)
unique_words = set([x.lower() for x in word_list])
# number of unique words
len_all = len(unique_words)
# make a dictionary word length : words
dict_words = {}          
for item in unique_words:
    dict_words.setdefault(len(item), []).append(item)
# make a dictionary word length : frequency
dict_freqs = {}
for key in sorted(dict_words.keys()):
    dict_freqs[key] = len(dict_words[key])/len_all


# plot 
plt.figure(figsize=(10,8));
plt.bar(dict_freqs.keys(), dict_freqs.values(), width = 1, edgecolor = "black");
plt.tight_layout();
plt.xticks(list(i for i in range(1, len(dict_freqs)+1)));
plt.xlabel("Word length");
plt.ylabel("Frequency");
plt.show;

# Task 6

def brick_translator(text):
    translated = re.sub(r'([ауоыиэяюёеАУОЫИЭЯЮЁЕ])', r'\1к\1', text)
    return translated

brick_translator("Синхрофазатрон")

# Task 7

def find_sent(text):
    sentences = []
    sentence_pattern = r"([A-ZА-Я][^\.!?]*)"
    sentences.extend(re.findall(sentence_pattern, text))
    return sentences
def find_n_words_sentences(text, n):
    sentences = find_sent(text=text)
    matched_sent = []
    for sentence in sentences:
        words = (re.findall(r"[a-zA-ZА-Яа-я\'\-]+", sentence))
        if len(words) == n:
            matched_sent.append(tuple(words))
    return matched_sent

