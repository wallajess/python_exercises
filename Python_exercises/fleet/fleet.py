from dataclasses import dataclass


@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def __post_init__(self):
        assert 0 >= self.zustand <= 100, f"Zustand {self.zustand}% muss zwischen 0% und 100% liegen."
        assert self.neupreis >= 0, f"Neupreis {self.neupreis}€ muss mindestens 0€ sein."
        assert self.leergewicht > 0, f"Leergewicht {self.leergewicht} kg muss größer als 0kg sein."
        assert self.baujahr > 1900, f"Baujahr {self.baujahr} muss größer als 1900 sein."

    def gewicht(self: "Fahrzeug") -> int:
        """Calculates the total weight of the vehicle"""
        return (self.leergewicht)

    def maut(self) -> int:
        """Calcualtes how much toll the vehicle must pay."""
        raise NotImplementedError

    def alter(self) -> int:
        """Calcualtes the vehicle's age."""
        if self.baujahr < 2022:
            return 2022 - self.baujahr
        return 0

    def marktwert(self) -> int:
        """Calcuates the vehicle's current market value."""
        prozentwert = (self.zustand - 5 * self.alter()) // 100
        marktwert = prozentwert * self.neupreis
        if marktwert < 0:
            return 0
        return marktwert


@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int = 0
    sitzplaetze: int = 0

    def __post_init__(self):
        assert self.leistung > 0, f"Leistung {self.leistung} kW muss größer als 0kW sein."
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."
        super().__post_init__()

    def plaetze(self: "Kraftfahrzeug") -> int:
        """Calculates a vechile's maximum number of passengers."""
        return self.sitzplaetze

    def maut(self: "Kraftfahrzeug") -> int:
        """Calcualtes how much toll the vehicle must pay based on max. number of passengers"""
        return (self.gewicht() // 5) + (25 * self.plaetze())


@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int = 0

    def __post_init__(self):
        assert self.stehplaetze <= self.sitzplaetze, "Stehplätze " + str(self.stehplaetze) + " muss kleiner oder gleich Sitzplätze " + str(self.sitzplaetze) + " sein."
        return super().__post_init__()

    def plaetze(self: "Bus") -> int:
        """Adds the number of standing spots on a bus to the total number of passengers."""
        return super().plaetze() + self.stehplaetze


@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int = 0

    def __post_init__(self):
        assert self.rahmengroesse > 0, "Rahmengröße " + str(self.rahmengroesse) + "cm muss größer als 0cm sein."
        super().__post_init__()

    def maut(self: "Fahrrad") -> int:
        """Indicates that a bicycle does not have to pay toll."""
        return 0

    def marktwert(self: "Fahrrad") -> int:
        """Calculates the current market value based on condition and age of the bike, includes 50% reduction."""
        super().marktwert() // 2


@dataclass
class PKW(Kraftfahrzeug):
    pass

    def __post_init__(self):
        super().__post_init__()

    def gewicht(self: "PKW") -> int:
        """Calculates the toal weight."""
        super().gewicht()


@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int = 0

    def __post_init__(self):
        assert 0 < self.zuladung <= (self.leergewicht * 2), "Zuladung " + str(self.zuladung) \
            + "kg muss größer als 0kg und maximal " + str(self.leergewicht * 2) + "kg sein."
        super().__post_init__()

    def gewicht(self: "LKW") -> int:
        """Calcualtes the total weight of the truck."""
        super().gewicht() + self.zuladung

    def maut(self: "LKW") -> int:
        """Calcualtes the toll the truck needs to pay based on its weight and number of seats."""
        super().maut() * 2