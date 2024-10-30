def inverse_chaine(chaine):
    result = ""
    for caractere in chaine :
        result = caractere + result
    return result

def est_palindrome(chaine):
    # penser à ecrire entre guillement lors de l'exécution
    # ex : est_palindrome("kayak")
    inverse = inverse_chaine(chaine)
    if chaine != inverse:
        return "Ce mont n'est pas un palindrome..."
    else :
        return "Ce mot est un palindrome !"

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)