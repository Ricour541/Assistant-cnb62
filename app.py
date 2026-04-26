import streamlit as st
from datetime import datetime, time

st.title("🛰️ Routeur Stratégique CNB62")

# --- SECTION 1 : TEMPS ---
st.header("📅 Planification du départ")
col1, col2 = st.columns(2)
with col1:
    date_depart = st.date_input("Date de départ", datetime.now())
with col2:
    heure_depart = st.time_input("Heure de départ (UTC)", time(10, 0))

# --- SECTION 2 : GÉOGRAPHIE ---
st.header("📍 Itinéraire")
col3, col4 = st.columns(2)
with col3:
    st.subheader("Départ")
    lat_dep = st.number_input("Latitude Départ", value=50.521, format="%.3f")
    lon_dep = st.number_input("Longitude Départ", value=1.583, format="%.3f")
with col4:
    st.subheader("Arrivée")
    lat_arr = st.number_input("Latitude Arrivée", value=51.125, format="%.3f")
    lon_arr = st.number_input("Longitude Arrivée", value=1.333, format="%.3f")

# --- SECTION 3 : VOS SOUHAITS ---
st.header("⛵ Vos souhaits de navigation")
confort = st.select_slider(
    "Niveau de confort souhaité",
    options=["Performance (Direct)", "Équilibré", "Confort (Éviter la mer forte)"]
)

vent_max = st.slider("Force du vent maximum acceptée (nœuds)", 10, 45, 25)

# Bouton pour lancer le calcul (on créera la logique après)
if st.button("Lancer l'analyse météo et le routage"):
    st.info(f"Analyse prévue pour le {date_depart} à {heure_depart}...")
    st.warning("Étape suivante : Connexion aux serveurs météo (API).")
