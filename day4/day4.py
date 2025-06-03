import random
import day4.bentuk as bentuk
# randomInt = random.randint(1,10)
# print(randomInt)

# random_0_to_1 = random.random() * 10
# print(random_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# if randomInt <= 5:
#     print("Heads")
# else:
#     print("Tails")

# state_of_america = ["Delware", "Pennsylvania"]
# print(state_of_america[0])



# people = ["Haziq", "Dian", "Andika", "Arif", "Vicky"]

# gacha = random.randint(0, len(people))
# print(people[gacha])

# cara simple
# print(random.choice(people))

# Batu Gunting Kertas

pilihan = int(input("Masukkan Pilihan (1. Batu, 2. gunting, 3. kertas): "))
komputer = random.randint(1,3)

if pilihan == 1:
    print("Pilihan: Batu")
    print(bentuk.batu)
elif pilihan == 2:
    print("Pilihan: Gunting")
    print(bentuk.gunting)
elif pilihan == 3:
    print("Pilihan: Kertas")
    print(bentuk.kertas)
else: 
    print("Invalid")
    
if pilihan != 1 and pilihan != 2 and pilihan != 3:
    print("Invalid")
elif komputer == 1:
    print("Pilihan: Batu")
    print(bentuk.batu)
elif komputer == 2:
    print("Pilihan: Gunting")
    print(bentuk.gunting)
elif komputer == 3:
    print("Pilihan: Kertas")
    print(bentuk.kertas)

if  pilihan != 1 and pilihan != 2 and pilihan != 3:
    print()
elif pilihan == komputer:
    print("Hasil: Seri")
elif pilihan == 1 and komputer == 2:
    print("Hasil: User Menang")
elif pilihan == 2 and komputer == 3:
    print("Hasil: User Menang")
elif pilihan == 3 and komputer == 1:
    print("Hasil: User Menang")
else:
    print("Komputer Menang")