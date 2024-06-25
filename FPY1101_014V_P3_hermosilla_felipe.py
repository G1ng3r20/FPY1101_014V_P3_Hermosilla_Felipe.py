import random 

def validar_patente(patente):
    if len(patente) != 6:
        return False
    letras = patente[:4]
    numeros = patente[4:]
    for letra in letras:
        if letra in 'AEIOU' or not letra.isalpha():
            return False
    if not numeros.isdigit():
        return False
    return True
def grabar_vehiculo(vehiculos):
    tipo = input("Ingrese el tipo de vehículo (Automóvil, Camión, Camioneta, Moto): ").strip().capitalize()
    while tipo not in ['Automóvil', 'Camión', 'Camioneta', 'Moto']:
        tipo = input("Tipo de vehículo incorrecto. Ingrese nuevamente: ").strip().capitalize()
    
    patente = input("Ingrese la patente del vehículo (4 letras consonantes seguidas de 2 números): ").strip().upper()
    while not validar_patente(patente):
        patente = input("Patente incorrecta. Ingrese nuevamente: ").strip().upper()
    
    marca = input("Ingrese la marca del vehículo (entre 2 y 15 caracteres): ").strip()
    while len(marca) < 2 or len(marca) > 15:
        marca = input("Marca incorrecta. Ingrese nuevamente: ").strip()
    
    precio = int(input("Ingrese el precio del vehículo (mayor a $5,000,000): "))
    while precio <= 5000000:
        precio = int(input("Precio incorrecto. Ingrese nuevamente: "))
    
    multas = []
    num_multas = int(input("Ingrese la cantidad de multas del vehículo (0, 1 o más): "))
    for _ in range(num_multas):
        monto = random.randint(1500, 3500)
        fecha = input("Ingrese la fecha de la multa (dd/mm/aaaa): ")
        multas.append((monto, fecha))
    
    fecha_registro = input("Ingrese la fecha de registro del vehículo (dd/mm/aaaa): ")
    run_dueño = input("Ingrese el RUN del dueño del vehículo: ")
    nombre_dueño = input("Ingrese el nombre del dueño del vehículo: ")
    
    vehiculos[patente] = {
        'Tipo': tipo,
        'Marca': marca,
        'Precio': precio,
        'Multas': multas,
        'Fecha Registro': fecha_registro,
        'RUN Dueño': run_dueño,
        'Nombre Dueño': nombre_dueño
    }
    print("Vehículo registrado correctamente.")
def buscar_vehiculo(vehiculos):
    patente = input("Ingrese la patente del vehículo a buscar: ").strip().upper()
    if patente in vehiculos:
        print("Información del vehículo:")
        for key, value in vehiculos[patente].items():
            print(f"{key}: {value}")
    else:
        print("Vehículo no encontrado.")
def imprimir_certificados(vehiculos):
    for patente, datos in vehiculos.items():
        print(f"Certificados para el vehículo con patente {patente}:")
        print(f"1. Emisión de contaminantes")
        print(f"   Nombre: Emisión de contaminantes")
        print(f"   Patente: {patente}")
        print(f"   Nombre Dueño: {datos['Nombre Dueño']}")
        print(f"   RUN Dueño: {datos['RUN Dueño']}")
        print(f"2. Anotaciones vigentes")
        print(f"   Nombre: Anotaciones vigentes")
        print(f"   Patente: {patente}")
        print(f"   Nombre Dueño: {datos['Nombre Dueño']}")
        print(f"   RUN Dueño: {datos['RUN Dueño']}")
        print(f"3. Multas")
        print(f"   Nombre: Multas")
        print(f"   Patente: {patente}")
        print(f"   Nombre Dueño: {datos['Nombre Dueño']}")
        print(f"   RUN Dueño: {datos['RUN Dueño']}")
        print()
def main():
    vehiculos = {}
    while True:
        print("\n=== Menú de opciones ===")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo por patente")
        print("3. Imprimir certificados")
        print("4. Salir del programa")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            grabar_vehiculo(vehiculos)
        elif opcion == '2':
            buscar_vehiculo(vehiculos)
        elif opcion == '3':
            imprimir_certificados(vehiculos)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Ingrese nuevamente.")

if _name_ == "_main_":
    main()
  