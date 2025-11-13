#!/usr/bin/env python3
"""
truth_creole.py - Analiz konplè mo kréol réyoné
Montré konvèsyon, propriété mathématik, hash, etc.
"""

import math
import hashlib
import base64
import sys

# Alfabè kréol réyoné
ALPHABET_CREOLE = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    # Karaktèr asan-tild kréol
    'É': 5, 'È': 5, 'Ê': 5, 'Ë': 5,
    'À': 1, 'Â': 1,
    'Î': 9, 'Ï': 9,
    'Ô': 15, 'Ö': 15,
    'Ù': 21, 'Û': 21, 'Ü': 21,
    'Ç': 3,
    'Ñ': 14
}

ALPHABET_INVERSE = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}

def encoder_mot_creole(mot):
    """Ankod yon mot kréol an sékans numérik"""
    mot = mot.upper().strip()
    resultat = []
    
    for lettre in mot:
        if lettre in ALPHABET_CREOLE:
            numero = ALPHABET_CREOLE[lettre]
            resultat.append(str(numero))
        elif lettre.isalpha():
            numero = ord(lettre) - ord('A') + 1
            resultat.append(str(numero))
    
    return '.'.join(resultat)

def decoder_sequence_creole(sequence):
    """Dékod yon sékans numérik an mot kréol"""
    nombres = sequence.split('.')
    mot_decode = []
    
    for nombre in nombres:
        if nombre.isdigit():
            numero = int(nombre)
            if 1 <= numero <= 26:
                lettre = ALPHABET_INVERSE[numero]
                mot_decode.append(lettre)
    
    return ''.join(mot_decode)

def mot_vers_nombre(mot):
    """Converti yon mot kréol an yon nonb inik (sòm kod)"""
    mot = mot.upper().strip()
    total = 0
    
    for lettre in mot:
        if lettre in ALPHABET_CREOLE:
            total += ALPHABET_CREOLE[lettre]
    
    return total

def analyser_mot_creole(mot):
    """Analiz konplè yon mot kréol"""
    results = {}
    
    # Enfòrmasyon dé baz
    results['mot_original'] = mot
    results['mot_majuscules'] = mot.upper()
    results['mot_minuscules'] = mot.lower()
    results['longueur_mot'] = len(mot)
    
    # Ankodaj kréol
    results['sequence_creole'] = encoder_mot_creole(mot)
    results['valeur_numerique'] = mot_vers_nombre(mot)
    
    # Dékodaj (pou vérifikasyon)
    results['mot_decode'] = decoder_sequence_creole(results['sequence_creole'])
    
    # Propriété tèks
    results['est_palindrome'] = est_palindrome(mot)
    results['nombre_voyelles'] = compter_voyelles_creoles(mot)
    results['nombre_consonnes'] = compter_consonnes_creoles(mot)
    results['lettres_uniques'] = lettres_uniques(mot)
    results['mots_creoles'] = detecter_mots_creoles(mot)
    
    # Analiz numérik bazé sou valè total
    nombre = results['valeur_numerique']
    results.update(analyser_nombre(nombre))
    
    return results

def analyser_nombre(nombre):
    """Analiz konplè yon nonb"""
    results = {}
    
    # Konvèsyon dé baz
    results['decimal'] = nombre
    results['hexadecimal'] = hex(nombre)[2:].upper()
    results['binary'] = bin(nombre)[2:]
    results['octal'] = oct(nombre)[2:]
    
    # Propriété mathématik
    results['parity'] = "Enpèr (Odd)" if nombre % 2 else "Pèr (Even)"
    results['factors'] = factorize(nombre)
    results['prime_status'] = "Prim (Prime)" if is_prime(nombre) else "Konpozé (Composite)"
    results['digit_sum'] = sum(int(d) for d in str(nombre))
    results['digit_count'] = len(str(nombre))
    results['square'] = nombre ** 2
    results['cube'] = nombre ** 3
    if nombre >= 0:
        results['square_root'] = math.sqrt(nombre)
    else:
        results['square_root'] = float('nan')
    
    # Hash é kriptografi
    results['md5'] = hashlib.md5(str(nombre).encode()).hexdigest()
    results['sha256'] = hashlib.sha256(str(nombre).encode()).hexdigest()
    results['base64'] = base64.b64encode(str(nombre).encode()).decode()
    
    # Valè kiltirèl kréol
    results['signification_nombre'] = signification_nombre_creole(nombre)
    
    return results

def est_palindrome(mot):
    """Vérifié si mo-a sé yon palindrome"""
    mot = mot.upper().replace(' ', '')
    # Nétwayé karaktèr spéso
    mot_nettoye = ''.join(c for c in mot if c in ALPHABET_CREOLE or c.isalpha())
    return mot_nettoye == mot_nettoye[::-1]

