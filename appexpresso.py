import streamlit as st
import joblib
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load('model.joblib')

# Fonction pour prédire le désabonnement
def predict_churn(features):
    return model.predict([features])

# Titre de l'application
st.title("Prédiction de Désabonnement des Clients Expresso")

# Formulaire pour saisir les caractéristiques des clients
st.header("Informations sur le client")

# Ajoutez les champs nécessaires pour recueillir les données des clients
region = st.number_input('Région (REGION)', min_value=0, max_value=10, step=1)
tenure = st.number_input('Ancienneté (TENURE)', min_value=0, step=1)
montant = st.number_input('Montant (MONTANT)', min_value=0.0)
frequence_rech = st.number_input('Fréquence des recharges (FREQUENCE_RECH)', min_value=0.0)
revenue = st.number_input('Revenu (REVENUE)', min_value=0.0)
arpu_segment = st.number_input('ARPU Segment (ARPU_SEGMENT)', min_value=0.0)
frequence = st.number_input('Fréquence (FREQUENCE)', min_value=0.0)
data_volume = st.number_input('Volume de données (DATA_VOLUME)', min_value=0.0)
on_net = st.number_input('On Net (ON_NET)', min_value=0.0)
orange = st.number_input('Orange (ORANGE)', min_value=0.0)
tigo = st.number_input('Tigo (TIGO)', min_value=0.0)
zone1 = st.number_input('Zone 1 (ZONE1)', min_value=0.0)
zone2 = st.number_input('Zone 2 (ZONE2)', min_value=0.0)
mrg = st.number_input('MRG (MRG)', min_value=0, step=1)
regularity = st.number_input('Régularité (REGULARITY)', min_value=0, step=1)
top_pack = st.number_input('Top Pack (TOP_PACK)', min_value=0, step=1)
freq_top_pack = st.number_input('Fréquence du Top Pack (FREQ_TOP_PACK)', min_value=0.0)

# Rassemblez toutes les entrées de l'utilisateur
features = [region, tenure, montant, frequence_rech, revenue, arpu_segment, frequence, data_volume, on_net, orange, tigo, zone1, zone2, mrg, regularity, top_pack, freq_top_pack]

# Bouton pour soumettre le formulaire
if st.button("Prédire"):
    prediction = predict_churn(features)
    if prediction[0] == 1:
        st.write("Le client est susceptible de se désabonner.")
    else:
        st.write("Le client n'est pas susceptible de se désabonner.")
