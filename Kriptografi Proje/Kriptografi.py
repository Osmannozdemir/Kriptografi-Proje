import hashlib
import random

#dosya yazdırmak
def dosyaya_yazdirmak(isim, password, dosya_adi): 
    with open(dosya_adi, 'a') as f:
        f.write(isim + ' ')
        f.write(password + '\n')


def kullanici_adi_olusturmak():
    # BIL008-2020xxxx gibi kullanıcı oluştur 4x rastgeledir
    return f"BIL008-2020{''.join(str(random.randint(0, 9)) for _ in range(5))}"


# Passwords.txt'den isim ve şifre içeren bir demet listesi oluşturmak
passwords = [line.strip().split(' ') for line in open('Password.txt')]


# 3.1 ilk Görev
for i in range(len(passwords)):
  
    # Şifrenin bir karmasını oluşturmak.
    hash_object = hashlib.md5(passwords[i][1].encode())
    
    # hash'i yazdırmak
    dosyaya_yazdirmak(f"{kullanici_adi_olusturmak()}",
                  passwords[i][2], 'Veritaban1.txt')


# 3.2 İkinci Görev
for i in range(len(passwords)):
 
    # Şifrenin bir karmasını oluşturmak
    hash_object = hashlib.md5(passwords[i][1].encode())
 
    # hash'i yazdırmak
    dosyaya_yazdirmak(f"{kullanici_adi_olusturmak()}",
                  hash_object.hexdigest(), 'Veritaban2.txt')


# 3.3 Üçüncü Görev
Salt = "9ahd37dn4hd82jdlf753"
for i in range(len(passwords)):
 
    # Şifre ve tuzdan XOR yapmak
    xor_password = bytes(
        [ord(x) ^ ord(y) for x, y in zip(passwords[i][1], Salt)])

    # Şifrenin bir karmasını oluşturur
    hash_object = hashlib.sha512(xor_password)


    # Dosyaya yazdırmak
    with open("Veritaban3.txt", 'a') as f:
        f.write(kullanici_adi_olusturmak() + ' ')
        f.write(hash_object.hexdigest() + '\n')


# 3.4 Dördüncü Görev
for i in range(len(passwords)):
   
    # 20 basamaklı rastgele bir tuz oluşturur.
    salt = ''.join(str(random.randint(0, 9)) for _ in range(20))

    # Şifre ve tuzdan XOR yapma
    xor_password = bytes(
        [ord(x) ^ ord(y) for x, y in zip(passwords[i][1], salt)])
  
    # SHA3_224 ile bir hash yapma
    hash_object = hashlib.sha3_224(xor_password)

    # Dosyaya yazdırmak
    with open("Veritaban4.txt", 'a') as f:
        f.write(kullanici_adi_olusturmak() + ' ')
        f.write(hash_object.hexdigest() + ' ')
        f.write(salt + '\n')


# 3.5 Beşinci Görev
for i in range(len(passwords)):
    
    # 20 basamaklı 20 rastgele tuz oluştur
    salt = []
    for _ in range(20):
        salt.append(''.join(str(random.randint(0, 9)) for _ in range(20)))

    
    # Rastgele bir tuz seçmek
    random_salt = random.choice(salt)

   
    # Şifre ve tuzdan XOR yapılır
    xor_password = bytes(
        [ord(x) ^ ord(y) for x, y in zip(passwords[i][1], random_salt)])
   
    # SHA3_384 ile bir hash yapılır
    hash_object = hashlib.sha3_384(xor_password)

    # Dosyaya yazmak
    with open("Veritaban5.txt", 'a') as f:
        f.write(kullanici_adi_olusturmak() + ' ')
        f.write(hash_object.hexdigest() + ' ')
        for i in range(len(salt)):
            f.write(salt[i] + ' ')  
        f.write('\n')
