import argparse
import math

import requests
import os
import urllib3
import json
import random


def assertt(condition, message):
    if condition:
        return
    else:
        raise AssertionError(f'ERREUR: {message}')
        


def testlvl0(backend: str):
    print("LVL0")
    try:
        response = requests.get(f"{backend}/salut")
    except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
        assertt(False, f"Erreur lors de la connection au serveur: {e}")
        return
    assertt(response.status_code == 200, "LVL0: response code doit être 200")
    gang = "Salut la gang"
    assertt(response.content.decode() == gang, f"Le contenu de la réponse doit être exactement '{gang}' (sans les guillemets)")
    return True


def testlvl1(backend: str):
    print("LVL1")
    mots = [('la', 'gang'),('les', 'freres'), ('les', 'soeurs'), ('les', 'gens'),('l\'','ami')]
    for word1, word2 in mots:
        try:
            response = requests.get(f"{backend}/salut/{word1}/{word2}")
        except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
            assertt(False, f"Erreur lors de la connection au serveur: {e}")
            return
        assertt(response.status_code == 200, "response code doit être 200")
        gang = f"Salut {word1} {word2}"
        assertt(response.content.decode() == gang, f"Le contenu de la réponse doit être exactement '{gang}', puisqu'on a accédé à /salut/{word2}/{word2} (sans les guillemets)")
    return True


def testlvl2(backend: str):
    print("LVL2")
    mots = [(0, 50),(1, 40), (999, 999), (123, 1234)]
    for debut, fin in mots:
        try:
            response = requests.get(f"{backend}/json/?debut={debut}&fin={fin}")
        except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
            assertt(False, f"Erreur lors de la connection au serveur: {e}")
            return
        assertt(response.status_code == 200, "response code doit être 200")
        assertt(response.headers.get('Content-Type') == 'application/json', "La réponse doit contenir un header 'Content-Type: application/json'.")
        try:
            data = json.loads(response.content)
        except Exception as e:
            assertt(False, f"La réponse doit être du JSON valide: {e}")

        assertt("Woop" in data, "'Woop' doit être une clé dans la réponse")
        assertt(data['Woop'] == 'woop', f"'woop' doit être la valeur à la clé 'Woop'. Obtenu: {data['Woop']}")
        assertt("suite" in data, "'suite' doit être une clé dans la réponse")

        expected = [a for a in range(debut, fin)]
        assertt(data['suite'] == expected, f'La suite ne correspond pas à ce qui est attendu pour un début {debut} et une fin {fin}.\n' +
                                           f'Attendu: {expected}\nObtenu: {data["suite"]}')
    return True


def testlvl3(backend: str):
    print("LVL3")
    try:
        response = requests.get(f"{backend}/brique")
    except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
        assertt(False, f"Erreur lors de la connection au serveur: {e}")
        return
    assertt(response.status_code == 200, "response code doit être 200 pour le GET. Obtenu: " + str(response.status_code))
    assertt(response.headers.get('Content-Type') == 'application/json', "La réponse doit contenir un header 'Content-Type: application/json'.")
    try:
        data = json.loads(response.content)
    except Exception as e:
        assertt(False, f"La réponse doit être du JSON valide: {e}")

    assertt(type(data) == list, "La réponse doit être une liste")
    assertt(len(data) == 0, f"La liste doit être initialement vide. Taille de la liste: {len(data)}")

    briques = []

    for i in range(5):
        largeur = random.random()
        hauteur = random.random()
        name = f'brique{i}'
        try:
            response = requests.post(f"{backend}/brique", json={"name": name, 'hauteur': hauteur, 'largeur': largeur})
        except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
            assertt(False, f"Erreur lors de la connection au serveur: {e}")
            return
        assertt(response.status_code == 201, f'Le status code de réponse doit être 201 quand on post sur /brique et que l\'insertion est faite. Obtenu: {response.status_code}')
        briques.append((name, hauteur, largeur))

    try:
        response = requests.get(f"{backend}/brique")
    except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError) as e:
        assertt(False, f"Erreur lors de la connection au serveur: {e}")
        return
    assertt(response.status_code == 200, "response code doit être 200 pour le GET")
    assertt(response.headers.get('Content-Type') == 'application/json', "La réponse doit contenir un header 'Content-Type: application/json'.")
    try:
        data: list = json.loads(response.content)
    except Exception as e:
        assertt(False, f"La réponse doit être du JSON valide: {e}")

    assertt(type(data) == list, "La réponse doit être une liste")
    assertt(len(data) == 5, f"La liste doit avoir une taille de 5 après l'insertion")
    for i, brique in enumerate(briques):
        assertt('name' in data[i], f'La {i + 1}e brique doit avoir "name" comme attribut.')
        assertt(data[i]['name'] == brique[0],
                f'La {i + 1}e brique doit avoir le nom {brique[0]}. Nom: {data[i]["name"]}')
        assertt('hauteur' in data[i], f'La {i + 1}e brique doit avoir "hauteur" comme attribut.')
        assertt(math.isclose(data[i]['hauteur'],  brique[1], abs_tol=0.01),
                f'La {i + 1}e brique doit avoir la hauteur {brique[1]}. Hauteur: {data[i]["hauteur"]}')
        assertt('largeur' in data[i], f'La {i + 1}e brique doit avoir "largeur" comme attribut.')
        assertt(math.isclose(data[i]['largeur'], brique[2], abs_tol=0.01),
                f'La {i + 1}e brique doit avoir la largeur {brique[2]}. Largeur: {data[i]["largeur"]}')

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend')
    backend: str = parser.parse_args().backend
    print(f"LVL0: {os.environ.get('lvl0')}" if testlvl0(backend) else "")
    print(f"LVL1: {os.environ.get('lvl1')}" if testlvl1(backend) else "")
    print(f"LVL2: {os.environ.get('lvl2')}" if testlvl2(backend) else "")
    print(f"LVL3: {os.environ.get('lvl3')}" if testlvl3(backend) else "")