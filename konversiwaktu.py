
# soal 1
# return function 1 argumen, input bilangan integer, output string dengan format waktu

# output string format waktu ("HH: MM: SS")

# output:
# HH: Hours, 2 digits, range: 00 - 99
# MM: Minutes, 2 digits, range: 00 - 59
# SS: seconds, 2 digits, range: 00 - 59

program = '** Konversi Waktu **'

def konversi(s):
    detik_jam = 3600
    detik_menit = 60
    jam = s // detik_jam
    sisa_jam = s % detik_jam
    menit = sisa_jam // detik_menit
    detik = sisa_jam % detik_menit
    return (f'HH: {jam} hours \nMM: {menit} minutes \nSS: {detik} seconds')
    
def konfirmasi():
    loop = True
    while loop:
        konfirm = input("Apakah ingin melakukan perhitungan ulang [Y|N]? ").lower()
        if konfirm == 'y':
            loop = False
            cek = True
        elif konfirm == 'n':
            
            loop = False
            cek = False
        else:            
            print("Input yang Anda masukkan salah")
            loop = True
            cek = False

    return cek

awal = True
while awal:
    print('=' * len(program))
    print(program)
    print('=' * len(program))
    print()
    
    try:
        x = int(input("Masukkan waktu (detik): "))
        if 0 < x <= 359999:
            print(konversi(x))
            print()
            if konfirmasi():
                awal = True
            else:
                print("** Perhitungan Selesai **")
                awal = False
        else:
            print('Invalid input')
            awal = True
    except:
        print("Invalid input")
        awal = True



