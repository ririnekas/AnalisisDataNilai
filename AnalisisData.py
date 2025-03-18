import pandas as pd 
import matplotlib.pyplot as plt
url = "C:\Rin1\Datanil.xlsx"
df=pd.read_excel(url) #Menampilkan semua data excel
while True:  
    print("1. Load data excel")
    print("2. Load data dengan pilihan kolom tertentu (No, Nama, Alamat, 1 Mapel)")
    print("3. Menginformasikan  data nilai (Rata-rata per map1l, Max, Min")
    print("4. Menginformasikan Rata – rata nilai per siswa dan memberikan status kelulusan")
    print("5. Memberikan grade nilai maple tertentu (Sangat Kurang, Kurang, Cukup, Baik, Sangat Baik) salah satu mapel.")
    print("6. Merangking dari mapel yang sudah diberi gradenya ( 1 mapel di point 5)")
    print("7. Membuat Grafik Batang untuk memvisualkan data nilai rata-rata mapel.")
    print("8. Membuat Sebaran Nilai (Histogram) untuk memvisualkan data nilai salah satu mapel")
    print("9. Selesai") 
    mapel= int(input("Pilih salah 1-9:"))
    if(mapel==1):
        print(df)
    elif(mapel==2):
        df1=df[["No","Nama","Alamat","Informatika"]] #Menampilkan kolom terterntu
        print(df1)
    elif(mapel==3):
        print("Nilai rata-rata setiap mapel") 
        print("----------------------------")
        rata=df[["MAT","Bhs Ing","Bhs Ind","Informatika"]].mean() #Menampilkan rata-rata
        print(rata)
        print("Nilai maksimal setiap mapel")
        print("----------------------------")
        mak=df[["MAT","Bhs Ing","Bhs Ind","Informatika"]].max() #Menampilkan nilai maksimal
        print(mak)
        print("Nilai minimal setiap mapel")
        print("----------------------------")
        min=df[["MAT","Bhs Ing","Bhs Ind","Informatika"]].min() #Menampilkan nilai minimal
        print(min)
    elif(mapel==4):
        df["Rata"]=df[["MAT","Bhs Ing","Bhs Ind","Informatika"]].mean(axis=1) #Menampilkan rata-rata semua orang
        hasil_rata=df[["No","Nama","MAT","Bhs Ing","Bhs Ind","Informatika","Rata"]].round(2)
        def cek_status(Rata):
            if(Rata>=70):
                return("Lulus")
            else:
                return("Tidak Lulus")
        hasil_rata["Status"]=hasil_rata["Rata"].apply(cek_status) #Menampilkan status Lulus atau Tidak Lulus
        print(hasil_rata)
    elif(mapel==5):
        def cek_grade(nilai):
            if nilai >= 85:
                return "Sangat Baik"
            elif nilai >= 75:
                return "Baik"
            elif nilai >= 65:
                return "Cukup"
            elif nilai >= 51:
                return "Kurang"
            else:
                return "Sangat Kurang"
        df['Grade MAT'] = df['MAT'].apply(cek_grade)
        MAT = df[['No', 'Nama', 'MAT', 'Grade MAT']]
        print(MAT)

    elif(mapel==6):
        def cek_grade(nilai):
            if nilai >= 85:
                return "Sangat Baik"
            elif nilai >= 75:
                return "Baik"
            elif nilai >= 65:
                return "Cukup"
            elif nilai >= 51:
                return "Kurang"
            else:
                return "Sangat Kurang"
        df['Grade MAT'] = df['MAT'].apply(cek_grade)
        df_sort=df.sort_values(["MAT"],ascending=False) # MAT tertinggi
        print(df_sort[["No", "Nama", "Alamat", "MAT", 'Grade MAT']])
    elif(mapel==7):
        def cek_grade(nilai):
            if nilai >= 85:
                return "Sangat Baik"
            elif nilai >= 75:
                return "Baik"
            elif nilai >= 65:
                return "Cukup"
            elif nilai >= 51:
                return "Kurang"
            else:
                return "Sangat Kurang"
        df['Grade MAT'] = df['MAT'].apply(cek_grade)
        ket_met = df[['No', 'Nama', 'MAT', 'Grade MAT']].round(2)
        jum_ket=ket_met.groupby(["Grade MAT"])["Grade MAT"].count()
        print(jum_ket)

        jum_ket.plot(kind="bar", color="skyblue", title="Kategori Nilai MAT")
        plt.xlabel("kategori")
        plt.ylabel("Jumlah")
        plt.show()
    elif(mapel==8):
        histogram=df[["Informatika"]]
        plt.hist(df["Informatika"], bins=10, color="orange", edgecolor="orange")
        plt.title("Kategori Nilai Informatika")
        plt.xlabel("Nilai Informatika")
        plt.ylabel("Jumlah")
        plt.show()
    elif(mapel==9):
        print("Selesai")
        break
    else:
        print("Nomor tidak ditemukan pilih salah 1-8:")