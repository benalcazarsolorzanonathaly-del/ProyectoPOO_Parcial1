# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY


from clase_base import ServicioGym
from clase_hija_1 import MembresiaPresencial
from clase_hija_2 import MembresiaVirtual
from clase_extra_1 import Cliente
from clase_extra_2 import GestorGym


def main():
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE GIMNASIO - GRUPO 8")
    print("=" * 60)

    # PUNTO 1: Crear varios objetos de las clases hijas
    print("\n1️⃣ CREACIÓN DE OBJETOS (Clases Hijas):")
    print("-" * 40)

    membresia1 = MembresiaPresencial("Plan Básico", 50, True, False)
    print(f"✓ MembresiaPresencial 1 creada: {membresia1.nombre}")

    membresia2 = MembresiaPresencial("Plan Premium", 80, True, True)
    print(f"✓ MembresiaPresencial 2 creada: {membresia2.nombre}")

    membresia3 = MembresiaVirtual("Virtual Básico", 30, "Estándar", False)
    print(f"✓ MembresiaVirtual 1 creada: {membresia3.nombre}")

    membresia4 = MembresiaVirtual("Virtual Full", 45, "Premium", True)
    print(f"✓ MembresiaVirtual 2 creada: {membresia4.nombre}")

    # PUNTO 2: Guardarlos en una lista de la superclase
    print("\n2️⃣ LISTA DE SUPERCLASE (Polimorfismo):")
    print("-" * 40)
    lista_servicios: list[ServicioGym] = [membresia1, membresia2, membresia3, membresia4]
    print(f"✓ Lista creada con {len(lista_servicios)} objetos ServicioGym")
    print(f"✓ Tipo de lista: {type(lista_servicios)}")
    print(f"✓ Tipo primer elemento: {type(lista_servicios[0])}")

    # PUNTO 3: Ejecutar métodos heredados y propios
    print("\n3️⃣ MÉTODOS HEREDADOS Y PROPIOS:")
    print("-" * 40)
    for i, servicio in enumerate(lista_servicios, 1):
        print(f"\nServicio {i} ({type(servicio).__name__}):")
        print(f"  Nombre (getter): {servicio.nombre}")
        print(f"  Precio base (getter): ${servicio.precio_base}")
        print(f"  Calcular costo (método): ${servicio.calcular_costo():.2f}")

    # Clases adicionales
    print("\n4️⃣ CLASES ADICIONALES (Cliente y Gestor):")
    print("-" * 40)
    cliente1 = Cliente(1, "Juan Pérez", "555-1234")
    cliente2 = Cliente(2, "Ana Gómez", "555-5678")
    print(f"✓ Cliente 1: {cliente1}")
    print(f"✓ Cliente 2: {cliente2}")

    gestor = GestorGym()
    for servicio in lista_servicios:
        gestor.agregar_servicio(servicio)
    print(f"✓ Gestor creado con {len(lista_servicios)} servicios")

    # PUNTO 4: Ejecutar los métodos polimórficos (los 2 obligatorios)
    print("\n5️⃣ MÉTODOS POLIMÓRFICOS (2 obligatorios):")
    print("-" * 40)

    print("\na) calcular_total_ingresos():")
    total = gestor.calcular_total_ingresos(lista_servicios)
    print(f"   Resultado: ${total:.2f}")

    print("\nb) generar_reporte():")
    reporte = gestor.generar_reporte(lista_servicios)
    print("   Contenido del reporte:")
    print("   " + "=" * 35)
    for linea in reporte.split('\n'):
        print(f"   {linea}")

    # PUNTO 5: Imprimir objetos para usar __str__()
    print("\n6️⃣ IMPRESIÓN CON __str__():")
    print("-" * 40)
    print("\nLista completa de servicios (usando __str__):")
    print("-" * 50)
    for servicio in lista_servicios:
        print(servicio)  # Esto llama automáticamente a __str__()

    print("\n" + "=" * 60)
    print("EJECUCIÓN COMPLETADA - TODOS LOS REQUISITOS CUMPLIDOS")
    print("=" * 60)

    # Mostrar fecha y hora (importante para captura)
    import datetime
    ahora = datetime.datetime.now()
    print(f"\n📅 Fecha y hora de ejecución: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()