#!/usr/bin/env python




def chiffrement(p, m):
    """
    fonction qui permet de chiffrer et dechiffrer un message
    """
    split = m.split()
    print(split)
    ch = ""
    phrase = []

    for i in range(len(split)):
        for j in split[i]:
            if ord(j) >= 65 and ord(j) <= 90 :
                t = (ord(j)-65+p)%26
                t = t+65
                t = chr(t)
                ch += t
            
            elif ord(j) >= 97 and ord(j) <= 122 :
                t = (ord(j)-97+p)%26
                t = t+97
                t = chr(t)
                ch += t


            elif ord(j) < 65 or ord(j) > 90 or ord(j) < 97 or ord(j) > 122:
                ch += j
                
                
        phrase.append(ch)
        print(ch)
        ch = ""
    phrase = " ".join(phrase)
    return phrase

#interaction
def interaction():
    """
    fonction qui permet l'interraction avec l'utilisateur pour chiffrer ou dechiffrer un message
    """

    choix = 0 #variable qui permet de sortir de la boucle while apres avoir choisi
    interaction = 0 # variable qui permet de mettre fin a la fonction interraction
    print("Bonjour et bienvenue sur CodicusCesarus !") 
    continuite =  0
    
        
    #permet de garder une continuité dans la fonction d'interraction

    """le choix de l'utilisateur"""

    while choix != 1: #boucle pour eviter que le programme soit casse par la suite si la reponse est pas bonne
        choix = input("""que souhaitez vous faire ?
1: Pour chiffrer un texte
2: Pour déchiffrer un texte
quel est votre choix ?""")

        if choix !="1" and choix != "2":
            print("Hum veuillez renseigner une réponse valide !")
    
        """execution en fonction du choix"""
        if choix == "1": #ppour chiffrer
                
            m = str(input("quel message souhaitez vous coder ?")) #m pour message
            p = int(input("quel pas souhaitez vous prendre ?")) #p pour pas
            print("voici votre message coder:", chiffrement(p, m))
        
        if choix == "2": #pour déchiffrer
            m = input("quel message souhaitez vous decoder ?")
            p = str(input("quel est le pas que vous souhaitez utiliser pour déchiffrer ?"))
            p = int("-" + p)
            print(chiffrement(p, m))
            
        
            
        """savoir si l"utilisateur veut continuer ou non"""
        while interaction != "oui" and interaction!= "non":
            interaction = input("Souhaitez vous chiffrer ou dechiffrer un autre message ? (oui/non)")
            if interaction == "oui":
                choix = 0
            if interaction == "non":
                choix = 1
        




interaction() # on lance directement la fonction

