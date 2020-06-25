import re
import string
frequency = {}  #empty dictionary
file_object = open("real_love.txt","r") #enables the program open &  read love
text_string = file_object.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string) #enables program to read  words called in  line 6
print(text_string)
def remove_stopwords(review_words):
    with open('Stop_words.txt') as stopfile:
        stopwords = stopfile.read()
    list = stopwords.split()
    print(list)
    with open('a.txt') as workfile:
        read_data = workfile.read()
        data = read_data.split()
        print(data)
        for word1 in list:
            for word2 in data:
                if word1 == word2:
                    return data.remove(list)
                    print(remove_stopwords)
for word in match_pattern:
    count = frequency.get(word, 0)  #word is key, value = 0
    frequency[word] = count + 1
frequency_list = frequency.keys()
for words in frequency_list:
    print(words,frequency[words])