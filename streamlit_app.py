import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import time

# Konfiguracja aplikacji
IMG_SIZE = (224, 224)
CLASS_NAMES = ['mieszana', 'naczynkowa', 'normalna', 'sucha', 'tlusta']
st.set_page_config(page_title="Klasyfikator Typu Skóry", layout="centered")

# Nagłówek i wstęp
st.markdown(
    """
    ## 👤 Klasyfikator typu skóry

    🤖 Aplikacja korzysta ze sztucznej inteligencji, **wytrenowanej przeze mnie na bazie zdjęć różnych typów cery**.

    📸 Wystarczy, że **zrobisz selfie lub wgrasz swoje zdjęcie**, a model spróbuje określić Twój typ skóry.

    🧪 To nie jest porada medyczna — bardziej **zabawa z AI i technologią pielęgnacyjną** ✨

    ### 💆‍♀️ Możliwe typy skóry:

    - 🌀 **Mieszana** – przetłuszczająca się w strefie T, sucha na policzkach  
    - 🌿 **Normalna** – zrównoważona, bez wyraźnych problemów  
    - 💢 **Naczynkowa** – zaczerwienienia, widoczne naczynka  
    - 🧊 **Sucha** – uczucie ściągnięcia, matowa  
    - ✨ **Tłusta** – błyszcząca, z tendencją do wyprysków  

    ---
    """,
    unsafe_allow_html=True
)

# Informacja o prywatności
st.info(
    "📷 **Jak to działa?** \n"
    "Zrób zdjęcie twarzy (lub wgraj jedno), nakieruj kamerę na siebie i kliknij „Take Photo”.\n\n"
    "🔐 **Prywatność:** Twoje zdjęcia nie są zapisywane ani przesyłane — są przetwarzane tylko w Twojej przeglądarce i znikają po odświeżeniu.",
    icon="🔎"
)

# Wczytanie modelu
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("skin_model.keras")

model = load_model()

# Funkcja predykcji
def predict_image(img):
    img = img.convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    preds = model.predict(img_array)[0]
    return preds

# 📷 Lusterko + analiza w tym samym miejscu
placeholder = st.empty()

with placeholder.container():
    st.markdown("### 📷 Zrób zdjęcie kamerą lub wgraj plik:")
    uploaded_file = st.file_uploader("Wybierz plik", type=["jpg", "jpeg", "png"])
    camera_image = st.camera_input("Podgląd kamery – kliknij 'Take photo' gdy jesteś gotowy")

img_data = uploaded_file or camera_image

if img_data:
    img = Image.open(img_data)

    # 🔬 Efekt skanowania
    with placeholder.container():
        st.image(img, caption="📸 Zrobione zdjęcie", use_container_width=True)
        st.markdown("## 🔬 Skanuję cerę...")
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.01)

    # 🔍 Predykcja
    predictions = predict_image(img)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]

    # 🎯 Wynik
    with placeholder.container():
        st.image(img, caption="📸 Twoje zdjęcie", use_container_width=True)
        st.markdown(f"<h2 style='color:green; text-align:center;'>🎯 Twój typ skóry: {predicted_class.upper()}</h2>", unsafe_allow_html=True)

        st.markdown("### 📊 Prawdopodobieństwa klas:")
        max_index = np.argmax(predictions)

        for i, (typ, prob) in enumerate(zip(CLASS_NAMES, predictions)):
            procent = prob * 100
            if i == max_index:
                st.markdown(f"🎯 <span style='color:green; font-weight:bold;'>{typ.capitalize()}</span>: <strong>{procent:.2f}%</strong>", unsafe_allow_html=True)
            else:
                st.markdown(f"- <strong>{typ.capitalize()}</strong>: {procent:.2f}%", unsafe_allow_html=True)

        st.markdown("---")
        st.info("🧠 W przyszłości dobierzemy dla Twojego typu skóry spersonalizowaną profilaktykę pielęgnacyjną.")

        if st.button("❌ Zamknij wynik / wróć"):
            st.rerun()
