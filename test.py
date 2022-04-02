def hello(name):
    return "Hello" + str(name)

def odejmij(a,b):
    wynik = float(a) - float(b)
    return wynik

def dodaj(a,b):
    wynik = float(a) + float(b)
    return wynik

def pomnoz(a,b):
    wynik = float(a) * float(b)
    return wynik

def dzielenie(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

pierwsza = input()
druga = input()

print (dodaj(pierwsza, druga))