def compter_voyelles_creoles(mot):
    """Konté vwayèl kréol"""
    voyelles = 'AEÉÈÊËÀÂIÎÏOÔÖUÛÜY'
    mot = mot.upper()
    return sum(1 for lettre in mot if lettre in voyelles)

def compter_consonnes_creoles(mot):
    """Konté konson kréol"""
    consonnes = 'BCÇDFGHJKLMNPQRSTVWXZ'
    mot = mot.upper()
    return sum(1 for lettre in mot if lettre in consonnes)

def lettres_uniques(mot):
    """Rétourné lèt inik nan mo-a"""
    return ''.join(sorted(set(mot.upper())))

def detecter_mots_creoles(mot):
    """Détèkté si mo-a sé yon mo kréol konn"""
    mots_creoles_communs = {
        'BONZOUR': 'Bonjour',
        'SAVA': 'Ça va',
        'MÉRSI': 'Merci',
        'WALÉ': 'Regarde',
        'LAKAZ': 'Maison',
        'ZANFAN': 'Enfant',
        'GRAMOUN': 'Vieillard',
        'KARÉ': 'Carré',
        'ZOURÉ': 'Travailler',
        'VIV': 'Vivre',
        'MANZ': 'Manger',
        'DORMI': 'Dormir'
    }
    
    mot_upper = mot.upper()
    if mot_upper in mots_creoles_communs:
        return f"Mo kréol konn: {mots_creoles_communs[mot_upper]}"
    else:
        return "Mo kréol posib"

def signification_nombre_creole(nombre):
    """Signifikasyon nonb dan kiltir kréol"""
    significations = {
        1: "Kommenman, inité",
        2: "Koupl, dualité",
        3: "Famni, Trinité",
        4: "Karé, stabilité",
        5: "Senk - senk sans (les cinq sens)",
        6: "Sièz - labitid",
        7: "Sèt - bonèr",
        8: "Wit - infinité",
        9: "Nèf - akonplisman",
        10: "Dis - totalité",
        15: "Kenz - importan dan kiltir kréol",
        26: "Vensisé - nonb lèt alfabè"
    }
    
    return significations.get(nombre, "Nonb jénéral")

def factorize(n):
    """Faktorizé yon nonb"""
    if n < 2:
        return [n]
    
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Vérifié si yon nonb sé prim"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def afficher_table_creole():
    """Montré tablo korespondans kréol"""
    print("\n" + "="*70)
    print("TABLO KORESPONDANS KRÉOL RÉYONÉ KONPLÈ")
    print("="*70)
    
    alphabet = list(ALPHABET_CREOLE.items())
    # Triyé par valè numérik (san doublon pou karaktèr spéso)
    alphabet_unique = []
    valeurs_vues = set()
    for lettre, valeur in alphabet:
        if valeur not in valeurs_vues:
            alphabet_unique.append((lettre, valeur))
            valeurs_vues.add(valeur)
    
    alphabet_unique.sort(key=lambda x: x[1])
    
    print("Alfabè dé baz:")
    for i in range(0, len(alphabet_unique), 6):
        ligne = alphabet_unique[i:i+6]
        for lettre, num in ligne:
            print(f"{lettre}={num:2d}", end="  ")
        print()
    
    print("\nKaraktèr asan-tild (akson kréol):")
    caracteres_speciaux = [
        ('É, È, Ê, Ë', 5), ('À, Â', 1), ('Î, Ï', 9), 
        ('Ô, Ö', 15), ('Ù, Û, Ü', 21), ('Ç', 3), ('Ñ', 14)
    ]
    for car, num in caracteres_speciaux:
        print(f"  {car:15} = {num:2d}")

