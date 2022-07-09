from Base.models import Persona
from django.db import models    

ESTADOS = (
    (1, "ACTIVO"), 
    (2, "BAJA"), 
    (3, "MOROSO"),
)

class Cliente(Persona):
    id_number = models.CharField(max_length=50, unique=True, null=False)
    estado = models.CharField(max_length=50, choices=ESTADOS, default="ACTIVO", null=False)

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except IndexError:
            return {}