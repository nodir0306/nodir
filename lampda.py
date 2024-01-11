def takrorlanishlar(lst,words):
    dct = {}
    for word in lst:
        count_word = words.count(word)
        dct[word] = count_word
    return dct
words = "When I was One I had ust begun When I was Two I was nearly new"
lst = ["I", "was","three","nar"]
print(takrorlanishlar(lst,words))
