"""crear clase alumno
debe tener un atriburo de nacionalidad
con valor peruano"""
class Alumno():

    def __init__(self, nombre, nacionalidad,distrito,nota1,nota2,nota3):
        self.nombre = nombre
        self.nacionalidad = "peruana"
        self.distrito = distrito
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Distrito:", self.distrito)
        print("Nota1:", self.nota1)
        print("Nota2:", self.nota2)
        print("Nota3:", self.nota3)
    def promedio(self):
        prom=(self.nota1+self.nota2+self.nota3)/3
        return prom
    def resultado(self):
        if self.promedio()>=11:
            print("Aprobo con :", self.promedio())
        else: print("Reprobo con :", self.promedio())

alumno1=Alumno("Sambenito","Peruano","Comas",0,18,4)
alumno2=Alumno("nelson","Venezolano","San Borja",0,13,3)
alumno1.mostrar()
alumno1.promedio()
alumno1.resultado()
alumno2.mostrar()
alumno2.promedio()
alumno2.resultado()

"""REVISAR EL CODIGO"""



