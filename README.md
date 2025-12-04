🏋️‍♂️ SISTEMA DE GESTIÓN DE GIMNASIO

Proyecto Primer Parcial - Programación Orientada a Objetos

📋 📌 DESCRIPCIÓN DEL PROYECTO

Este proyecto implementa un Sistema de Gestión de Servicios para un Gimnasio utilizando Programación Orientada a Objetos en Python. Permite administrar diferentes tipos de membresías, clientes y operaciones del gimnasio.

🎯 🎯 OBJETIVOS DE APRENDIZAJE
✅	Objetivo
1️⃣	Diseñar un sistema con mínimo 5 clases
2️⃣	Aplicar encapsulamiento con atributos privados
3️⃣	Implementar herencia con superclase y 2 hijas
4️⃣	Demostrar polimorfismo con métodos comunes
5️⃣	Organizar código según PEP8 y buenas prácticas

🚀 Instrucciones para Ejecutar

Requisitos previos

* Python 3.8 o superior instalado
* Editor de código (VS Code, PyCharm, etc.)

Pasos de ejecución

1.- Clonar o descargar el repositorio

2.- Verificar que todos los archivos estén presentes:

* clase_base.py
* clase_hija_1.py
* clase_hija_2.py
* clase_extra_1.py
* clase_extra_2.py
* main.py

3.- Ejecutar el programa principal:

* main.py

4.- Salida esperada:

══════════════════════════════════════════
        REPORTE DE SERVICIOS
══════════════════════════════════════════

📋 Plan Básico - Presencial
   ├─ Precio base: $50.00
   ├─ Acceso sala: ✅
   ├─ Acceso clases: ❌
   └─ Costo total: $70.00

📋 Plan Premium - Presencial
   ├─ Precio base: $80.00
   ├─ Acceso sala: ✅
   ├─ Acceso clases: ✅
   └─ Costo total: $115.00

📋 Virtual Básico - Virtual
   ├─ Precio base: $30.00
   ├─ Plan videos: Estándar
   ├─ Incluye app: ❌
   └─ Costo total: $30.00

📋 Virtual Full - Virtual
   ├─ Precio base: $45.00
   ├─ Plan videos: Premium
   ├─ Incluye app: ✅
   └─ Costo total: $55.00

══════════════════════════════════════════
💰 TOTAL INGRESOS: $270.00
══════════════════════════════════════════

👥 CLIENTES REGISTRADOS:
• Cliente 1: Juan Pérez - Tel: 555-1234
• Cliente 2: Ana Gómez - Tel: 555-5678

📊 GESTOR ACTIVO:
• 4 servicios registrados

🏗️ 📐 DIAGRAMA DE CLASES

┌─────────────────────────────────┐
│      ServicioGym (Abstract)     │
├─────────────────────────────────┤
│ - _nombre: str                  │
│ - _precio_base: float           │
├─────────────────────────────────┤
│ + nombre: str (property)        │
│ + precio_base: float (property) │
│ + calcular_costo()*             │
│ + __str__()                     │
└───────────┬─────────────────────┘
            │
    ┌───────┴───────┐
    ▼               ▼
┌─────────────┐ ┌─────────────┐
│ Membresía   │ │ Membresía   │
│ Presencial  │ │ Virtual     │
├─────────────┤ ├─────────────┤
│ - acceso_   │ │ - plan_     │
│   sala      │ │   videos    │
│ - acceso_   │ │ - incluye_  │
│   clases    │ │   app       │
└─────────────┘ └─────────────┘
         │               │
         └───────┬───────┘
                 ▼
        ┌─────────────────┐
        │   GestorGym     │
        ├─────────────────┤
        │ - servicios[]   │
        ├─────────────────┤
        │ + agregar()     │
        │ + calcular_     │
        │   total()       │
        │ + generar_      │
        │   reporte()     │
        └─────────────────┘

