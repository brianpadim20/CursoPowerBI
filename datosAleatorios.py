import random

contador = 0
tipo_cliente = ["cliente oro", "empleado", "cliente normal"]
sucursal = ["Medellín","Sabaneta","Envigado","Cali","Barranquilla"]
while contador <= 198:
    # aleatorio = random.randint(18, 75)
    # tipo_cliente_elegido = random.choice(tipo_cliente)
    sucursal_elegida = random.choice(sucursal)
    print(f"{sucursal_elegida}")
    contador += 1


