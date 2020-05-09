def jeu_ordi(nb_allum, prise_max):
    s = prise_max + 1
    t = (nb_allum - s) % (prise_max + 1)
    while(t != 0):
        s -= 1
        t = (nb_allum - s) % (prise_max + 1)
    prise = s - 1
    if ( prise == 0):
        prise = 1
    print("l'ordinateur en prend : ", prise)
    return prise



def afficher_allumettes(n):
    for i in range(0, n):
        print('°', end=' ')
    print()
    for i in range(0, n):
        print("|", end=' ')
    print()



def main():
    # initialisation des variables.
    nb_max_d=0 #nbre d'allumettes maxi au départ
    nb_allu_max=0 #nbre d'allumettes maxi que l'on peut tirer au maxi
    nb_allu_rest=0; #nbre d'allumettes restantes
    prise=0 #nbre d'allumettes prises par le joueur
    qui = -1 #qui joue? 0=User --- 1=PC
    # verification pour l'initialisation.
    while( nb_max_d < 10 or nb_max_d > 60):
        try:
            nb_max_d=int(input("Entrez un nombre max d'allumette au depart entre 10 et 60 : "))
        except:
            print("saisie incorrecte")
    # mise a jour du nombre d'allumette en jeu.
    nb_allu_rest=nb_max_d

    # Définir le nombre d'allumette max que l'on peut tirer
    while( nb_allu_max < 1 or  nb_allu_max > nb_max_d):
        try:
            nb_allu_max=int(input("Entrez un nombre max d'allumette que l'on peut retirer : "))
        except:
            print("saisie incorrecte")
    
    print("Qui commence à jouer ? tapper\n 0 : Vous \n 1 : Ordinateur")
    
    qui=int(input("Qui : "))
    

    print("Le jeu va commencer \nIl y a %i allumettes \nVous pouvez retirez au maximum %i allumettes" % (nb_allu_rest, nb_allu_max))
    if (qui == 0):
        print ("Vous allez commencer à jouer\n C'est parti!")
    else :
        print ("L'ordinateur va commencer à jouer\n C'est parti!")
    afficher_allumettes(nb_allu_rest)
    # Jouer tant qu il reste des allumettes 
    while(nb_allu_rest>0):
        if(qui == 0) : 
            print("Il reste %i allumettes \nVous pouvez retirez au maximum %i allumettes" % (nb_allu_rest, nb_allu_max))
            
            while( prise < 1 or prise > nb_allu_max):
                try:
                    prise = int(input("Quel est le nombre d'allumettes que vous voulez retirer ?"))
                except:
                    print("saisie incorrecte")
            
            nb_allu_rest-=prise
            afficher_allumettes(nb_allu_rest)
            qui = 1 
            prise = 0
        else :
            prise = jeu_ordi(nb_allu_rest,nb_allu_max)
            nb_allu_rest-=prise
            afficher_allumettes(nb_allu_rest)
            qui = 0
            prise = 0
    if (qui == 0) : 
        print ("BRAVO! Vous avez gangnez ! ")
    else:
        print ("L'ordinateur a gagné !")

if __name__ == '__main__':
   main()
