print("Python est très utilisé")
print('Python est très utilisé')

# utiliser ' dans '' utiliser \
print("C'est facile de programmer en Python")
print('C\'est facile de programmer en Python')

# utiliser '' dans ' utiliser \
print("Python est fait pour les\"nuls\" ")
print('Python est fait pour les"nuls"')


# les 3 ''' ou """ sont utilisés pour des retours à la ligne autorisés
print("""Nous avons vu les types
          - int
          - float
          - str
          """
          )

print(''' Nous avons vu les types
          - int
          - float
          - str
          '''
      )

#  cas special n pour sauter a la ligne t tabulation
print("Nous avons vu les types : \n\t- int\n\t- float\n\t- str")

#ou pour plus propre
print("Nous avons vu les types : \n\t"
      "- int\n\t"
      "- float\n\t"
      "- str")

#trouver la lettre du numéro 3 de salut
nexemple: str = "salut ca va?"
print(nexemple[3])

#afficher en position pour afficher alu de salut, le dernier caractere est exclu
nexemple: str = "salut ca va?"
print(nexemple[1:4])

#concaténation
print('toi' + 'moi')
#répétition
print('toi' * 3)

# 3 x le 6 donc répétition
var1: str = '6'
print(var1 * 3)

#multiplication
var2: int = 6
print(var2 * 3)

#compter le nombre de caractère
print(len("Hello"))

#minuscule et majuscule
print("Hello" .lower())
print('hello' .upper())



print("""Nombre de cailloux et distances :
- Léa : """, total_lea, """ cailloux et """, km_lea, """ km
- Louis :
- Matilde :
- Eva :
- Roland : 
""")

#correction
DIST_CAILLOUX: int = 80
RESTE_LEA: int = 156
CAILLOUX_EVA: int = 322

cailloux_lea: int
cailloux_louis: int
cailloux_matilde: int
cailloux_roland: int

dist_eva: float
dist_eva: float
dist_louis: float
dist_matilde: float
dist_roland: float

cailloux_louis = RESTE_LEA * 3
cailloux_matilde = cailloux_louis + 233
cailloux_lea = CAILLOUX_EVA + 100 + RESTE_LEA
cailloux_roland = cailloux_louis * 2

dist_eva: CAILLOUX_EVA * DIST_CAILLOUX / 1000
dist_eva: cailloux_lea * DIST_CAILLOUX / 1000
dist_louis: cailloux_louis * DIST_CAILLOUX / 1000
dist_matilde: cailloux_matilde * DIST_CAILLOUX / 1000
dist_roland: cailloux_roland * DIST_CAILLOUX / 1000

