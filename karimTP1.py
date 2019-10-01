# ## Déclaration des variables
annee: int
bissextile: bool

# ## Initialisation des variables
#tout d'abord on dit au programme de demander à l'utilisateur d'insérer l'année
#ensuite toujours dans la variable année on prend l'information tapée et on y ajoute dans annee

annee = int(input("Saisir une année:  "))
bissextile = False
# ## Séquence d'opération
#si le reste entier de l'année noté(modulo) est = à 0,
# donc ca sera multiple de 4 et chaque année bissextile est un multiple de 4
#selon wikipedia une année est bissextille seulement si elle est divisible par 4
# et non divisible par 10
#ou si l'année est divisible par 400

if  annee % 400 == 0:
    bissextile = True

elif annee % 100 == 0:
    bissextile = False

elif annee % 4 == 0:
    bissextile = True

if bissextile:
    print("L'année", annee, "est bissextile")
else:
    print("L'année", annee,"n'est pas bissextile ")
