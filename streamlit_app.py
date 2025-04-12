
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import time
from produkty import produkty, Produkt

# Stałe
IMG_SIZE = (224, 224)
CLASS_NAMES = ['mieszana', 'naczynkowa', 'normalna', 'sucha', 'tlusta']

st.set_page_config(page_title="Klasyfikator Typu Skóry", layout="centered")

# Wczytywanie modelu
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

# Rekomendacje ogólne
def rekomendacja_pielegnacji(top1, score1, top2, score2, gender, age):
    tekst = f"**Twoja cera wykazuje cechy typu: {top1.capitalize()} ({int(score1 * 100)}%)**.\n\n"
    if abs(score1 - score2) < 0.15 and top2 != top1:
        tekst += f"Dodatkowo widoczne są cechy typu: **{top2.capitalize()} ({int(score2 * 100)}%)**.\n\n"

    opisy = {
        'tlusta': "Błyszczenie, zaskórniki i przetłuszczanie to typowe objawy skóry tłustej.",
        'sucha': "Suchość, szorstkość i uczucie ściągnięcia to cechy skóry suchej.",
        'mieszana': "Skóra przetłuszcza się w strefie T, ale bywa sucha na policzkach.",
        'normalna': "Zrównoważona, elastyczna skóra — ale wciąż potrzebuje pielęgnacji.",
        'naczynkowa': "Zaczerwienienia, wrażliwość i widoczne naczynka to typowe objawy."
    }
    tekst += f"{opisy.get(top1, '')}\n\n"

    if gender == "Mężczyzna":
        tekst += "🧔 Dla mężczyzn polecam łagodne kosmetyki bezzapachowe i produkty po goleniu bez alkoholu.\n\n"
    else:
        tekst += "💄 Zadbaj o dokładny demakijaż i łagodną pielęgnację, dopasowaną do typu cery.\n\n"

    if age < 25:
        tekst += "🧴 W młodym wieku postaw na lekkość, matowienie i regularne oczyszczanie.\n"
    elif age <= 40:
        tekst += "🌿 Buduj świadomą rutynę pielęgnacyjną — serum, krem i SPF codziennie.\n"
    else:
        tekst += "🌟 Skóra dojrzała wymaga regeneracji, antyoksydantów i ceramidów.\n"

    tekst += "\n### 📝 **Jak stosować produkty:**\n"
    tekst += "- Regularność jest kluczem – aplikuj produkty zgodnie z instrukcjami.\n"
    tekst += "- Rano i wieczorem staraj się stosować odpowiedni krem nawilżający i serum.\n"
    tekst += "- W przypadku produktów z SPF, nakładaj je na dzień, a wieczorem skup się na regeneracji skóry."

    return tekst

# Interfejs
st.title("🧴 Klasyfikator Typu Skóry")
st.info("📷 Wgraj zdjęcie lub użyj kamery – po analizie otrzymasz typ skóry oraz rekomendacje dopasowane do Ciebie.")

gender = st.radio("👤 Wybierz płeć", ["Kobieta", "Mężczyzna"], horizontal=True)
age = st.slider("🎂 Wiek", 15, 80, 30)

placeholder = st.empty()

with placeholder.container():
    uploaded_file = st.file_uploader("Wybierz plik", type=["jpg", "jpeg", "png"])
    camera_image = st.camera_input("Zrób zdjęcie kamerą")

img_data = uploaded_file or camera_image

if img_data:
    img = Image.open(img_data)

    with placeholder.container():
        st.image(img, caption="📸 Twoje zdjęcie", use_container_width=True)
        st.write("🔬 Analizuję cerę...")
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.005)

    predictions = predict_image(img)
    top_indices = np.argsort(predictions)[::-1]
    top1, top2 = CLASS_NAMES[top_indices[0]], CLASS_NAMES[top_indices[1]]
    score1, score2 = predictions[top_indices[0]], predictions[top_indices[1]]

    with placeholder.container():
        st.image(img, caption="📸 Twoje zdjęcie", use_container_width=True)
        st.markdown("### 📊 **Prawdopodobieństwa typów skóry:**")
        for idx in top_indices:
            st.write(f"- **{CLASS_NAMES[idx].capitalize()}**: {predictions[idx] * 100:.2f}%")

        st.markdown("---")
        st.markdown("### 📝 **Rekomendacje pielęgnacyjne:**")
        rec = rekomendacja_pielegnacji(top1, score1, top2, score2, gender, age)
        st.markdown(rec)

        st.markdown("---")
        st.markdown("### 🛍️ **Proponowane produkty pielęgnacyjne:**")
        produkty_dla_uzytkownika = produkty.get(top1, {}).get(gender, [])
        for produkt in produkty_dla_uzytkownika:
            with st.expander(f"💄 {produkt.name}"):
                st.markdown(f"💰 **{produkt.price}**")
                st.markdown(f"🧴 {produkt.desc}")
                st.markdown(f"[🔗 Zobacz produkt]({produkt.link})")
                st.markdown(f"🏷️ Kategoria: {produkt.kategoria}")
                st.markdown(f"⭐ Ocena: {produkt.ocena}/5")
                st.markdown(f"💡 **Jak stosować**: Aplikuj produkt na oczyszczoną skórę 2 razy dziennie (rano i wieczorem).")

        if st.button("❌ Zamknij wynik / wróć"):
            st.rerun()
