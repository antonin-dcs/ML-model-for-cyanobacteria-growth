#fonction qui permet de calculer l'aire sous un pic données 
def integrale(dataframe,borne_début,borne_fin):
    borne_début=int(borne_début)
    borne_fin=int(borne_fin)
    col_supp=dataframe.columns[:7]  # on sélectionne les colonnes à supprimer qui ne correspondent pas au spectre
    df_data=dataframe.drop(columns=col_supp)
    df_tranche=df_data.iloc[:, [i-200 for i in range(int(borne_début),int(borne_fin))]]
    #on va supprimer le trapèze en dessous du spectre
    df_x=df_data.iloc[:,borne_début-200]
    df_y=df_data.iloc[:,borne_fin-200]
    trapeze=(borne_fin-borne_début)*(df_x+df_y)/2
    return df_tranche.sum(axis=1)-trapeze
