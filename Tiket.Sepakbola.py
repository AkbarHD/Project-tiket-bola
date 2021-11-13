print("^^^^^^Selamat Datang Di Stadion Gelora Bung Karno^^^^^^^^^^")

print("===============================================================")
print("=================Pendaftaram Tiket E-Commercce=================")
print(" -_- Pertandingan pagi -_- ")
print(" 1. Arema VS Persebaya           07.00             Rp. 70.0000 ")
print(" 2. Persib VS Persija            08.30             Rp. 65.0000 ")
print(" 3. PSM VS Persiba               10.30             Rp. 50.0000 ")
print("-_- Pertandingan Sore -_- ")
print(" 4. Persipura VS PSS             15.00             Rp. 65.0000 ")
print(" 5. Borneo VS Persita            16.30             Rp. 45.0000 ")
print(" 6. Bacerlona VS Real Madrid     18.30             Rp. 100.0000")
print("===============================================================")

nama = input("masukan nama anda : ")
jadwal_pertandingan =int(input("silahkan pilih pertandingan pagi/sore dengan ketik 1 = pagi, 2 = sore : "))
if jadwal_pertandingan ==1:
    print(" 1. Arema VS Persebaya           07.00             Rp. 70.0000")
    print( "2. Persib VS Persija            08.30             Rp. 65.0000")
    print(" 3. PSM VS Persiba               10.30             Rp. 50.0000")
elif jadwal_pertandingan ==2:
    print(" 4. Persipura VS PSS             15.00             Rp. 65.0000")
    print(" 5. Borneo VS Persita            16.30             Rp. 45.0000")
    print(" 6. Bacerlona VS Real Madrid     18.30             Rp. 100.0000")
else:
    while True:
        print("==============tidak tersedia silahkan ketika ulang=======")
        jadwal_pertandingan = int(input("silahkan ketik kode yang ingin di tonton : "))
        if jadwal_pertandingan==1 or jadwal_pertandingan==2:
            if jadwal_pertandingan==1:
                print("Arema VS Persebaya           07.00             Rp. 70.0000")
                print("Persib VS Persija            08.30             Rp. 65.0000")
                print("PSM VS Persiba               10.30             Rp. 50.0000")
            elif jadwal_pertandingan==2:
                    print("Persipura VS PSS             15.00             Rp. 65.0000")
                    print("Borneo VS Persita            16.30             Rp. 45.0000")
                    print("Bacerlona VS Real Madrid     18.30             Rp. 100.0000")
            continue
Pertandingan = int(input("silahkan dengan memilih no kode :   "))
if Pertandingan==1:
    spec ="Arema VS Persebaya"
    Jam  ="07.30 "
    harga = 700000
elif Pertandingan==2:
    spec ="Persib VS Persija"
    jam ="08.30"
    harga = 650000
elif Pertandingan==3:
    spec ="PSM VS Persiba"
    jam ="10.30" 
    harga =50000
elif Pertandingan==4:
    spec ="Persipura VS PSS"
    jam ="15.00"
    harga =650000
elif Pertandingan==5:
    spec ="Borneo VS Persita"
    jam ="16.30"
    harga =450000
elif Pertandingan==6:
    spec ="Bercelona VS Real Madrid"
    jam ="18.30"
    harga =100000
else:
    while True:
        print("^^^^^^^^^^pilihan tidak tersedia silahkan^^^^^^^^^^^^^^^^^^^^^")
        Pertandingan =int(input("silahkan pilih pertandingan(dengan ketik no kode : "))
        if Pertandingan==1 or Pertandingan==2 or Pertandingan==3 or Pertandingan==4 or Pertandingan==5 or Pertandingan==6:
            if Pertandingan==1:
               spec ="Arema VS Persebaya"
               Jam  ="07.30 "
               harga = 700000 
            elif Pertandingan==2:
                 spec ="Persib VS Persija"
                 jam ="08.30"
                 harga = 650000
            elif Pertandingan==3:
                spec ="PSM VS Persiba"
                jam ="10.30" 
                harga =50000
            elif Pertandingan==3:
                spec ="PSM VS Persiba"
                jam ="10.30" 
                harga =50000
            elif Pertandingan==4:
                spec ="Persipura VS PSS"
                jam ="15.00"
                harga =650000
            elif Pertandingan==5:
                 spec ="Borneo VS Persita"
                 jam ="16.30"
                 harga =450000
            elif Pertandingan==6:
                 spec ="Bercelona VS Real Madrid"
                 jam ="18.30"
                 harga =100000
                 continue
total = int(input("Masukan jumlah pembelian tiket : "))
print("\nNota Pembelian Tiket")
print("```````````````````````")
print("Nama anda :  "+str(nama))
print("liga pertandingan : "+str(spec))
print("jam pertandingan : "+str(jam))
print("jumlah tiket : ",total)
print("harga : ",harga)
bayar = total * harga

print("anda harus membayar : {}".format(bayar))
ubay = int(input("masukan uang bayar anda : "))
kembali =(ubay-bayar)
print("uang kembali : ",kembali)
print('\nNote : Bonus Didalam Teater')
bonus = ['botol Air Minum','Pop Corn']
for i in range (len(bonus)):
    print("1",bonus[i])
print ("===================================================")
print ('******** Terima Kasih Dan Selamat Menonton ********')
print ("===================================================")







                


                


                



                







                




