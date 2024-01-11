def vaqt(word):
    word = word.replace(" ",".").replace(":",".")
    word = word.split(".")
    result = ""
    k = ''
    for i in range(len(word)):
        k = word[i]
        if k[0] == "0":
            word[i] = k[1]
    match word[1]:
        case '1':
            result = word[0] + " January " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '2':
            result = word[0] + " February " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '3':
            result = word[0] + " March " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '4':
            result = word[0] + " April " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '5':
            result = word[0] + " May " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '6':
            result = word[0] + " Juny " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '7':
            result = word[0] + " July " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '8':
            result = word[0] + " Avgust " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '9':
            result = word[0] + " September " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '10':
            result = word[0] + " Oktember " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '11':
            result = word[0] + " November " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
        case '12':
            result = word[0] + " December " + word[2] + " year " + word[3] + " hours " + word[4] + " minute"
    return result

#Check

word = "11.12.2000 23:45"
print(vaqt(word))
