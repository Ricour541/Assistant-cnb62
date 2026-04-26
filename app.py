import streamlit as st

st.title("Assistant de Navigation CNB62")

st.header("⚙️ Paramètres de navigation")

# Zones de saisie pour vos chiffres
dist = st.number_input("Distance à parcourir (milles)", value=10.0)
vit = st.number_input("Vitesse surface (nœuds)", value=5.0)

st.divider() # Une jolie ligne de séparation

# Le calcul automatique
if vit > 0:
    temps = dist / vit
    # Affichage du résultat en gros
    st.success(f"⏱️ Temps estimé : {temps:.2f} heures")
    
    # Un petit bonus pour le vent (votre texte de tout à l'heure)
    st.info("Note : N'oubliez pas de vérifier la force du vent avant de partir.")
else:
    st.error("La vitesse doit être supérieure à 0 pour calculer le temps.")
