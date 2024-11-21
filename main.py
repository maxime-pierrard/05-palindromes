"""
Dans cet exercice on vérifie si une chaine de caractère est un palindrome.
On va appeller dans une fonction main, une fonction is palindrome qui le vérifie.
"""
#### Fonction secondaire


def ispalindrome(p):
    # votre code ici
    """
    Cette méthode remplace les caracteres avec des accents par leurs caractères sans accent
    et elle est transforme toute la string en minuscule et pour finir,
    elle compare le premier caractere avec le dernier puis le deuxieme avec l'avant dernier etc 
    """
    rep=True
    p=p.lower()
    accents=str.maketrans("éèêëàâäîïôöùûüç","eeeeaaaiioouuuc"," ,?;.:/!'()-")
    p=p.translate(accents)
    x=len(p)
    for i in range(0,x):
        a=p[i]
        b=p[x-i-1]
        if a!=b:
            rep=False
    return rep

#### Fonction principale


def main():
    """
    Cette méthode appelle ispalindrome et affiche le string et son booléen.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "étoile", "Maxime","NINON","RADAR"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
