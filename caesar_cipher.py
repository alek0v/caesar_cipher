

def encrypt(text, key):  # Функція шифрування (зсув вправо)
    out = ""
    for i in text:
        if i.isalpha():
            if i.isupper() and ord(i) + key > ord('Z'):  # Функції для зсуву вправо (якщо дійшли до кінця алфавіту - перехід на початок)
                i = chr(ord("A") + ((ord(i) + key) % ord('Z') - 1))
            elif i.islower() and ord(i) + key > ord('z'):
                i = chr(ord("a") + ((ord(i) + key) % ord('z') - 1))
            elif i.isalpha():
                i = chr(ord(i) + key)
        out += i
    return out

def decrypt(text, key):  # Функція дешифрування (зсув вліво)
    out = ""
    for i in text:
        if i.isalpha():
            if i.isupper() and ord(i) - key < ord('A'):  # Функції для зсуву вліво (якщо дійшли до початку алфавіту - перехід в кінець)
                i = chr(ord("Z") - (ord('A') - 1) % (ord(i) - key))
            elif i.islower() and ord(i) - key < ord('a'):
                i = chr(ord("z") - (ord('a') - 1) % (ord(i) - key))
            elif i.isalpha():
                i = chr(ord(i) - key)
        out += i
    return out


def ciph_k(q):  # Перевірка коректності вхідної відповіді
    while True:
        if q.upper() == "E":
            return q.upper()
        elif q.upper() == 'D':
            return q.upper()
        else:
            q = input("Invalid input data. Enter E - Encryption, D - Decryption: ")



def one_more(q):  # Перевірка коректності вхідної відповіді
    while True:
        if q.lower() == "y" or q.lower() == "yes":
            return True
        elif q.lower() == 'n' or q.lower() == 'no':
            return False
        else:
            q = input('Invalid input data. Enter y (yes) n (no): ')

c = True
while c == True:
    t = input("Enter your input text: ")
    a = ciph_k(input("Enter E - Encryption, D - Decryption (Caesar cipher): "))

    if a == 'E':
        for i in range(26):
            o = encrypt(t, i)
            print(f"ROT{i}: {o}")
            
    elif a == 'D':
        for i in range(26):
            o = decrypt(t, i)
            print(f"ROT{i}: {o}")

    c = one_more(input("\nDo another transformation? y (yes), n (no): "))
    
input("\nPress 'Enter' to close the program: ")