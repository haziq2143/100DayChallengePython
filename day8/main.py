# def greet() :
#     print("Hello")
#     print("Good Night")
#     print("Sleep Well")

# greet()

# def greetWithName(name):
#     print(f"Hello {name}")
#     print(f"Good Night, {name}")
#     print(f"Sleep Well, {name}")

# greetWithName("Haziq")

# function with more than 1 input
# def greet_with(name, location):
#     print(f"Hai {name} yang ada di {location}")

# greet_with('hazoq', 'perumnas')
# greet_with(location="Perumnas", name="Haziq")

# projek
import random
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

# print(huruf.)
def encrypt(kata, jumlah):
    i = 0
    kataEnc = []
    while i < len(kata):
        if kata[i] in huruf:
            kataEnc.append(huruf[(huruf.index(kata[i]) + jumlah) % len(huruf)])
        else:
            kataEnc.append(kata[i])
        i += 1

    hasil = ''
    for i in kataEnc:
        hasil += i
    print(hasil)

def decrypt(kata, jumlah):
    i = 0
    kataDec = []
    while i < len(kata):
        if kata[i] in huruf:
            kataDec.append(huruf[huruf.index(kata[i]) - jumlah])
        else:
            kataDec.append(kata[i])
        i += 1
    hasil = ''
    for i in kataDec:
        hasil += i
    print(hasil)



selesai = False



while selesai != True:
    menu = int(input("1. Encrypt\n2. Decrypt\nPilih menu: "))

    if menu == 1:

        kata = input("Masukkan Kata: ").lower()
        encryp = int(input("Masukkan encrypt: "))
        encrypt(kata, encryp)
    elif menu == 2:
        kata = input("Masukkan Kata: ").lower()
        decryp = int(input("Masukkan decrypt: "))
        decrypt(kata, decryp)
    else:
        print("Pilihan invalid")