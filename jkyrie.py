class D():
    t = "abcdefghijklmnopqrstuvwxyz0123456789"
    def d(e,k): return D.k(D.s(e,k))
    def k(t: str):
        r=""
        for a in t: 
            if a in D.t:
                i=D.t.index(a)+1
                if i>=len(D.t):i=0
                a=D.t[i]
            r+=a
        return r
    def s(z,k):
        k=sum(ord(i)for i in k)
        while True:
            if k%4==0:break
            k+=1
        d=3
        t=r=""
        while True:
            if len(z)<=k:break
            t=z[k]
            z=z[k+1:]
            r+=chr(ord(t)-d)
        return r