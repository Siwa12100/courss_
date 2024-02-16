# ============
# Exercice 1 :
# ============
print()
print("=-=-=-=-=-=-= Exo 1 =-=-=-=-=-=-=-=")

# 1.)
# ---
# Le calcul effectué est le renvoie de la valeur ASCII du caractère passé en paramètre.
# H(Ī) = 298

def H(lettre) :
    return ord(lettre)

print(H('A'))
print(H('Ī'))

# 2.)
# ---
# G(ABC) = H(A) * 1 + H(B) * 2 + H(C) * 3
def G(chaine):
    somme = 0
    for i, caractere in enumerate(chaine, start=1):
        somme += H(caractere) * i
    return somme

print(G('coucou'))


# ============
# Exercice 2 :
# ============
print()
print("=-=-=-=-=-=-= Exo 2 =-=-=-=-=-=-=-=")
import hashlib

mot="coucou"
sha256 = hashlib.sha256(mot.encode('utf-8')).hexdigest()
# print(sha256)

mot1 = "123456789"
print(" - " , mot1," --> ", hashlib.sha256(mot1.encode('utf-8')).hexdigest())

mot2 = "tungsten"
print(" - " , mot2," --> ", hashlib.sha256(mot2.encode('utf-8')).hexdigest())


