print("bienvenido al programa..")
persona={"Nombre":"","Apellido":"","Edad":0,"Peso":0,"Altura":0,"Direccion":"","Telefono":""}
def cat_imc(imc):
    def cat_imc():
    "Obtencion de categoria de IMC"
    if imc < 18.5:
        cat = "Bajo peso"
    elif 18.5 < imc < 24.9:
        cat = "Peso normal"
    elif 25.0 < imc < 29.9:
        cat = "Sobre Peso"
    elif 30.0 < imc < 34.9:
        cat = "Obesidad tipo I"
    elif 35.0 < imc < 39.9:
        cat = "Obesidad tipo II"
    else imc > 40:
        cat = "Obesidad tipo III"
def imprimir(persona):
    print("Resultados: " + persona["Nombre"] + " " + persona["Apellido"] + "\nCategoria de IMC: " + cat_imc() + " / Peso " + persona["Peso"] + " / Kg altura: "+ persona["Altura"] + " metros\nEdad: " + persona["Edad"] + " años" "\nDireccion en: " + persona["Direccion"] + " / Telefono: " + persona["Telefono"] )
for item in persona:
    persona[item]=input(f"Ingrese su {item}")
imc=round(float(personal["Peso"])/(float(persona["Altura"])**2),2)
persona["IMC"]=imc

cat_imc(cat)
imprimir(persona)