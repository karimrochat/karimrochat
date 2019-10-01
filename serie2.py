#savoir le type de notre donnée
print(type(3))
print(type('bonjour'))

#convertir un type dans une autre= int (variable)
age:int = 28
print("j'ai " + str(age) + "ans ")
print("j'ai", age, "ans")
print("C'est mon", age, "ème anniversaire") #ne marche pas par exemple il faut faire la concaténation comme le premier

#formatagegg
var_1: float = 111.1135666
var_2: int = 222.2667774
print("Valeur de la 1ere variable: {} et de la 2eme {}".format(var_1, var_2)) # la var_1 est en position 0 et var2 en 1
print("Valeur de la 1ere variable: {1} et de la 2eme {0}".format(var_1, var_2)) # la var_1 est en position 0 et var2 en 1
print("Valeur de la 1ere variable: {:.2f} et de la 2eme {:.0f}".format(var_1, var_2)) # arrondi pour pas de virgule

#demander a lutilisateur son age
age = int(input("Quel âge as-tu? "))
print("dans 8 ans tu aura {} ans".format(age+8))

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

#déclaration
agex: str
agez: str
age: int

#initialisation
age = int(input("quel age as-tu): "))
agex = "Ce jeu est déconseillé au moins de 16 ans"
agex = "vous avez l'age requis"

#séquence et affichage
if age < 16:
   print(agex)
else
    print(agez)

