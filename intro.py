def ndigits(n):
    return len(str(n))


def nword(s):
    words=s.split(" ")
    return len(words)


def nsentences(s):
    return s.count(".")+s.count("!")+s.count("?")


def largest(a, b, c):
    if a > b:
        if a > c: 
            return a
        else:
            return c 
    else:
        if b > c: 
            return b 
        else:
            return c


def category(n):
    if n < 10:
        return "sub junior"
    elif n < 15:
        return "junior"
    elif n < 20:
        return "cadet"
    elif n < 30:
        return "senior"
    else:
        return "veteran"

def password():
    password="topsecret"
    got=input("Enter password: ")
    while(got!=password):
      got=input("Enter password:")
 
    print ("Success")
    return True    

def avg(l):
    count=len(l)
    total=0
    for i in l:
        print(f"Adding {i}")
        toatal+=i
    return total/count

def panagram(s):
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in s:
            print(f"{i} is missing")
            return False
        return True

def dumpfile(fname):
    f=open(fname)
    for i in f:
        print(i)
    f.close(fname)