def afficher_resultats(results):
    """Montré rézilta an fòma"""
    print("="*80)
    print(f"ANALIZ KONPLÈ MO KRÉOL: '{results['mot_original']}'")
    print("="*80)
    
    print("\nENFÒMASYON JÉNÉRAL")
    print(f"    Mo orijinal : {results['mot_original']}")
    print(f"    An majiskil : {results['mot_majuscules']}")
    print(f"    An miniskil : {results['mot_minuscules']}")
    print(f"    Longè mo : {results['longueur_mot']} karaktè")
    print(f"    Palindrome : {'Wi (Yes)' if results['est_palindrome'] else 'Non (No)'}")
    
    print("\nANALIZ LENGWISTIK")
    print(f"    Nonb vwayèl : {results['nombre_voyelles']}")
    print(f"    Nonb konson : {results['nombre_consonnes']}")
    print(f"    Lèt inik : {results['lettres_uniques']}")
    print(f"    Nòt kréol : {results['mots_creoles']}")
    
    print("\nANKODAJ KRÉOL")
    print(f"    Sékans numérik : {results['sequence_creole']}")
    print(f"    Mo dékodé (vérifikasyon) : {results['mot_decode']}")
    print(f"    Valè numérik total : {results['valeur_numerique']}")
    
    print("\nANALIZ NUMÉRIK VALÈ TOTAL")
    print(f"    Décimal : {results['decimal']}")
    print(f"    Égzadésimal : {results['hexadecimal']}")
    print(f"    Binèr : {results['binary']}")
    print(f"    Oktal : {results['octal']}")
    
    print(f"\n    Parité : {results['parity']}")
    print(f"    Faktè : {', '.join(map(str, results['factors']))}")
    print(f"    Prim ou Konpozé : {results['prime_status']}")
    print(f"    Sòm chif : {results['digit_sum']}")
    
    print(f"\n    Karé : {results['square']}")
    print(f"    Kib : {results['cube']}")
    if not math.isnan(results['square_root']):
        print(f"    Rasin karé : {results['square_root']:.4f}")
    
    print("\nHASH KRIPTOGRAFI")
    print(f"    MD5 : {results['md5']}")
    print(f"    SHA-256 : {results['sha256']}")
    print(f"    Base64 : {results['base64']}")
    
    print("\nSIGNIFIKASYON KRÉOL")
    print(f"    Signifikasyon nonb : {results['signification_nombre']}")
    
    # Montré détail ankodaj
    print("\nDÉTAIL ANKODAJ LÈT PA LÈT")
    mot = results['mot_original'].upper()
    for i, lettre in enumerate(mot):
        if lettre in ALPHABET_CREOLE:
            code = ALPHABET_CREOLE[lettre]
            print(f"    {i+1:2d}. {lettre} = {code:2d}")
        elif lettre.isalpha():
            code = ord(lettre) - ord('A') + 1
            print(f"    {i+1:2d}. {lettre} (laten) = {code:2d}")

def main():
    if len(sys.argv) != 2:
        print("Itilizasyon: python truth_creole.py <mo_kréol>")
        print("Égzamp: python truth_creole.py BONZOUR")
        print("Égzamp: python truth_creole.py \"2.15.14.26.15.21.18\" (pou dékodé)")
        sys.exit(1)
    
    entree = sys.argv[1].strip()
    
    try:
        # Gadé si sé yon sékans numérik
        if '.' in entree and all(part.isdigit() for part in entree.split('.')):
            mot_decode = decoder_sequence_creole(entree)
            print(f"🔓 Sékans dékodé : {entree} → {mot_decode}")
            results = analyser_mot_creole(mot_decode)
        else:
            results = analyser_mot_creole(entree)
        
        afficher_resultats(results)
        afficher_table_creole()
        
    except Exception as e:
        print(f"❌ Erèr : {e}")
        sys.exit(1)

def interface_interactive():
    """
    Entèrfas aktif pou analiz plizyè mo
    """
    print("=== ANALIZ KRÉOL RÉYONÉ KONPLÈ ===")
    print("Analiz lengwistik, ankodaj, propriété mathématik, hash")
    print("\nLòd:")
    print("  - Antre yon mo kréol pou analizé")
    print("  - Antre yon sékans numérik pou dékodé é analizé")
    print("  - 'tablo' pou wè tablo korespondans")
    print("  - 'kité' pou sorti")
    print("-" * 70)
    
    while True:
        try:
            entree = input("\nAntre yon mo ou yon sékans : ").strip()
            
            if entree.lower() == 'kité':
                print("Orevwar! À la prochaine!")
                break
            elif entree.lower() == 'tablo':
                afficher_table_creole()
                continue
            
            if not entree:
                continue
            
            # Analiz antre-a
            if '.' in entree and all(part.isdigit() for part in entree.split('.')):
                mot_decode = decoder_sequence_creole(entree)
                print(f"🔓 Sékans dékodé : {entree} → {mot_decode}")
                results = analyser_mot_creole(mot_decode)
            else:
                results = analyser_mot_creole(entree)
            
            # Montré yon rézimé
            print(f"\n📊 RÉZIMÉ POU '{results['mot_original']}':")
            print(f"   Sékans: {results['sequence_creole']}")
            print(f"   Valè total: {results['valeur_numerique']}")
            print(f"   Longè: {results['longueur_mot']} karaktè")
            print(f"   Palindrome: {'Wi' if results['est_palindrome'] else 'Non'}")
            print(f"   MD5: {results['md5'][:16]}...")
            
            voir_complet = input("\nWè analiz konplè? (w/n): ").strip().lower()
            if voir_complet in ['w', 'wi', 'y', 'yes']:
                afficher_resultats(results)
                
        except KeyboardInterrupt:
            print("\n\nOrevwar! À la prochaine!")
            break
        except Exception as e:
            print(f"❌ Erèr : {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Mòd aktif
        interface_interactive()
    else:
        # Mòd lòd-ligne
        main()
