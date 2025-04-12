from dataclasses import dataclass

@dataclass
class Produkt:
    name: str
    price: str
    link: str
    desc: str
    kategoria: str
    ocena: float

produkty = {
    "mieszana": {
        "Kobieta": [
            Produkt(
                name="EstGen Krem nawilżający z zieloną herbatą",
                price="ok. 79,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Lekki krem nawilżający, reguluje sebum i nawilża skórę.",
                kategoria="Krem",
                ocena=4.7
            ),
            Produkt(
                name="Larens Serum z kwasem hialuronowym",
                price="ok. 99,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Serum nawilżające, poprawia koloryt skóry.",
                kategoria="Serum",
                ocena=4.8
            ),
            Produkt(
                name="Apis Żel oczyszczający z aloesem",
                price="ok. 45,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Delikatny żel oczyszczający, nie wysusza skóry.",
                kategoria="Żel",
                ocena=4.6
            )
        ],
        "Mężczyzna": [
            Produkt(
                name="EstGen Krem nawilżający z zieloną herbatą",
                price="ok. 79,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Lekki krem nawilżający, reguluje sebum i nawilża skórę.",
                kategoria="Krem",
                ocena=4.7
            ),
            Produkt(
                name="Larens Serum z kwasem hialuronowym",
                price="ok. 99,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Serum nawilżające, poprawia koloryt skóry.",
                kategoria="Serum",
                ocena=4.8
            ),
            Produkt(
                name="Apis Żel oczyszczający z aloesem",
                price="ok. 45,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Delikatny żel oczyszczający, nie wysusza skóry.",
                kategoria="Żel",
                ocena=4.6
            )
        ]
    },
    "naczynkowa": {
        "Kobieta": [
            Produkt(
                name="EstGen Krem z kasztanowcem",
                price="ok. 89,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Wzmacnia naczynka, redukuje zaczerwienienia.",
                kategoria="Krem",
                ocena=4.9
            ),
            Produkt(
                name="Larens Ampułki z witaminą K",
                price="ok. 120,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Wzmacnia naczynia, redukuje pajączki.",
                kategoria="Ampułki",
                ocena=5.0
            ),
            Produkt(
                name="Apis Maska kojąca z arniką",
                price="ok. 55,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Łagodzi podrażnienia, wzmacnia naczynia krwionośne.",
                kategoria="Maska",
                ocena=4.7
            )
        ],
        "Mężczyzna": [
            Produkt(
                name="EstGen Krem z kasztanowcem",
                price="ok. 89,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Wzmacnia naczynka, redukuje zaczerwienienia.",
                kategoria="Krem",
                ocena=4.9
            ),
            Produkt(
                name="Larens Ampułki z witaminą K",
                price="ok. 120,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Wzmacnia naczynia, redukuje pajączki.",
                kategoria="Ampułki",
                ocena=5.0
            ),
            Produkt(
                name="Apis Maska kojąca z arniką",
                price="ok. 55,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Łagodzi podrażnienia, wzmacnia naczynia krwionośne.",
                kategoria="Maska",
                ocena=4.7
            )
        ]
    },
    "normalna": {
        "Kobieta": [
            Produkt(
                name="EstGen Krem nawilżający z SPF 15",
                price="ok. 85,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem nawilżający, chroniący przed promieniowaniem UV.",
                kategoria="Krem",
                ocena=4.7
            ),
            Produkt(
                name="Larens Tonik nawilżający z ogórkiem",
                price="ok. 50,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Tonik nawilżający, odświeżający.",
                kategoria="Tonik",
                ocena=4.6
            ),
            Produkt(
                name="Apis Peeling enzymatyczny",
                price="ok. 60,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Delikatny peeling enzymatyczny, usuwający martwe komórki.",
                kategoria="Peeling",
                ocena=4.8
            )
        ],
        "Mężczyzna": [
            Produkt(
                name="EstGen Krem nawilżający z SPF 15",
                price="ok. 85,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem nawilżający, chroniący przed promieniowaniem UV.",
                kategoria="Krem",
                ocena=4.7
            ),
            Produkt(
                name="Larens Tonik nawilżający z ogórkiem",
                price="ok. 50,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Tonik nawilżający, odświeżający.",
                kategoria="Tonik",
                ocena=4.6
            ),
            Produkt(
                name="Apis Peeling enzymatyczny",
                price="ok. 60,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Delikatny peeling enzymatyczny, usuwający martwe komórki.",
                kategoria="Peeling",
                ocena=4.8
            )
        ]
    },
    "sucha": {
        "Kobieta": [
            Produkt(
                name="EstGen Krem nawilżający z masłem shea",
                price="ok. 95,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem z masłem shea, wzmacnia barierę lipidową.",
                kategoria="Krem",
                ocena=4.8
            ),
            Produkt(
                name="Larens Serum regenerujące z olejem arganowym",
                price="ok. 120,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Serum regenerujące, przywraca elastyczność skóry.",
                kategoria="Serum",
                ocena=4.9
            ),
            Produkt(
                name="Apis Krem odżywczy z witaminą E",
                price="ok. 70,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem odżywczy, głęboko nawilża i regeneruje.",
                kategoria="Krem",
                ocena=4.7
            )
        ],
        "Mężczyzna": [
            Produkt(
                name="EstGen Krem nawilżający z masłem shea",
                price="ok. 95,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem z masłem shea, wzmacnia barierę lipidową.",
                kategoria="Krem",
                ocena=4.8
            ),
            Produkt(
                name="Larens Serum regenerujące z olejem arganowym",
                price="ok. 120,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Serum regenerujące, przywraca elastyczność skóry.",
                kategoria="Serum",
                ocena=4.9
            ),
            Produkt(
                name="Apis Krem odżywczy z witaminą E",
                price="ok. 70,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem odżywczy, głęboko nawilża i regeneruje.",
                kategoria="Krem",
                ocena=4.7
            )
        ]
    },
    "tlusta": {
        "Kobieta": [
            Produkt(
                name="EstGen Żel oczyszczający z kwasem salicylowym",
                price="ok. 69,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Żel oczyszczający, reguluje wydzielanie sebum.",
                kategoria="Żel",
                ocena=4.7
            ),
            Produkt(
                name="Larens Krem matujący z ekstraktem z drzewa herbacianego",
                price="ok. 85,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem matujący, kontroluje błyszczenie.",
                kategoria="Krem",
                ocena=4.8
            ),
            Produkt(
                name="Apis Tonik ściągający z zieloną herbatą",
                price="ok. 55,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Tonik ściągający, redukuje nadmiar sebum.",
                kategoria="Tonik",
                ocena=4.6
            )
        ],
        "Mężczyzna": [
            Produkt(
                name="EstGen Żel oczyszczający z kwasem salicylowym",
                price="ok. 69,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Żel oczyszczający, reguluje wydzielanie sebum.",
                kategoria="Żel",
                ocena=4.7
            ),
            Produkt(
                name="Larens Krem matujący z ekstraktem z drzewa herbacianego",
                price="ok. 85,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Krem matujący, kontroluje błyszczenie.",
                kategoria="Krem",
                ocena=4.8
            ),
            Produkt(
                name="Apis Tonik ściągający z zieloną herbatą",
                price="ok. 55,00 zł",
                link="https://www.ceneo.pl/xyz",
                desc="Tonik ściągający, redukuje nadmiar sebum.",
                kategoria="Tonik",
                ocena=4.6
            )
        ]
    }
}
