PI = 3.14159265358979

def input_positif(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai <= 0:
                print("Input tidak valid: Angka harus lebih dari 0")
            else:
                return nilai
        except ValueError:
            print("Input tidak valid: Harus berupa angka!")

def tampilkan_menu_utama():
    print("\n" + "="*40)
    print("   KALKULATOR MATEMATIKA TERPADU")
    print("="*40)
    print("1. Kalkulator Angka")
    print("2. Kalkulator Luas Bangun Datar")
    print("3. Kalkulator Volume Bangun Ruang")
    print("4. Keluar")
    print("="*40)

def kalkulator_angka():
    while True:
        print("\n--- KALKULATOR ANGKA ---")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Pangkat (^)")
        print("0. Balik ke Menu Utama")

        pilihan = input("\nPilih operasi: ")

        if pilihan == "0":
            break

        if pilihan not in ["1", "2", "3", "4", "5"]:
            print("Pilihan lu gavalid KONCETT.")
            continue

        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == "1":
            hasil = a + b
            print(f"Hasil: {a} + {b} = {hasil}")
        elif pilihan == "2":
            hasil = a - b
            print(f"Hasil: {a} - {b} = {hasil}")
        elif pilihan == "3":
            hasil = a * b
            print(f"Hasil: {a} x {b} = {hasil}")
        elif pilihan == "4":
            if b == 0:
                print("Error: gabisa dibagi sama 0 KONCETT!")
            else:
                hasil = a / b
                print(f"Hasil: {a} / {b} = {hasil}")
        elif pilihan == "5":
            hasil = a ** b
            print(f"Hasil: {a} ^ {b} = {hasil}")

def kalkulator_luas():
    while True:
        print("\n--- KALKULATOR LUAS BANGUN DATAR ---")
        print("1. Persegi")
        print("2. Segitiga")
        print("3. Lingkaran")
        print("4. Persegi Panjang")
        print("5. Trapesium")
        print("0. Balik ke Menu Utama")

        pilihan = input("\nPilih bangun datar: ")

        if pilihan == "0":
            break

        if pilihan == "1":
            sisi = input_positif("Masukkan panjang sisi: ")
            luas = sisi ** 2
            print(f"Luas Persegi = {sisi}² = {luas}")

        elif pilihan == "2":
            alas = input_positif("Masukkan alas: ")
            tinggi = input_positif("Masukkan tinggi: ")
            luas = 0.5 * alas * tinggi
            print(f"Luas Segitiga = ½ x {alas} x {tinggi} = {luas}")

        elif pilihan == "3":
            jari = input_positif("Masukkan jari-jari: ")
            luas = PI * jari ** 2
            print(f"Luas Lingkaran = π x {jari}² = {luas:.4f}")

        elif pilihan == "4":
            panjang = input_positif("Masukkan panjang: ")
            lebar = input_positif("Masukkan lebar: ")
            luas = panjang * lebar
            print(f"Luas Persegi Panjang = {panjang} x {lebar} = {luas}")

        elif pilihan == "5":
            a = input_positif("Masukkan sisi sejajar pertama (a): ")
            b = input_positif("Masukkan sisi sejajar kedua (b): ")
            tinggi = input_positif("Masukkan tinggi: ")
            luas = 0.5 * (a + b) * tinggi
            print(f"Luas Trapesium = ½ x ({a} + {b}) x {tinggi} = {luas}")

        else:
            print("Pilihanlu gavalid KONCETT.")

def kalkulator_volume():
    while True:
        print("\n--- KALKULATOR VOLUME BANGUN RUANG ---")
        print("1. Tabung")
        print("2. Kubus")
        print("3. Balok")
        print("4. Bola")
        print("5. Prisma Segitiga")
        print("6. Prisma Segi Empat")
        print("0. Kembali ke Menu Utama")

        pilihan = input("\nPilih bangun ruang: ")

        if pilihan == "0":
            break

        if pilihan == "1":
            jari = input_positif("Masukkan jari-jari: ")
            tinggi = input_positif("Masukkan tinggi: ")
            volume = PI * jari ** 2 * tinggi
            print(f"Volume Tabung = π x {jari}² x {tinggi} = {volume:.4f}")

        elif pilihan == "2":
            sisi = input_positif("Masukkan panjang sisi: ")
            volume = sisi ** 3
            print(f"Volume Kubus = {sisi}³ = {volume}")

        elif pilihan == "3":
            panjang = input_positif("Masukkan panjang: ")
            lebar = input_positif("Masukkan lebar: ")
            tinggi = input_positif("Masukkan tinggi: ")
            volume = panjang * lebar * tinggi
            print(f"Volume Balok = {panjang} x {lebar} x {tinggi} = {volume}")

        elif pilihan == "4":
            jari = input_positif("Masukkan jari-jari: ")
            volume = (4/3) * PI * jari ** 3
            print(f"Volume Bola = (4/3) x π x {jari}³ = {volume:.4f}")

        elif pilihan == "5":
            alas = input_positif("Masukkan alas segitiga: ")
            tinggi_segi = input_positif("Masukkan tinggi segitiga: ")
            tinggi_prisma = input_positif("Masukkan tinggi prisma: ")
            luas_alas = 0.5 * alas * tinggi_segi
            volume = luas_alas * tinggi_prisma
            print(f"Volume Prisma Segitiga = (½ x {alas} x {tinggi_segi}) x {tinggi_prisma} = {volume}")

        elif pilihan == "6":
            panjang = input_positif("Masukkan panjang alas: ")
            lebar = input_positif("Masukkan lebar alas: ")
            tinggi = input_positif("Masukkan tinggi prisma: ")
            volume = panjang * lebar * tinggi
            print(f"Volume Prisma Segi Empat = {panjang} x {lebar} x {tinggi} = {volume}")

        else:
            print("Pilihan tidak valid! Coba lagi.")

def main():
    print("\nSelamat datang di Kalkulator Matematika Terpadu!")

    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            kalkulator_angka()
        elif pilihan == "2":
            kalkulator_luas()
        elif pilihan == "3":
            kalkulator_volume()
        elif pilihan == "4":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1-4.")

main()