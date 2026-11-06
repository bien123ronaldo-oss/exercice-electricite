from pathlib import Path

import pandas as pd
import streamlit as st

DOSSIER = Path(__file__).parent / "donnees"

st.set_page_config(page_title="L'électricité dans 12 quartiers", page_icon="⚡", layout="wide")

st.title("L'électricité dans 12 quartiers")
st.caption("Relevés mensuels de janvier 2024 à décembre 2025. Données fictives.")

@st.cache_data
def charger():
    return pd.read_csv(DOSSIER / "consommation_propre.csv")


df = charger()

st.write(
    "Ce tableau de bord répond à une question du directeur : la consommation "
    "suit-elle la chaleur, ou les heures de courant ?"
)
st.write(f"Le fichier propre compte {len(df)} lignes.")

communes = sorted(df["commune"].unique())
choix = st.sidebar.multiselect("Communes", communes, default=communes)

annees = sorted(df["annee"].unique())
annee = st.sidebar.selectbox("Année", annees, index=len(annees) - 1)

if not choix:
    st.warning("Choisissez au moins une commune.")
    st.stop()

filtre = df[(df["commune"].isin(choix)) & (df["annee"] == annee)]