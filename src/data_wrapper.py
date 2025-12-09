import pandas as pd
from pyspectra.readers.read_spc import read_spc,read_spc_dir
import matplotlib.pyplot as plt
from time_function import *


"""Dans la suite tout nos données seront préparés grâce à nos data_wrapper
sous la forme d'un DataFrame avec le format suivant : 
        Temps de culture (en h) T°C pH PO2 dissout A600nm Glucose Ethanol 200 201 .... 2400 """

def data_wrapper_j1():
    
    #on prend que  les lignes qui contiennent de l'information
    df_données_brut=pd.read_excel('C:\\Users\\antod\Desktop\\ei_st4_levures\\excel\\240604.xlsx')
    df_donnee_pair=df_données_brut.iloc[::2] 
    col=df_donnee_pair.columns[:3]
    df_donnee_pair=df_donnee_pair.drop(columns=col)
    df_donnee=df_donnee_pair.set_index('Heure',drop=True)
    #on prend que la partie correspondant à l'heure comme nom d'index
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j1_2024')
    df_spc.index=df_spc.index.str[34:40]
    df_spc.index=df_spc.index.map(convertir_heure)

    #on va créer une boucle qui va sélectionner les heures les plus proches des heures de mesures hors-lignes
    data1=[]
    label1=[]
    for h in df_donnee.index:
        data1.append(df_spc.loc[heure_plus_proche(h,df_spc.index)])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    #on ajoute une dernière colonne à notre dataframe pour obtenir les données d'entraînement

    df=pd.concat([df_donnee,df_spc_filtre],axis=1)
    df.loc[df['Glucose']=='< 0.2','Glucose']=0
    return df

def data_wrapper_j2():
    #on prend que  les lignes qui contiennent de l'information
    df_données_brut=pd.read_excel('C:\\Users\\antod\Desktop\\ei_st4_levures\\excel\\240605.xlsx') #chemin d'accés à spécifier en fonction de l'organistation des données
    df_donnee_pair=df_données_brut.iloc[::2] 
    col=df_donnee_pair.columns[:3]
    df_donnee_pair=df_donnee_pair.drop(columns=col)
    df_donnee=df_donnee_pair.set_index('Heure',drop=True)
    #on prend que la partie correspondant à l'heure comme nom d'index
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j2_2024')
    df_spc.index=df_spc.index.str[34:40]
    df_spc.index=df_spc.index.map(convertir_heure)

    #on va créer une boucle qui va sélectionner les heures les plus proches des heures de mesures hors-lignes
    data1=[]
    label1=[]
    for h in df_donnee.index:
        data1.append(df_spc.loc[heure_plus_proche(h,df_spc.index)])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    #on ajoute une dernière colonne à notre dataframe pour obtenir les données d'entraînement

    df=pd.concat([df_donnee,df_spc_filtre],axis=1)
    df.loc[df['Glucose']=='< 0.2','Glucose']=0
    col7=df.columns[7]
    df.drop(columns=col7,inplace=True)
    return df
def data_wrapper_j3():
    #on prend que  les lignes qui contiennent de l'information
    df_données_brut=pd.read_excel('C:\\Users\\antod\Desktop\\ei_st4_levures\\excel\\250603.xlsx')
    df_donnee_pair=df_données_brut.iloc[::2] 
    col=df_donnee_pair.columns[:3]
    df_donnee_pair=df_donnee_pair.drop(columns=col)
    df_donnee=df_donnee_pair.set_index('Heure',drop=True)
    #on prend que la partie correspondant à l'heure comme nom d'index
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j1_2025')
    df_spc.index=df_spc.index.str[33:39]
    df_spc.index=df_spc.index.map(convertir_heure)

    #on va créer une boucle qui va sélectionner les heures les plus proches des heures de mesures hors-lignes
    data1=[]
    label1=[]
    for h in df_donnee.index:
        data1.append(df_spc.loc[heure_plus_proche(h,df_spc.index)])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    #on ajoute une dernière colonne à notre dataframe pour obtenir les données d'entraînement

    df=pd.concat([df_donnee,df_spc_filtre],axis=1)
    df.loc[df['Glucose']=='< 0.2','Glucose']=0
    col7=df.columns[7]
    return df


