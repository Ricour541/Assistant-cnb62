import streamlit as st

# Configuration
st.set_page_config(page_title="Routage CNB 62", page_icon="⛵")

st.title("⚓ Assistant de Navigation CNB 62")

# --- PANNEAU LATÉRAL (Réglages) ---
st.sidebar.header("Paramètres du Trajet")
distance = st.sidebar.number_input("Distance à parcourir (milles)", min_value=1.0, value=50.0)
allure = st.sidebar.selectbox("Allure du bateau", 
    ["Près (45°)", "Bon plein (60°)", "Travers (90°)", "Largue (120°)", "Vent arrière (150°+)"])

# --- INTERFACE PRINCIPALE ---
col1, col2 = st.columns(2)
with col1:
    vent = st.slider("Force du vent (nds)", 0, 50, 15)
with col2:
    mer = st.slider("Hauteur mer (m)", 0.0, 6.0, 1.0, 0.5)

# --- CALCUL DES PERFORMANCES (Polaires simplifiées) ---
# Multiplicateur selon l'allure
coeffs_allure = {
    "Près (45°)": 0.35,
    "Bon plein (60°)": 0.48,
    "Travers (90°)": 0.55,
    "Largue (120°)": 0.52,
    "Vent arrière (150°+)": 0.40
}

vitesse_theo = vent * coeffs_allure[allure]

# Impact de la mer (freinage)
frein_mer = mer * 0.4
vitesse_reelle = max(1.5, vitesse_theo - frein_mer)
if vitesse_reelle > 12.5: vitesse_reelle = 12.5 # Vitesse max théorique

# Calcul du temps
temps_decimal = distance / vitesse_reelle
heures = int(temps_decimal)
minutes = int((temps_decimal - heures) * 60)

# --- AFFICHAGE DU ROUTAGE ---
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Vitesse Surface", f"{vitesse_reelle:.1f} kts")
c2.metric("Distance", f"{distance} nm")
c3.metric("Temps estimé", f"{heures}h {minutes}min")

# --- CONSEILS DE SÉCURITÉ ---
if vent > 30 or mer > 3.5:
    st.error("⚠️ ALERTE : Conditions musclées. Réduire la toile (2 ris minimum).")
elif vent < 8:
    st.info("ℹ️ Vent faible : Appui moteur probable pour maintenir la moyenne.")
else:
    st.success("✅ Bonne navigation prévue !")
