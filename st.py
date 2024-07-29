import streamlit as st
import numpy as np
import joblib

# Chargez votre modèle pré-entraîné avec joblib
model = joblib.load('model.joblib')

# Fonction pour effectuer la prédiction
def predict_depreciation(car_age, present_price, kms_driven, fuel_type, seller_type, transmission):
    # Prétraitement des entrées de l'utilisateur pour correspondre à ce que le modèle attend
    fuel_dict = {'Diesel': 0, 'Petrol': 1}
    seller_dict = {'Dealer': 0, 'Individual': 1}
    transmission_dict = {'Automatic': 0, 'Manual': 1}

    fuel_type = fuel_dict[fuel_type]
    seller_type = seller_dict[seller_type]
    transmission = transmission_dict[transmission]

    # Création de l'array d'entrée pour la prédiction
    inputs = np.array([[car_age, present_price, kms_driven, fuel_type, seller_type, transmission]])
    
    # Faire la prédiction
    prediction = model.predict(inputs)
    return prediction[0]

# Titre de l'application
st.title('Prédiction de la Dépréciation des Voitures d\'Occasion')

# Champs de saisie des caractéristiques de la voiture
car_age = st.number_input('Âge de la voiture (en années)', min_value=0, max_value=100, value=5)
present_price = st.number_input('Prix actuel (en milliers de $)', min_value=0.0, max_value=1000.0, value=10.0)
kms_driven = st.number_input('Kilomètres parcourus', min_value=0, max_value=1000000, value=50000)
fuel_type = st.selectbox('Type de carburant', ['Diesel', 'Petrol'])
seller_type = st.selectbox('Type de vendeur', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', ['Automatic', 'Manual'])

# Bouton pour effectuer la prédiction
if st.button('Prédire la Dépréciation'):
    prediction = predict_depreciation(car_age, present_price, kms_driven, fuel_type, seller_type, transmission)
    st.write(f'La valeur de dépréciation prédite pour cette voiture est de ${prediction:.2f}k')

# Pour exécuter l'application, utilisez la commande suivante dans le terminal :
# streamlit run app.py