def data_wrapper_j4():
    #on prend que  les lignes qui contiennent de l'information
    df_données_brut=pd.read_excel('C:\\Users\\antod\Desktop\\ei_st4_levures\\excel\\250604.xlsx')
    df_donnee_pair=df_données_brut.iloc[::2] 
    col=df_donnee_pair.columns[:3]
    df_donnee_pair=df_donnee_pair.drop(columns=col)
    df_donnee=df_donnee_pair.set_index('Heure',drop=True)
    #on prend que la partie correspondant à l'heure comme nom d'index
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j2_2025')
    df_spc.index=df_spc.index.str[33:39]
    df_spc.index=df_spc.index.map(convertir_heure)

    #on va créer une boucle qui va sélectionner les heures les plus proches des heures de mesures hors-lignes
    data1=[]
    label1=[]
    for h in df_donnee.index:
        data1.append(df_spc.loc[heure_plus_proche(h,df_spc.index)])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    #on ajoute une dernière colonne à notre dataframe pour obtenir les données d'entraînement

    df=pd.concat([df_donnee,df_spc_filtre],axis=1)
    df.loc[df['Glucose']=='< 0.2','Glucose']=0
    
    return df

def data_wrapper_all_spc_j3():
    "fonction qui permet de récupérer tout les spectres Raman"
    "\ d'une journée et de les transformer en DataFrame "
    "\avec l'heure de mesure en Index, chaque colonne correspond au nombre d'onde du spectre"
    "\Enfin l'intensité du spectre est l'information dans le DataFrame"
    "Le DataFrame est organisé de la façon suivante : "
    "            200    201   .... 2400"
    "  Heure     12341  6024  .... 531     "
    
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j1_2025')
    df_spc.index=df_spc.index.str[33:39]
    df_spc.index=df_spc.index.map(convertir_heure)
    data1=[]
    label1=[]
    for h in df_spc.index:
        data1.append(df_spc.loc[h])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    return df_spc_filtre

def data_wrapper_all_spc_j4():
    "fonction qui permet de récupérer tout les spectres Raman"
    "\ d'une journée et de les transformer en DataFrame "
    "\avec l'heure de mesure en Index, chaque colonne correspond au nombre d'onde du spectre"
    "\Enfin l'intensité du spectre est l'information dans le DataFrame"
    "Le DataFrame est organisé de la façon suivante : "
    "            200    201   .... 2400"
    "  Heure     12341  6024  .... 531     "
    
    df_spc,dict_spc=read_spc_dir('C:\\Users\\antod\Desktop\\ei_st4_levures\\data\\data_j2_2025')
    df_spc.index=df_spc.index.str[33:39]
    df_spc.index=df_spc.index.map(convertir_heure)
    data1=[]
    label1=[]
    for h in df_spc.index:
        data1.append(df_spc.loc[h])
        label1.append(h)
    df_spc_filtre=pd.DataFrame(data1,label1)
    return df_spc_filtre


def convertir_heure(heure):
    """ Fonction pour convertir le format HHMMSS en 'HH:MM:SS'"""
    return f"{heure[:2]}:{heure[2:4]}:{heure[4:6]}"



#test unitaire de la fonction heure_plus_proche
liste_heures = ["00:00:00", "06:00:00", "12:00:00", "18:00:00", "23:59:59"]
assert heure_plus_proche(time(0, 5, 0), liste_heures) == "00:00:00"

if __name__=='__main__':
    df2=data_wrapper_j2()
    df1=data_wrapper_j1()
    df3=data_wrapper_j3()
    df4=data_wrapper_j4()
    df5=data_wrapper_all_spc_j3()
    df6=data_wrapper_all_spc_j4()
    print(df5)
    
        #test unitaire de la fonction heure_plus_proche
    liste_heures = ["00:00:00", "06:00:00", "12:00:00", "18:00:00", "23:59:59"]
    assert heure_plus_proche(time(0, 5, 0), liste_heures) == "00:00:00"



