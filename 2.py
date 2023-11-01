import tkinter as tk
from tkinter import ttk

# Fungsi untuk mengenkripsi teks dengan metode Caesar Cipher
def encrypt_text():
    plaintext = plaintext_Text.get("1.0", "end-1c")
    shift_str = shift_entry.get()

    try:
        shift = int(shift_str)
        if shift < 1 or shift > 25:
            raise ValueError("Shift harus berada dalam rentang 1-25")

        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                else:
                    shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                ciphertext += shifted
            else:
                ciphertext += char
        ciphertext_text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan yang baru
        ciphertext_text.insert("1.0", ciphertext)

    except ValueError as e:
        # Tangani pengecualian jika shift di luar rentang
        ciphertext_text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan pesan kesalahan
        ciphertext_text.insert("1.0", "Error: " + str(e))

# Fungsi untuk mendeskripsi teks yang telah dienkripsi dengan metode Caesar Cipher
def decrypt_text():
    ciphertext = ciphertext_Text.get("1.0", "end-1c")
    shift_str = shift_entry2.get()

    try:
        shift = int(shift_str)
        if shift < 1 or shift > 25:
            raise ValueError("Shift harus berada dalam rentang 1-25")

        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    shifted = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                else:
                    shifted = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                plaintext += shifted
            else:
                plaintext += char
        plaintext_text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan yang baru
        plaintext_text.insert("1.0", plaintext)

    except ValueError as e:
        # Tangani pengecualian jika shift di luar rentang
        plaintext_text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan pesan kesalahan
        plaintext_text.insert("1.0", "Error: " + str(e))

# Fungsi untuk mengenkripsi teks dengan metode Reverse
def reverse_text():
    plaintext = reverse_plaintext_Text.get("1.0" , "end-1c")
    reversed_text = plaintext[::-1]
    reverse_ciphertext_Text.delete("1.0", "end")
    reverse_ciphertext_Text.insert("1.0", reversed_text)

# Fungsi untuk mendeskripsi teks yang telah dienkripsi dengan metode Reverse
def decrypt_reverse_text():
    reversed_text = reverse_ciphertext2_Text.get("1.0" , "end-1c")
    plaintext = reversed_text[::-1]
    reverse_plaintext2_Text.delete("1.0", "end")
    reverse_plaintext2_Text.insert("1.0", plaintext)

#vigenere bos
def vigenere_encrypt():
    plaintext = vigenere_plaintext_Text.get("1.0", "end-1c")
    keyword = vigenere_keyword_entry.get()
    #except bos
    if not keyword.isalpha():
        vigenere_ciphertext_Text.delete("1.0", "end")
        vigenere_ciphertext_Text.insert("1.0", "Error: Keyword harus berisi huruf alphabet")
        return

    ciphertext = ""
    keyword_len = len(keyword)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + ord(keyword[i % keyword_len]) - ord('a')) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + ord(keyword[i % keyword_len]) - ord('a')) % 26) + ord('A'))
            ciphertext += shifted
        else:
            ciphertext += char
    vigenere_ciphertext_Text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan yang baru
    vigenere_ciphertext_Text.insert("1.0", ciphertext)
