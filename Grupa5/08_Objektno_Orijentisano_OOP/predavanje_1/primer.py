#!/usr/bin/env python3
# Grupa5 / 08 / P1 â Klase

class FudbalskiTim:
    def __init__(self, naziv, grad, godina_osnivanja):
        self.naziv = naziv
        self.grad = grad
        self.godina = godina_osnivanja
        self.bodovi = 0
        self.golovi = 0

    def pobeda(self, dati, primljeni):
        self.bodovi += 3
        self.golovi += dati

    def nereseno(self, dati, primljeni):
        self.bodovi += 1
        self.golovi += dati

    def __str__(self):
        return f"{self.naziv} ({self.grad}) â {self.bodovi}b, {self.golovi}g"

t1 = FudbalskiTim("Partizan", "Beograd", 1945)
t2 = FudbalskiTim("Vojvodina", "Novi Sad", 1914)
t1.pobeda(3, 1)
t1.pobeda(2, 0)
t1.nereseno(1, 1)
t2.pobeda(1, 0)
print(t1)
print(t2)