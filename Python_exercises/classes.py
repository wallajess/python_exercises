
# Methoden:
#    - erste Parameter heißt self


@dataclass
class Circle: 
    radius : float
    x : float 
    y : float

    def area(self) -> float: 
        return self.radius * self.radius * math.pi 
    
    def size_change(self , percent : float): 
        self.radius = self.radius * (percent / 100) 
    
    def move(self , xchange : float =0, ychange : float =0): 
        self.x = self.x + xchange 
        self.y = self.y + ychange


# Vererbung
# Unterklassen:
# - erben Attribute und Methoden von der Oberklasse und 
# - können neue Attribute und Methoden einführen und
# - können Attribute und Methoden der Oberklasse überschreiben


#Invariante
# Eine logische Aussage über die Attribute eines Objects 
# Must be mentioned in the docstring!!!
# Essentially a condition that an object must meet at all times
# It must be tested using the __post_init__

@dataclass 
class Circle(TwoDObject ): 
    ...
    radius : float 
    
    def __post_init__(self): 
        assert self.radius > 0, "radius␣should␣be␣greater␣than␣0"

# Properties
# Their names begin with __:
@dataclass 
class Circle(TwoDObject ): 
    ...
    __radius : float # Property 
    
    def __post_init__(self): 
        assert self.radius > 0, "radius␣should␣be␣greater␣than␣0"
    
    @property # allows radius to be used as an attribute
    def radius(self) -> float:
        return self.__radius

# Creating classes without @dataclass
# Conventions:
# - capitalize class names