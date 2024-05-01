dicc={}

dicc["departamento 1"] = "Lima"
dicc["departamento 2"] = "Trujillo"
dicc["departamento 3"] = "Ancash"
dicc["departamento 4"] = "Loreto"
dicc["departamento 5"] = "Moquegua"
dicc["departamento 6"] = "Apurimac"

print(dicc)

del dicc["departamento 3"]
print(dicc)
keys = sorted(dicc)
print(keys)