#NE PAS MODIFIER LES FONCTIONS
#JUSTE LES VALEURS EN BAS SOUS LE if __name__ == '__main__':

#NE PAS VALIDER LES REPONSES EN 1 MINUTE SUR LE MOODLE ON VA ETRE GRILLER


#JE NE GARANTIS PAS LE 100% DE REUSSITE ET JE SUIS EN AUCUN CAS RESPONSABLE DE VOTRE ECHEC
#SI VOUS ETES PAS CONTENT APPRENEZ LE COURS ET FAITES LE POUR DE VRAI !
#CA MARCHE PAS FORCEMENT REGARDEZ LE SUJET
from math import exp, log, pi, cos, sin, tan, acos, degrees, radians, sqrt


def ex1(U, f, i, phi):

    # Q1 : P => Puissance Active
    q1 = U * i * cos(radians(phi))
    print(f'Q1 : {q1} W')

    # Q2 : Q => Puissance Reactive
    q2 = U * i * sin(radians(phi))
    print(f'Q1 : {q2} VAR')

    # Q3 : S => Puissance Apparent
    q3 = sqrt(q1**2 + q2**2)
    print(f'Q1 : {q3} VA')

    # Q4 : Fp => Facteur de puissance
    q4 = cos( radians(phi) )
    print(f'Q4 : {q4} ')




def ex2(Moteur, U, f, r, Fp):
    rendement = r/100
    FacteurP = Fp / 100

    # Q5 : P => Puissance Active
    q5 = Moteur / rendement
    print(f'Q5 : {q5} kW')

    # Q6 : P => Puissance Reactive
    q6 = q5 * tan( acos(FacteurP) )
    print(f'Q6 : {q6} kVAR')

    # Q7 : I => Courant en A
    q7 = q5 / (U * FacteurP) * 1000
    print(f'Q7 : {q7} A')


def ex3(U, f, P, Q):

    # Q8 : R => Resistance en ohms
    q8 = (U**2) / P
    print(f'Q8 : {q8} ohms')

    # Q9 : C => Condensateur en µF
    q9 = Q / -(U**2 * 2*pi * f)
    print(f'Q9 : {q9} µF (ATTENTION: NE PAS METTRE LE 10 puissance -6 !!!!!!!!)')

    # Q10 : I => Courant en A
    S = sqrt( P**2 + Q**2 )
    q10 = S / U
    print(f'Q10 : {q10} A')

    # Q11 : Fp => Facteur puissance
    q11 = P / S
    print(f'Q11 : {q11} ')


if __name__ == '__main__':
    #Mettre les valeurs dans les mêmes unités que proposer par exemple
    # pour 11.4mH -> écrire 11.4
    #SI CHIFFRE A VIRGULE C'EST UN POINT A METTRE !!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #ATTENTION AUX UNITES QUE JE DEMANDE
    #la réponse est toujours donnée dans l'unité demandé ex q7 en ms

    # ------------------- EXO1
    # ex1(230, 50, 5.9, 49)

    # ------------------- EXO2
    ex2(7.4, 230, 50, 72, 63)

    # ------------------- EXO3
    # ex3(230, 50, 140, -92)
