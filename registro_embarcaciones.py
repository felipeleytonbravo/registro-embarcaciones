def registrar_embarcacion():
    nombre = input("Nombre de la embarcación: ")
    tipo = input("Tipo (pesquera, turismo, carga, etc.): ")
    capacidad = input("Capacidad de personas: ")
    capitan = input("Nombre del capitán: ")

    return {
        "nombre": nombre,
        "tipo": tipo,
        "capacidad": capacidad,
        "capitan": capitan
    }

def mostrar_embarcaciones(lista):
    print("\n=== Registro de Embarcaciones ===")
    for i, emb in enumerate(lista, start=1):
        print(f"{i}. {emb['nombre']} - {emb['tipo']} - Capacidad: {emb['capacidad']} - Capitán: {emb['capitan']}")

def main():
    embarcaciones = []

    print("=== Sistema de Registro de Embarcaciones ===")
    while True:
        opcion = input("\n1) Registrar embarcación\n2) Mostrar registro\n3) Salir\nSeleccione: ")

        if opcion == "1":
            embarcaciones.append(registrar_embarcacion())
        elif opcion == "2":
            mostrar_embarcaciones(embarcaciones)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
