import streamlit as st
with st.sidebar:
    # INFORMATIONS PERSONNELLES
    st.header(" Informations personnelles")
    st.write("**Nom :Awa Souare")
    st.write("**Date de Naissance :** 24/01/03 ")
    st.write("**Email :**awasouare158@gmail.com")
    st.write("**Téléphone :**+221 77 165 45 91")
    st.write("**Adresse :** Sénégal")

# PROFIL
st.header(" profil")
st.write("""
Jeune bacheliére motivée, actuellement en formation en géomatique.
Passionnée par les systémes d'information géographiques (SIG),
la cartographie et la programmation en python.
""")

# FORMATION
st.header(" Formation")
st.write("**2025 : Baccalauriat**")
st.write("**2025 - Présent :Formation en Géomatique**")

# COMPETENCES TECHNIQUES
st.header(" Compétences")
st.write("-Programmation (Python)")
st.write("-Technique de Base de la Géographie(QGIS, ArcGIS)")
st.write("-Topographie(Excel)")
st.write("-Base de Donnée(Pandas / Geopandas,PostGIS,PostGres)")
st.write("-Cartographie(Excel,QGIS)")

# PROJETS ACADEMIQUES
st.header(" projets")
st.write("-Application IMC avec Streamlit")
st.write("-Manipulation de données spatiales avec Geopandas")
st.write("-Analyse cartographique")

# LANGUES
st.header(" Langues")
st.write("-Français")
st.write("-Anglais (niveau intermédiaire)")

st.write("---")
st.write("CV créé avec Streamlit ")
