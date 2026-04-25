import os
os.system('pip install numpy scipy')
import streamlit as st
import numpy as np
from scipy.interpolate import interp2d

# Configuration de l'interface
st.set_page_config(page_title="CNB 62 Navigation", page_icon="⛵")
st.title("⚓ Assistant de Routage CNB 62")

# Polaires du CNB 62
twa_axis = [52, 60, 75, 90, 110, 120, 135, 150]
tws_axis = [4, 6, 8, 10, 12, 14, 16, 20, 24]
data_vitesse = [
    [4.24, 4.62, 4.91, 4.68, 4.80, 4.67, 4.11, 3.37],
    [5.87, 6.30, 6.63, 6.50, 6.69, 6.53, 5.83, 4.86],
    [7.17, 7.57, 7.89, 7.96, 8.22, 8.07, 7.33, 6.22],
    [8.10, 8.48, 8.80, 8.95, 9.29, 9.19, 8.54, 7.40],
    [8.74, 9.08, 9.37, 9.59, 9.91, 9.86, 9.42, 8.43],
    [9.22, 9.51, 9.75, 9.85, 10.38, 10.43, 9.99, 9.25],
    [9.46, 9.77, 10.05, 10.11, 10.75, 10.82, 10.47, 9.80],
    [9.62, 9.94, 10.38, 10.66, 11.23, 11.68, 11.53, 10.63],
    [9.68, 10.01, 10.53, 11.03, 11.65, 12.23, 12.70, 11.56]
]
vpp_func = interp2d(twa_axis, tws_axis, data_vitesse, kind='linear')

# Menu latéral
st.sidebar.header("🛡️ Paramètres de Sécurité")
lim_pres = st.sidebar.slider("Vent Max Près/Travers (kts)", 15, 30, 25)
lim_portant = st.sidebar.slider("Vent Max Largue (kts)", 20, 40, 30)
lim_mer = st.sidebar.slider("Mer Max (m)", 1.0, 5.0, 3.0)

# Saisie des conditions
st.header("🌦️ Conditions Prévues")
c1, c2, c3 = st.columns(3)
tws = c1.number_input("Vent Réel (kts)", value=18)
twa = c2.number_input("Angle du Vent (°)", value=130)
mer = c3.number_input("Vagues (m)", value=1.5)

# Calcul
vitesse = float(vpp_func(twa, tws))
dist = 95
t_dec = dist / vitesse

# Verdict
st.markdown("---")
if mer > lim_mer:
    st.error(f"⛔ MER TROP FORTE ({mer}m)")
elif twa <= 110 and tws > lim_pres:
    st.error(f"⛔ VENT TROP FORT ({tws}kt)")
elif twa > 110 and tws > lim_portant:
    st.error(f"⛔ VENT TROP FORT ({tws}kt)")
else:
    st.success("✅ CONDITIONS OK")
    st.metric("Vitesse estimée", f"{vitesse:.2f} kts")
    st.metric("Temps (pour 95mn)", f"{int(t_dec)}h {int((t_dec%1)*60)}min")
