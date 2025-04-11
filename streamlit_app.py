# streamlit_app.py

import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# Stałe
IMG_SIZE = (224, 224)
CLASS_NAMES = ['mieszana', 'naczynkowa', 'normalna', 'sucha', 'tlusta']

# Ustawienia aplikacji
st.set_page_config(page_title="Skin Type Classifier", layout="centered")
st.title("🧴 Klasyfikator Typu Skóry")

# 🛡️ Informacja o prywatności
st.markdown(
    """
    🔒 **Prywatność:**  
    Aplikacja nie zapisuje, nie przechowuje i nie przesyła Twoich zdjęć.  
    Wszystkie obrazy są przetwarzane wyłącznie lokalnie (w pamięci przeglądarki) i usuwane po analizie.
    Możesz bezpiecznie korzystać z uploadu lub kamery.
    """,
    unsafe_allow_html=True
)

# Ładowanie modelu
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("skin_model.keras")

model = load_model()

# Predykcja
def predict_image(img):
    img = img.convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    preds = model.predict(img_array)[0]
    return preds

# Upload lub kamera
uploaded_file = st.file_uploader("📷 Wgraj zdjęcie", type=["jpg", "jpeg", "png"])
camera_image = st.camera_input("📸 Lub zrób zdjęcie kamerą")

# Przetwarzanie
img_data = uploaded_file or camera_image

if img_data:
    img = Image.open(img_data)
    st.image(img, caption='Wczytane zdjęcie', use_container_width=True)

    with st.spinner('🔍 Analizuję...'):
        predictions = predict_image(img)
        predicted_class = CLASS_NAMES[np.argmax(predictions)]

    st.success(f"🎯 **Predykcja:** `{predicted_class.upper()}`")

    st.subheader("📊 Prawdopodobieństwa klas:")
    for i, prob in enumerate(predictions):
        st.write(f"- {CLASS_NAMES[i]}: {prob * 100:.2f}%")
