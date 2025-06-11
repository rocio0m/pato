from datetime import date
objeto= {
    "nombre": "rocio",
    "edad": 17,
    "cuidad": "buenos aires",
}
#json
objeto["cumple"]=date(2007,08.09)
hoy = date(2025,6,11)
objeto["edad"] = hoy.year - objeto["cumple"].year
print("hola",objeto["nombre"])

def cumpleHoy(fechaDehoy):
    fechaDeNacimiento
