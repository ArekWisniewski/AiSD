def zad9( a ):
    tyg=['poniedziałek','wtorek','środa','czwartek','piątek','sobota','niedziela']
    return tyg[(a-1)%7]

print(zad9(100))