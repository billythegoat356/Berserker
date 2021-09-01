from random import choice, randint

strings = "abcdefghijklmnopqrstuvwxyz0123456789"



class Encrypt:

    
    def encrypt(e: str):
        e1 = Encrypt._kyrie(e)
        return Encrypt._encrypt(e1)


    def _kyrie(text: str):
        
        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r


    def _encrypt(text: str):
        while True:
            n = randint(3, 150)
            if n % 4 == 0:
                break
        d = randint(3, 15)
        t = [chr(ord(t)+d) for t in text]
        r = "".join(
            "".join(choice(strings) for _ in range(n)) + i
            for i, _ in zip(t, range(len(t)))
        )
        spcar = choice(("_", "-", "%", "&"))
        r += "".join(choice(strings) for _ in range(int(n/4))) + spcar + str(n) + spcar + "".join(choice(strings) for _ in range(int(n/4))) + "".join(choice(strings) for _ in range(int(n/4))) + spcar + str(d) + spcar + "".join(choice(strings) for _ in range(int(n/4)))
        return r


class KeyEncrypt:

    def encrypt(e: str, key: str):
        e1 = KeyEncrypt._kyrie(e)
        return KeyEncrypt._encrypt(e1, key=key)

    def _kyrie(text: str):

        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r

    def _encrypt(text: str, key: str):
        n = sum(ord(i) for i in key)
        while True:
            if n % 4 == 0:
                break
            n += 1
        d = 3
        t = [chr(ord(t)+d) for t in text]
        r = "".join(
            "".join(choice(strings) for _ in range(n)) + i
            for i, _ in zip(t, range(len(t)))
        )
        spcar = choice(("_", "-", "%", "&"))
        return r



class KeyDecrypt():


    def decrypt(e: str, key: str):
        e1 = KeyDecrypt._decrypt(e, key)
        return KeyDecrypt._kyrie(e1)

    def _kyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _decrypt(text: str, key: str):

        n = sum(ord(i) for i in key)
        while True:
            if n % 4 == 0:
                break
            n += 1
        d = 3
        t = ""
        r = ""
        while True:
            if len(text) <= n:
                break
            t = text[n]
            text = text[n+1:]
            r += chr(ord(t)-d)
        return r


class Decrypt():

    def decrypt(e: str):
        spcar = ""
        for a in reversed(e):
            if a not in strings:
                spcar = a
                break
        e1 = Decrypt._decrypt(e, spcar)
        return Decrypt._kyrie(e1)

    def _kyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _decrypt(text: str, spcar: str):
        n = int(text.split(spcar)[1])
        d = int(text.split(spcar)[3])
        text = text.split(spcar)[0] + \
            text.split(spcar)[2] + text.split(spcar)[4]
        t = ""
        r = ""
        while True:
            if len(text) == n:
                break
            t = text[n]
            text = text[n+1:]
            r += chr(ord(t)-d)
        return r

