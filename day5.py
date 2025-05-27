# Loop

student_scores = [90, 80, 83, 200, 63, 100, 28, 75, 95, 67, 89, 94, 105]

# total = sum(student_scores)
# print(total)

# manual
# total = 0
# for score in student_scores:
#     total += score

# print(total)
# maximal = max(student_scores)

# manual
# maximal = 0
# for i in student_scores:
#     if i > maximal:
#         maximal = i
    
# print(maximal)
# num = 0
# for number in range(1, 101):
#     num += number
# print(num)

# import random
# huruf = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y', 'z',
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#     'U', 'V', 'W', 'X', 'Y',
# ]

# angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# simbol = [
#     '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#     '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
#     ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
# ]


# print("Random Password Generator")

# h = int(input("Masukkan jumlah huruf: "))
# a = int(input("Masukkan jumlah angka: "))
# s = int(input("Masukkan jumlah simbol: "))

# arr = []
# password = ''
# maximum = max(h,a,s)

# for i in range(0, h):
#     arr.append(random.choice(huruf))
 
# for x in range(0, a):
#     arr.append(random.choice(angka))
    
# for y in range(0, s):
#     arr.append(random.choice(simbol))
   
# random.shuffle(arr)

# for i in arr:
#     password += i
# print(f"Password anda adalah: {password}")


# Gacha
import random
karakter_acak = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]


print("Lucky Draw Konser")

vip = int(input('Masukkan Jumlah VIP: '))
reg = int(input('Masukkan Jumlah Regular: '))
giv = int(input('Masukkan Jumlah Giveaway: '))

peserta = []

for i in range(0, vip):
    
    pesert = 'VIP'
    peser = random.sample(karakter_acak, 4)
    for x in peser:
        pesert += x
    peserta.append(pesert)

for x in range(0, reg):
    
    pesert = 'REG'
    peser = random.sample(karakter_acak, 4)
    for y in peser:
        pesert += y
    peserta.append(pesert)


for y in range(0, giv):
    
    pesert = 'GIV'
    peser = random.sample(karakter_acak, 4)
    for z in peser:
        pesert += z
    peserta.append(pesert)

pemenang = peserta[random.randint(0, len(peserta) - 1)]
print(f"Pemenangnya adalah: {pemenang}")