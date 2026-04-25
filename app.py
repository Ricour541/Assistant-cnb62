import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Assistant CNB 62", page_icon="⚓")

st.title("⚓ Assistant de Routage CNB 62")

# --- INTERFACE ---
st.header("Conditions de Navigation")
vent = st.slider("Force du vent (nœuds)", 0, 50, 15)
mer = st.slider("Hauteur de la mer (mètres)", 0.0, 6.0, 1.0, 0.5)

# --- CALCUL SIMPLIFIÉ (Sans outils externes) ---
# Une formule simple pour estimer la vitesse du CNB 62
vitesse_base = vent * 0.45
if mer > 2.0:
    vitesse_base -= (mer * 0.5)

vitesse_finale = max(0.0, min(vitesse_base, 12.0))

# --- VERDICT ---
st.subheader("Analyse du Capitaine")

if vent > 35 or mer > 4.0:
    st.error("⚠️ CONDITIONS DANGEREUSES : Restez au port ou cherchez un abri !")
elif vent > 25:
    st.warning("⛵ Navigation sportive : Réduire la voilure (Ris 2 ou 3).")
else:
    st.success("✅ Conditions favorables pour le CNB 62.")

st.metric("Vitesse estimée", f"{vitesse_finale:.1f} nœuds")
