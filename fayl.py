#Menda qanaqadir muommo tufaylimi bitta misol ko'rinmadi. Bu yonimdagilarda fayllarga oid masala ekan shu sabab men ham ixtiyoriy faylga oid misol yechdim.
file = open("sonlar.txt","r")
sonlar = file.read()
sonlar = sonlar.split()
lst = []
sonlar = list(map(int,sonlar))


def max_son(sonlar):
    max_son = sonlar[0]
    for i in sonlar:
        if i > max_son:
            max_son = i
    return max_son
def juftlarining_toqlariga_ayirmasi(sonlar):
    juftlar_sum = 0
    toqlari_sum = 0
    for i in sonlar:
        if i % 2 == 0:
            juftlar_sum += i
        else:
            toqlari_sum += i
    return juftlar_sum - toqlari_sum

print(juftlarining_toqlariga_ayirmasi(sonlar))