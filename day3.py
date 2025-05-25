# day 3
# Angka ganjil or genap
# angka = int(input("Masukkan angka: "))

# if angka % 2 == 0:
#     print("Angka ini genap")
# else:
#     print("Angka ini ganjil")

# Pizza
# print("Selamat Datang Di Toko Pizza")
# size = input("Masukkan Size yang anda mau (S, M, L): ").upper()
# papperoni = input("Apakah mau pakai papperoni? (Y, N): ").upper()
# extraKeju = input("Apakah mau extra keju? (Y, N): ").upper()
# total = 0
# if size == "S":
#     total += 15
#     if papperoni == "Y":
#         total += 2
#         if extraKeju == "Y":
#             total += 1
#     if extraKeju == "Y":
#         total += 1
#     print(f"Total Tagihan: ${total}")
# elif size == "M":
#     total += 20
#     if papperoni == "Y":
#         total += 3
#         if extraKeju == "Y":
#             total += 1
#     if extraKeju == "Y":
#         total += 1
#     print(f"Total Tagihan: ${total}")
# elif size == "L":
#     total += 25
#     if papperoni == "Y":
#         total += 3
#         if extraKeju == "Y":
#             total += 1
#     if extraKeju == "Y":
#         total += 1
#     print(f"Total Tagihan: ${total}")
# else:
#     print('Invalid')

# treasure hunter

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______//____
''')

print("Welcome to treasure island. Your mission is to find the treasure")

print('''You are a brave adventurer who just landed on the mysterious island.
The sun is setting, and two paths stretch before you.\n''')

print('''One leads **left**, into a dark forest.  
The other leads **right**, toward the cliffs where the waves crash loudly...\n''')

print("Which way will you go?")

quest1 = input("left or right? \n").upper()

if quest1 == "LEFT":
    print("You follow the path into the forest. It's quiet... too quiet.\nAfter a long walk, you reach a wide, deep lake.\nIn the middle of the lake, you see a glowing temple – maybe that's where the treasure is hidden!")
    
    print("You can try to **swim** across... \nOr wait and see if something – or someone – can help.")
    quest2 = input("Swim or wait? \n").upper()
    if quest2 == "WAIT":

        print("You sit by the lake, waiting.\nThe wind grows colder... and then, out of the mist, a small boat appears.\nNo one is steering it – but it stops right in front of you.")
        print("You get in. The boat silently takes you to the other side.")
        print("You enter the ancient temple and find three doors:\nOne **Red**, one **Yellow**, and one **Blue**.")
        print("Each door holds a different fate.\nChoose wisely...")
        
        quest3 = input("Which door? (Red/ Yellow/ Blue): \n").upper()
        
        if quest3 == "YELLOW":
            print('You Win')
        elif quest3 == "RED":
            print('Burned by fire. Game Over!!!')
        elif quest3 == 'BLUE':
            print("Eaten By Beats. Game Over!!!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game Over")