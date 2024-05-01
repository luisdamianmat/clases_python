mis_cursos=["Análisis Real 1","Análisis Funcional","Estructuras Algebraicas 1","EDO","EDP","Topología"]

print("Mis cursos sin actualizarlos es: {}".format(mis_cursos))
"""Ahora usaremos INSERT para añadir nuevos valores en la posicion correspondiente"""
mis_cursos.insert(1, "Análisis Real 2")
mis_cursos.insert(4, "Estructuras Algebraicas 2")

print("Mis cursos actualizados es: {}".format(mis_cursos))