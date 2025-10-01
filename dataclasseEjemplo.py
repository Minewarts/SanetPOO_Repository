from dataclasses import dataclass, field, asdict
import operaciones as op
@dataclass(frozen=True)
class Persona:
    nombre: str
    edad: int = field(default=35)

    def getEdadx2(self)->int:
        return self.edad * 2
@dataclass
class Puesto:
    persona: Persona
    nombre: str
    salario: float


persona = Persona("Juan",49)
print(asdict(persona))
persona2 = Persona("Juan")
puesto1 = Puesto(persona, "Desarrollador", 1500)
print(asdict(puesto1))
print(op.suma(persona.edad, persona2.edad))
if persona == persona2:
    print("Son iguales")
else:
    print("No son iguales")