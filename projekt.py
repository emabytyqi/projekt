notat = {}
piket = int(input("Shkruaj numrin e nxënësve: "))
for i in range(piket):
    emri = input(f"Shkruaj emrin e nxënësit {i+1}: ")
    nota = float(input(f"Shkruaj notën e nxënësit {emri}: "))
    notat[emri] = nota
print("Lista e notave për nxënësit është:")
for emri, nota in notat.items():
    print(f"{emri}: {nota}")
notat_lista = list(notat.values())
mesatarja = sum(notat_lista) / len(notat_lista)
maximale = max(notat_lista)
minimale = min(notat_lista)
print(f"Mesatarja e notave është: {mesatarja}")
print(f"Maximajla e notave eshte: {maximale}")
print(f"Vlera minimale e notave është: {minimale}")