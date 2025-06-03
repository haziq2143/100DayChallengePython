# lelang



selesai = False

data = {}
while selesai != True:
    
    nama = input("Siapa Nama Anda? ")
    tawaran = int(input("Berapa tawaran anda? "))
    cek = input("Ada lagi yang nawar? ").lower()
    data[nama] = tawaran
    if cek == "tidak":
        selesai = True
terbesar = 0
nama = ""
for i in data:
    if data[i] > terbesar:
        nama = i
        terbesar = data[i]
        
print(f"pemenang: {nama} : {terbesar}")
  
   