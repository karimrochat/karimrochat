#print "python est très utilisé" puis print 'Python est très utilisé'



#print "C'est facile de programmer en Pyhton" et print 'C'est facile de programmer en Pyton alt+maj+/



# print "python est fait pour les "nuls" " et print 'Python est fait pour les "nuls" '



# print """ Nous avons vu les types - int - float - str """



# print ''' Nous avons vu les types - int - float - str '''




# print " Nous avons vu les types en utilisant des sauts de pages et tabulations"



# print la meme chose mais en plus propre , sauts a la ligne



#trouver la lettre du numéro 3 de "salut ca va" qui est tout d'abord mis dans une variable ensuite print  , reponse: u



#afficher en position pour afficher alu de salut, le dernier caractere est exclu, il y a variable de salut cava et print




#print une concaténation de toi et moi en texte



#print une répétition de toi pour avoir le resultat toitoitoi



# faire une variable avec 6 en valeur str puis le print pour obtenir la répetition 666



#taper une variable avec le 6 en entier et le print pour obtenir le resultat de 6*3



#compter le nombre de caractère dans Hello donc print tout simplement Hello en comptant le nb de caractère



#minuscule et majuscule faire de meme mais en mettant un print pour Hello et un autre pour hello, l'un sera en maj lautre en min


#exercice avec les cailloux



#déclarer les variables

CAILLOUX: float
LEA_CAILLOUX: int
EVA_CAILLOUX: int

lea2_cailloux: int
louis_cailloux: int
matilde_cailloux: int
roland_cailloux: int

lea_distance: int
louis_distance: int
matilde_distance: int
eva_distance: int
roland_distance: int

#initialiser les variables
CAILLOUX: float = 0.08
LEA_CAILLOUX: int = 156
EVA_CAILLOUX: int = 322


#séquence d'opération

louis_cailloux = LEA_CAILLOUX * 3
matilde_cailloux = louis_cailloux + 233
lea2_cailloux = LEA_CAILLOUX + EVA_CAILLOUX + 100
roland_cailloux = louis_cailloux * 2

lea_distance: int = lea2_cailloux * CAILLOUX
louis_distance: int = louis_cailloux * CAILLOUX
matilde_distance: int = matilde_cailloux * CAILLOUX
eva_distance: int = EVA_CAILLOUX * CAILLOUX
roland_distance: int = roland_cailloux * CAILLOUX

print("Nombre de cailloux et distances\n\t"
      " - Léa : ",lea2_cailloux,"cailloux et", lea_distance," KM \n\t"
         " - Louis : ",louis_cailloux,"cailloux et",louis_distance, " KM\n\t" 
             " - Matilde :", matilde_cailloux,"cailloux et", matilde_distance, "KM\n\t"
                 " - Eva :",EVA_CAILLOUX,"cailloux et",eva_distance,"KM\n\t"
                     " - Roland :",roland_cailloux,"cailloux et",roland_distance,"KM\n\t")
