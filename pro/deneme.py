import random

sifreleme_a = "abcdefghABCDEFGH"
sifreleme_n = "12345678"
sifreleme_s = "/&%+*?-_"

parola_l = int(input("parolanızın uzunluğunu belirleyiniz:"))

parola = ""

sayim = 0

for i in range(parola_l):
    
        parola += random.choice(sifreleme_a)
        sayim += 1

        if sayim >= parola_l:
            break

        parola += random.choice(sifreleme_n)
        sayim += 1

        if sayim >= parola_l:
            break

        parola += random.choice(sifreleme_s)
        sayim += 1

        if sayim >= parola_l:
                break

print(parola)
