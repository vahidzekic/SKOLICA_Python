prviBroj = 50
drugiBroj = 10
treciBroj = 15
cetvrtiBroj = 20

poruka1 = "Prvi broj je manji od drugog broja."
poruka2 = "Prvi broj je manji od treceg broja."
poruka3 = "Prvi broj je manji od cetvrtog broja."
poruka4 = "Prvi broj je veci od drugo, treceg i cetvrtog broja."


if prviBroj < drugiBroj:
    print(poruka1)
elif prviBroj < treciBroj:
    print(poruka2)
elif prviBroj < cetvrtiBroj:
    print(poruka2)
else:
    print(poruka4)
