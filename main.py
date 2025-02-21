from enum import Enum, auto


class Color(Enum):
    rouge = 0
    bleue = 1
    noir = 2
    blanche = 3
    verte = auto()


class Marque(Enum):
    dunlop = auto()
    michelin = auto()


class DimensionRoue(Enum):
    taille_16_pouces = auto()
    taille_17_pouces = auto()
    taille_18_pouces = auto()
    taille_28_pouces = auto()


class Roues:
    def __init__(self, nb_de_roue: int, marque_du_pneu: Marque):
        self.nombre = nb_de_roue
        self.dimension: DimensionRoue = DimensionRoue.taille_16_pouces
        self.marque: Marque = marque_du_pneu

class Vehicule:
    def __init__(self):
        self.color: Color = Color.blanche
        self.roues_du_vehicule: Roues or None = None


class Velo(Vehicule):
    def __init__(self):
        super().__init__()
        self.roues_du_vehicule = Roues(2, Marque.dunlop)
        self.roues_du_vehicule.dimension = DimensionRoue.taille_28_pouces


class Vae(Velo):
    def __init__(self):
        super().__init__()
        self.moteur_en_marche: bool = False


class Voiture(Vehicule):
    def __init__(self, nb_de_roue: int = 4, nombre_de_places_assises=4):
        super().__init__()
        self.roues_du_vehicule = Roues(4, Marque.michelin)
        self.__moteur = False
        self.nombre_de_places_assises = int(nombre_de_places_assises)

    def demarre(self):
        if self.__moteur:
            print("Le moteur est déjà en marche")
        else:
            self.__moteur = True
            print("Moteur en marche")

    def arrete(self):
        if self.__moteur is False:
            print("Le moteur est déjà à l'arret")
        else:
            self.__moteur = False
            print("Moteur à l'arret")


toto = int(5)
la_voiture_de_papa = Voiture(nombre_de_places_assises=5)
la_voiture_de_papa.nombre_de_places_assises = 5
print(la_voiture_de_papa.color)
print(la_voiture_de_papa.roues_du_vehicule.nombre)

print(la_voiture_de_papa.roues_du_vehicule.dimension)
la_voiture_de_papa.arrete()
la_voiture_de_papa.demarre()

print()

la_voiture_de_maman = Voiture(nb_de_roue=4)
la_voiture_de_maman.color = Color.verte
la_voiture_de_maman.roues_du_vehicule.marque = Marque.dunlop
la_voiture_de_maman.demarre()

if la_voiture_de_maman.color == Color.bleue:
    print("Elle est bleue")
else:
    print(la_voiture_de_maman.color.name)

print()
velo1 = Velo()
velo1.color = Color.rouge
print(velo1.roues_du_vehicule.nombre)
print(type(velo1))

print()
vae1 = Vae()
vae1.moteur_en_marche = True

print()
voitures_au_garage = {}
for i in range(0, 10, 1):
    voitures_au_garage[f"Voiture n°{i}"] = Voiture(4)

pass
