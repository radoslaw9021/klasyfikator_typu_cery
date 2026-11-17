# Klasyfikator typu cery

Aplikacja w Streamlit, która ze zdjęcia twarzy rozpoznaje typ cery i podpowiada pielęgnację oraz produkty.

## Jak działa
1. Użytkownik wgrywa zdjęcie i podaje płeć oraz wiek.
2. Model CNN (Keras, wejście 224×224) zwraca prawdopodobieństwa dla 5 klas: **mieszana, naczynkowa, normalna, sucha, tłusta**.
3. Aplikacja pokazuje dominujący typ, a jeśli dwa typy mają zbliżony wynik (różnica < 15 p.p.), także drugi.
4. Na tej podstawie generuje zalecenia pielęgnacyjne dopasowane do płci i wieku oraz listę produktów (`produkty.py`).

## Uruchomienie
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Technologie
Python · TensorFlow/Keras · Streamlit · Pillow · NumPy

> Projekt edukacyjny z 2025 roku. Wynik modelu nie jest diagnozą dermatologiczną.
> Ten sam model wykorzystałem w aplikacji [BeautyAI](https://github.com/radoslaw9021/app_pro_wersja1).
