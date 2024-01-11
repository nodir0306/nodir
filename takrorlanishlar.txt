def takrorlanishlar(lst,words):
    dct = {}
    words = words.split(" ")
    for i in range(len(lst)):
        count = 0
        for j in range(len(words)):
            if lst[i] == words[j]:
                count += 1
        dct[lst[i]] = count
    return dct

#check

words = "When I was One I had ust begun When I was Two I was nearly new"
lst = ["I", "was","three","near"]
print(takrorlanishlar(lst,words))