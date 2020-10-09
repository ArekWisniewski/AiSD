def zad8():
    a=[]
    b=''
    print("Podawaj wartości do listy. Zakończ wyrażeniem 'stop'. :)")
    while(b!="stop"):
        if b!="":
            a.append(b)
        b=input()
    return tuple(a)

print(zad8())