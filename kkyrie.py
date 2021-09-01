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