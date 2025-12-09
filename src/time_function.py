from datetime import datetime, timedelta,time

# Fonction pour extraire le temps d'un nom de fichier de spectre
def extraire_temps(str_heure):
    heure=int(str_heure[:2])
    minutes=int(str_heure[3:5])
    secondes=int(str_heure[6:8])
    return 60*heure+minutes+round(secondes/60)-9*60


def time_to_minutes(time_obj):
    # Calculer le nombre total de minutes
    total_minutes = time_obj.hour * 60 + time_obj.minute
    return total_minutes-540



def heure_plus_proche(heure_cible, liste_heures):
    """Fonction qui permet de faire correspondre le spectre Raman 
    dont l'heure de mesure est la plus proche des mesures de conventration en glucose et éthanol"""
    # Convertir chaque heure de la liste en objet datetime.time
    heures_time = [datetime.strptime(h, "%H:%M:%S").time() for h in liste_heures]

    # Initialiser les variables pour trouver l'heure la plus proche
    heure_plus_proche_obj = None
    plus_petite_difference = float('inf')

    for heure in heures_time:
        # Calculer la différence absolue en secondes
        difference = abs((datetime.combine(datetime.today(), heure) - datetime.combine(datetime.today(), heure_cible)).total_seconds())

        # Mettre à jour l'heure la plus proche si une différence plus petite est trouvée
        if difference < plus_petite_difference:
            plus_petite_difference = difference
            heure_plus_proche_obj = heure

    # Retourner l'heure la plus proche au format HH:MM:SS
    return heure_plus_proche_obj.strftime("%H:%M:%S")


#test unitaire 
if __name__=='__main__':
    liste_heures = ["00:00:00", "06:00:00", "12:00:00", "18:00:00", "23:59:59"]
    assert heure_plus_proche(time(0, 5, 0), liste_heures) == "00:00:00"