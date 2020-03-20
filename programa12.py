precio_payaso = 112
precio_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
precio_total = precio_payaso * payasos + precio_muñeca * muñecas
print("El precio total del paquete es " + str(precio_total))