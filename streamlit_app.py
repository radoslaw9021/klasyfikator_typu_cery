import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

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

# Placeholder na dynamiczną zmianę treści
placeholder = st.empty()
uploaded_file = None
camera_image = None

# Krok 1: upload lub kamera
with placeholder.container():
    st.markdown("### 📥 Wgraj zdjęcie lub użyj kamery:")
    uploaded_file = st.file_uploader("Wybierz plik JPG/PNG", type=["jpg", "jpeg", "png"])
    camera_image = st.camera_input("Lub zrób zdjęcie", key="camera")

img_data = uploaded_file or camera_image

# Krok 2: jeśli zdjęcie wgrane → pokaż wynik w tym samym miejscu
if img_data:
    img = Image.open(img_data)
    with st.spinner("🔍 Analizuję zdjęcie..."):
        predictions = predict_image(img)
        predicted_class = CLASS_NAMES[np.argmax(predictions)]

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
            st.rerun()  # ✅ Nowa poprawna wersja!
