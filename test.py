def hello(name):
    return "Hello" + str(name)

def odejmij(a,b):
    wynik = float(a) - float(b)
    return wynik

def dodaj(a,b):
    wynik = float(a) + float(b)
    return wynik

pierwsza = input()
druga = input()

print (dodaj(pierwsza, druga))