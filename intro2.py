#puissance
print(2 ** 3)

#division entiere
print(2 // 3)

#donne le reste de la division c a dire le modulo
print(5 % 3)

#parentheses
print((2 + 50)* 12)


#var
print("exercice1 avec variables")





#déclaration variable

MASSE_TOTAL = 5000
caisse1: int
caisse2: int
caisse3: int
smasse_1: float
smasse_2: float
smasse_3: float

#initialisation variable

caisse1 = int(input("Combien de caisse de 54.5 KG charge-t-on à Genève?:  "))
caisse2 = int(input("Combien de caisse de 35 KG charge-t-on à Genève?: "))
caisse3 = int(input("Combien de caisse de 5 KG charge-t-on à Lausanne?: "))
caisse4 = int(input("Combien de ciasse de 12.5 KG charge-t-on à Montreux?: "))

#séquence d'opération

smasse_1 = MASSE_TOTAL - (caisse1 * 54.5 + caisse2 * 35)
smasse_2 = smasse_1 - (5 * caisse3)
smasse_3 = smasse_2 - (12.5 * caisse4)

#affichage résultat

print("""lors des différents chargements, les masses pouvant encore être ajoutées sont les suivantes :

- Après le 1er chargement, on peut encore ajouter {} KG dans le camion
- Après le 2ème chargement, on peut encore ajouter {} KG dans le camion
- Après le 3ème chargement, on peut encore ajouter {} KG dans le camion

""".format(smasse_1, smasse_2, smasse_3))











print(masse_1)
print(masse_2)
print(masse_3)

#exo supplementaire
print("exo supplementaire")

TOTAL_KM: float = 42.195

audrey: int = 17

marie: float = (2 * audrey) + 6.75

maz: float = marie - 9.27

laura: float = maz - 7.29

jean_fran: float = audrey + 8

print("marie:")
print(marie)

print("max:")
print(maz)

print("laura:")
print(laura)

print("jean_fran:")
print(jean_fran)

print("audrey:")
print(audrey)



#question: Mettre un espace après le <<:>>(pas avant) dans ppt, pourquoi python indique une gene et dit de mettre un espace?









