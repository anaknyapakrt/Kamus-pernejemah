import time

meme_dict = {
    "SYBAU": "kata digunakan untuk menyuruh seseorang diam",
    "CREEPY": "menakutkan, tidak menyenangkan",
    "BRB": "Memberitahu bahwa anda akan pergi sebentar",
    "XD": "Suatu teks yang menunjukkan emoji ketawa",
    "WHAT": "Bisa sebagai pemberi tahu bahwa anda terkejut atau bingung",
    "EWW": "Merasa jijik / tidak nyaman",
    "GAJE": "nggak jelas",
    "WKWK": "ketawa",
    "BRO": "saudara",
    "BUCIN": "budak cinta",
    "MANTUL": "mantap betul"
}

print("Halo! Selamat datang ke kamus kata-kata meme!")
time.sleep(1)
print("Anda dapat mencari hingga 5 kata dari kamus ini.")
time.sleep(1)
print("Ketik 'HELP' untuk melihat semua kata yang tersedia.\n")

for i in range(5):
    word = input("Ketik kata yang tidak kamu mengerti (gunakan huruf KAPITAL semua!): ").upper()

    if word == "HELP":
        print("\nKata-kata yang tersedia:")
        for key in meme_dict.keys():
            print("-", key)
        print()
    elif word in meme_dict:
        print("Makna kata", word, "adalah:", meme_dict[word])
        print()
    else:
        print("Kata tidak ditemukan...\n")

print("Terima kasih sudah menggunakan kamus meme!")
