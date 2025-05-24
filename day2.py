# print("Welcome to the tip calculator!")
# bill = float(input("Berapa jumlah total Bill kamu? "))
# tip = int(input('Mau kasih tip berapa persen? 10, 12, or 15? '))
# split = int(input("Mau split bill berapa?"))

# totalTip = (tip / 100) * bill
# totalBill = bill + totalTip
# totalPerPerson = totalBill / split
# print(round(totalPerPerson, 2))




# print("Total yang harus dibayarkan:", totalPerorang)


tagihan = float(input("Masukkan Tagihan: "))
diskon = int(input("Masukkan Diskon: "))

totalDiskon = (diskon / 100) * tagihan
total = tagihan - totalDiskon

orang = int(input("Masukkan jumlah orang: "))
totalPorsi = 0
coba = []
i = 0
while i < orang:
    nama = input("Masukkan Nama: ")
    porsi = int(input("Masukkan Porsi: "))

    
    totalPorsi += porsi
    i += 1
    print(totalPorsi)
    coba.append({'nama': nama, 'porsi' : porsi})

x = 0
while x < len(coba):
    print(f"{coba[x]['nama']}: {(coba[x]['porsi'] / totalPorsi) * total }")  
    x += 1



