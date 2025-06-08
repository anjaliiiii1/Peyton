def freq_count(words):
    freq = {}

    for word in  words:
        if  word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

word_list = input("Enter a list of words : ")
word = word_list.split()
result = freq_count(word)
print(result)