def vigenere_decrypt():
    ciphertext = vigenere_ciphertext2_Text.get("1.0", "end-1c")
    keyword = vigenere_keyword_entry.get()
    #except ges
    if not keyword.isalpha():
        vigenere_plaintext2_Text.delete("1.0", "end")
        vigenere_plaintext2_Text.insert("1.0", "Error: Keyword harus berisi huruf alphabet")
        return

    plaintext = ""
    keyword_len = len(keyword)
    for i,char in enumerate(ciphertext):
        if char.isalpha():
            if char.islower():
                shifted = chr(((ord(char) - ord('a') - (ord(keyword[i % keyword_len]) - ord('a'))) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') - (ord(keyword[i % keyword_len]) - ord('a'))) % 26) + ord('A'))
            plaintext += shifted
        else:
            plaintext += char
    vigenere_plaintext2_Text.delete("1.0", "end")  # Menghapus teks sebelum menambahkan yang baru
    vigenere_plaintext2_Text.insert("1.0", plaintext)

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Kriptografi Chiper -by_kuesell sell")



# Membuat tabbed interface
tab_control = ttk.Notebook(app)

# Tab untuk Caesar Cipher
caesar_tab = ttk.Frame(tab_control)
tab_control.add(caesar_tab, text="Caesar Cipher")
tab_control.pack(expand=1, fill="both")


# Label dan input teks untuk Caesar Cipher
plaintext_label = tk.Label(caesar_tab, text="Teks:")
plaintext_label.pack()
plaintext_Text = tk.Text(caesar_tab, width=60 , height = 5)
plaintext_Text.pack()

# Label untuk input pergeseran
shift_label = tk.Label(caesar_tab, text="Pergeseran (1-25):")
shift_label.pack()
shift_entry = tk.Entry(caesar_tab)
shift_entry.pack()

# Tombol untuk mengenkripsi (Caesar Cipher)
encrypt_button = tk.Button(caesar_tab, text="Enkripsi", command=encrypt_text)
encrypt_button.pack()



# Label untuk teks terenkripsi (Caesar Cipher)
ciphertext_text = tk.Text(caesar_tab, width=60, height=5)
ciphertext_text.pack()
#spasi
separator_label = tk.Label(caesar_tab, text="===================================")
separator_label.pack()

# Label untuk input teks terenkripsi
ciphertext_label2 = tk.Label(caesar_tab, text="Teks Terenkripsi:")
ciphertext_label2.pack()

# Input teks terenkripsi
ciphertext_Text = tk.Text(caesar_tab , width = 60 , height = 5)
ciphertext_Text.pack()

# Label untuk input pergeseran
shift_label = tk.Label(caesar_tab, text="Pergeseran (1-25):")
shift_label.pack()
shift_entry2 = tk.Entry(caesar_tab)
shift_entry2.pack()

# Tombol untuk mendeskripsi (Caesar Cipher)
decrypt_button = tk.Button(caesar_tab, text="Deskripsi", command=decrypt_text)
decrypt_button.pack()

#hasil
plaintext_text = tk.Text(caesar_tab, width=60, height=5)
plaintext_text.pack()

# Tab untuk Reverse
reverse_tab = ttk.Frame(tab_control)
tab_control.add(reverse_tab, text="Reverse")
tab_control.pack(expand=1, fill="both")

# Label dan input teks untuk Reverse
reverse_plaintext_label = tk.Label(reverse_tab, text="Teks:")
reverse_plaintext_label.pack()

reverse_plaintext_Text = tk.Text(reverse_tab,width=60, height=5)
reverse_plaintext_Text.pack()

# Tombol untuk mengenkripsi (Reverse)
encrypt_reverse_button = tk.Button(reverse_tab, text="Enkripsi", command=reverse_text)
encrypt_reverse_button.pack()

#spasi
separator_label = tk.Label(reverse_tab, text="Hasil :")
separator_label.pack()

# Label untuk teks terenkripsi (Reverse)
reverse_ciphertext_Text = tk.Text(reverse_tab,width=60, height=5 )
reverse_ciphertext_Text.pack()

#spasi
separator_label = tk.Label(reverse_tab, text="===================================")
separator_label.pack()


# Label untuk input teks terenkripsi (Reverse)
reverse_ciphertext_label2 = tk.Label(reverse_tab, text="Teks Terenkripsi:")
reverse_ciphertext_label2.pack()

# Input teks terenkripsi
reverse_ciphertext2_Text = tk.Text(reverse_tab,width=60, height=5)
reverse_ciphertext2_Text.pack()

# Tombol untuk mendeskripsi (Reverse)
decrypt_reverse_button = tk.Button(reverse_tab, text="Deskripsi", command=decrypt_reverse_text)
decrypt_reverse_button.pack()

#spasi
separator_label = tk.Label(reverse_tab, text="Hasil :")
separator_label.pack()

# Label untuk teks terenkripsi (Reverse)
reverse_plaintext2_Text = tk.Text(reverse_tab,width=60, height=5)
reverse_plaintext2_Text.pack()

# Tab untuk Vigenere Cipher
vigenere_tab = ttk.Frame(tab_control)
tab_control.add(vigenere_tab, text="Vigenere Cipher")
tab_control.pack(expand=1, fill="both")

# Label dan input teks untuk Vigenere Cipher
vigenere_plaintext_label = tk.Label(vigenere_tab, text="Teks:")
vigenere_plaintext_label.pack()
vigenere_plaintext_Text = tk.Text(vigenere_tab, width = 60 , height =5)
vigenere_plaintext_Text.pack()

# Label dan input kata kunci untuk Vigenere Cipher
vigenere_keyword_label = tk.Label(vigenere_tab, text="Kata Kunci (Vigenere):")
vigenere_keyword_label.pack()
vigenere_keyword_entry = tk.Entry(vigenere_tab, width = 75)
vigenere_keyword_entry.pack()

# Tombol untuk mengenkripsi (Vigenere Cipher)
vigenere_encrypt_button = tk.Button(vigenere_tab, text="Enkripsi", command=vigenere_encrypt)
vigenere_encrypt_button.pack()

# Label untuk teks terenkripsi (Vigenere Cipher)
vigenere_ciphertext_Text = tk.Text(vigenere_tab, width=60, height=5)
vigenere_ciphertext_Text.pack()
#spasi
separator_label = tk.Label(vigenere_tab, text="===================================")
separator_label.pack()
# Label untuk input teks terenkripsi
vigenere_ciphertext_label2 = tk.Label(vigenere_tab, text="Teks Terenkripsi:")
vigenere_ciphertext_label2.pack()

# Input teks terenkripsi
vigenere_ciphertext2_Text = tk.Text(vigenere_tab,width=60, height=5)
vigenere_ciphertext2_Text.pack()

# Label dan input kata kunci untuk Vigenere Cipher
vigenere_keyword_label = tk.Label(vigenere_tab, text="Kata Kunci (Vigenere):")
vigenere_keyword_label.pack()
vigenere_keyword_entry2 = tk.Entry(vigenere_tab, width = 75)
vigenere_keyword_entry2.pack()

# Tombol untuk mendeskripsi (vigenere Cipher)
vignere_decrypt_button = tk.Button(vigenere_tab, text="Deskripsi", command=vigenere_decrypt)
vignere_decrypt_button.pack()

# Label untuk hasil dekripsinya
vigenere_plaintext2_Text = tk.Text(vigenere_tab,  width=60, height=5)
vigenere_plaintext2_Text.pack()

app.mainloop()
