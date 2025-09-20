#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestor de Notas Académicas
Sistema para gestionar y analizar calificaciones de cursos universitarios
Autor: Sistema de Gestión Académica
Fecha: 2025
"""

# Variables globales principales
courses_list = []
pila_historial = []
cola_revisiones = []


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*40)
    print("    GESTOR DE NOTAS ACADÉMICAS")
    print("="*40)
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    print("="*40)


def obtener_opcion():
    """Obtiene y valida la opción del usuario"""
    try:
        option = int(input("Seleccione una opción (1-13): "))
        return option
    except ValueError:
        return -1


def pausa():
    """Hace una pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


def main():
    """Función principal del programa"""
    continuar = True
    
    print("¡Bienvenido al Gestor de Notas Académicas!")
    
    while continuar:
        mostrar_menu()
        option = obtener_opcion()
        
        if option == 1:
            registrar_curso()
            
        elif option == 2:
            mostrar_todos_cursos()
            
        elif option == 3:
            calcular_promedio_general()
            
        elif option == 4:
            contar_aprobados_reprobados()
            
        elif option == 5:
            buscar_curso_lineal()
            
        elif option == 6:
            actualizar_nota_curso()
            
        elif option == 7:
            eliminar_curso()
            
        elif option == 8:
            ordenar_por_nota_burbuja()
            
        elif option == 9:
            ordenar_por_nombre_insercion()
            
        elif option == 10:
            buscar_curso_binario()
            
        elif option == 11:
            simular_cola_revisiones()
            
        elif option == 12:
            mostrar_historial_cambios()
            
        elif option == 13:
            print("\n¡Gracias por usar el Gestor de Notas Académicas!")
            print("¡Hasta pronto!")
            continuar = False
            
        else:
            print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 13.")
        
        if continuar:
            pausa()


# Funciones del sistema
def registrar_curso():
    """
    Registra un nuevo curso con su respectiva nota
    Valida que el nombre no esté vacío y que la nota esté entre 0 y 100
    """
    print("\n--- REGISTRAR NUEVO CURSO ---")
    
    # Validar nombre del curso
    while True:
        nombre = input("Ingrese el nombre del curso: ").strip()
        if nombre:
            break
        else:
            print("❌ El nombre del curso no puede estar vacío. Inténtelo de nuevo.")
    
    # Validar nota del curso
    while True:
        try:
            nota = float(input("Ingrese la nota del curso (0-100): "))
            if 0 <= nota <= 100:
                break
            else:
                print("❌ La nota debe estar entre 0 y 100. Inténtelo de nuevo.")
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
    
    # Verificar si el curso ya existe
    for curso in courses_list:
        if curso["nombre"].lower() == nombre.lower():
            print(f"❌ El curso '{nombre}' ya está registrado.")
            print("Use la opción 6 para actualizar la nota existente.")
            return
    
    # Agregar curso a la lista
    nuevo_curso = {
        "nombre": nombre,
        "nota": nota
    }
    courses_list.append(nuevo_curso)
    
    print(f"✅ Curso '{nombre}' registrado exitosamente con nota {nota}")
    print(f"Total de cursos registrados: {len(courses_list)}")

def mostrar_todos_cursos():
    """
    Muestra todos los cursos registrados con sus notas
    """
    print("\n--- TODOS LOS CURSOS REGISTRADOS ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados.")
        print("Use la opción 1 para registrar su primer curso.")
        return
    
    print(f"Total de cursos: {len(courses_list)}")
    print("-" * 50)
    
    for i, curso in enumerate(courses_list, 1):
        estado = "✅ APROBADO" if curso["nota"] >= 60 else "❌ REPROBADO"
        print(f"{i:2}. {curso['nombre']:<30} | Nota: {curso['nota']:6.2f} | {estado}")
    
    print("-" * 50)


def calcular_promedio_general():
    """
    Calcula y muestra el promedio general de todas las notas
    """
    print("\n--- PROMEDIO GENERAL ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para calcular el promedio.")
        return
    
    # Sumar todas las notas
    suma_notas = sum(curso["nota"] for curso in courses_list)
    
    # Calcular promedio
    promedio = suma_notas / len(courses_list)
    
    print(f"Cantidad de cursos: {len(courses_list)}")
    print(f"Suma total de notas: {suma_notas:.2f}")
    print(f"Promedio general: {promedio:.2f}")
    
    # Determinar estado general
    if promedio >= 60:
        print("🎉 Estado general: APROBADO")
    else:
        print("⚠️ Estado general: NECESITA MEJORAR")

def contar_aprobados_reprobados():
    """
    Cuenta y muestra estadísticas de cursos aprobados y reprobados
    """
    print("\n--- ANÁLISIS DE APROBADOS Y REPROBADOS ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para analizar.")
        return
    
    aprobados = 0
    reprobados = 0
    
    # Contar cursos según su estado (nota >= 60 es aprobado)
    for curso in courses_list:
        if curso["nota"] >= 60:
            aprobados += 1
        else:
            reprobados += 1
    
    total = len(courses_list)
    porcentaje_aprobados = (aprobados / total) * 100
    porcentaje_reprobados = (reprobados / total) * 100
    
    print(f"Total de cursos: {total}")
    print("-" * 40)
    print(f"✅ Cursos aprobados: {aprobados} ({porcentaje_aprobados:.1f}%)")
    print(f"❌ Cursos reprobados: {reprobados} ({porcentaje_reprobados:.1f}%)")
    print("-" * 40)
    
    # Mostrar detalles por categoría
    if aprobados > 0:
        print("\nCURSOS APROBADOS:")
        for curso in courses_list:
            if curso["nota"] >= 60:
                print(f"  • {curso['nombre']}: {curso['nota']:.2f}")
    
    if reprobados > 0:
        print("\nCURSOS REPROBADOS:")
        for curso in courses_list:
            if curso["nota"] < 60:
                print(f"  • {curso['nombre']}: {curso['nota']:.2f}")
    
    # Análisis adicional
    if porcentaje_aprobados >= 70:
        print("\n🎉 Excelente rendimiento académico!")
    elif porcentaje_aprobados >= 50:
        print("\n👍 Buen rendimiento, pero puede mejorar.")
    else:
        print("\n⚠️ Rendimiento bajo, necesita mejorar urgentemente.")

def buscar_curso_lineal():
    """
    Busca un curso por nombre usando búsqueda lineal
    Permite coincidencias parciales (case insensitive)
    """
    print("\n--- BÚSQUEDA LINEAL DE CURSO ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para buscar.")
        return
    
    termino_busqueda = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    if not termino_busqueda:
        print("❌ Debe ingresar un término de búsqueda válido.")
        return
    
    resultados = []
    
    # Búsqueda lineal secuencial
    for i, curso in enumerate(courses_list):
        if termino_busqueda in curso["nombre"].lower():
            resultados.append((i, curso))
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
        print("-" * 50)
        for posicion, curso in resultados:
            estado = "APROBADO" if curso["nota"] >= 60 else "REPROBADO"
            print(f"Posición: {posicion + 1}")
            print(f"Curso: {curso['nombre']}")
            print(f"Nota: {curso['nota']:.2f}")
            print(f"Estado: {estado}")
            print("-" * 50)
    else:
        print(f"❌ No se encontró ningún curso que contenga '{termino_busqueda}'.")

def actualizar_nota_curso():
    """
    Actualiza la nota de un curso existente
    Registra el cambio en el historial (pila)
    """
    print("\n--- ACTUALIZAR NOTA DE CURSO ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para actualizar.")
        return
    
    # Mostrar cursos disponibles
    print("Cursos disponibles:")
    for i, curso in enumerate(courses_list, 1):
        print(f"{i}. {curso['nombre']} - Nota actual: {curso['nota']:.2f}")
    
    nombre_buscar = input("\nIngrese el nombre del curso a actualizar: ").strip()
    
    if not nombre_buscar:
        print("❌ Debe ingresar un nombre válido.")
        return
    
    # Buscar el curso
    curso_encontrado = None
    for curso in courses_list:
        if curso["nombre"].lower() == nombre_buscar.lower():
            curso_encontrado = curso
            break
    
    if not curso_encontrado:
        print(f"❌ No se encontró el curso '{nombre_buscar}'.")
        return
    
    print(f"\nCurso encontrado: {curso_encontrado['nombre']}")
    print(f"Nota actual: {curso_encontrado['nota']:.2f}")
    
    # Validar nueva nota
    while True:
        try:
            nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
            if 0 <= nueva_nota <= 100:
                break
            else:
                print("❌ La nota debe estar entre 0 y 100. Inténtelo de nuevo.")
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
    
    # Confirmar actualización
    print(f"\n¿Confirma actualizar la nota de '{curso_encontrado['nombre']}'?")
    print(f"Nota actual: {curso_encontrado['nota']:.2f}")
    print(f"Nueva nota: {nueva_nota:.2f}")
    
    confirmacion = input("Confirmar (s/n): ").lower()
    
    if confirmacion == 's':
        # Guardar en historial antes de actualizar
        registro_historial = {
            "accion": "actualizado",
            "curso": curso_encontrado['nombre'],
            "nota_anterior": curso_encontrado['nota'],
            "nota_nueva": nueva_nota
        }
        pila_historial.append(registro_historial)
        
        # Actualizar la nota
        curso_encontrado['nota'] = nueva_nota
        
        print(f"✅ Nota actualizada exitosamente para '{curso_encontrado['nombre']}'")
        print(f"Cambio registrado en el historial.")
    else:
        print("Operación cancelada.")


def eliminar_curso():
    """
    Elimina un curso de la lista
    Registra la eliminación en el historial (pila)
    """
    print("\n--- ELIMINAR CURSO ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para eliminar.")
        return
    
    # Mostrar cursos disponibles
    print("Cursos disponibles:")
    for i, curso in enumerate(courses_list, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")
    
    nombre_buscar = input("\nIngrese el nombre del curso a eliminar: ").strip()
    
    if not nombre_buscar:
        print("❌ Debe ingresar un nombre válido.")
        return
    
    # Buscar el curso
    curso_encontrado = None
    indice_curso = -1
    
    for i, curso in enumerate(courses_list):
        if curso["nombre"].lower() == nombre_buscar.lower():
            curso_encontrado = curso
            indice_curso = i
            break
    
    if not curso_encontrado:
        print(f"❌ No se encontró el curso '{nombre_buscar}'.")
        return
    
    print(f"\nCurso a eliminar:")
    print(f"Nombre: {curso_encontrado['nombre']}")
    print(f"Nota: {curso_encontrado['nota']:.2f}")
    
    # Confirmar eliminación
    print(f"\n⚠️ ¿Está seguro de que desea eliminar el curso '{curso_encontrado['nombre']}'?")
    print("Esta acción se puede deshacer desde el historial.")
    
    confirmacion = input("Confirmar eliminación (s/n): ").lower()
    
    if confirmacion == 's':
        # Guardar en historial antes de eliminar
        registro_historial = {
            "accion": "eliminado",
            "curso": curso_encontrado['nombre'],
            "nota_anterior": curso_encontrado['nota'],
            "nota_nueva": None
        }
        pila_historial.append(registro_historial)
        
        # Eliminar el curso
        courses_list.pop(indice_curso)
        
        print(f"✅ Curso '{curso_encontrado['nombre']}' eliminado exitosamente.")
        print(f"Eliminación registrada en el historial.")
        print(f"Cursos restantes: {len(courses_list)}")
    else:
        print("Operación cancelada.")

def ordenar_por_nota_burbuja():
    """
    Ordena los cursos por nota usando el algoritmo de burbuja (descendente)
    """
    print("\n--- ORDENAR CURSOS POR NOTA (BURBUJA) ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para ordenar.")
        return
    
    if len(courses_list) <= 1:
        print("✅ Solo hay un curso o menos, no es necesario ordenar.")
        return
    
    print(f"Ordenando {len(courses_list)} cursos por nota (mayor a menor)...")
    
    # Algoritmo de ordenamiento burbuja (descendente)
    n = len(courses_list)
    intercambios = 0
    
    for i in range(n):
        hubo_intercambio = False
        
        for j in range(0, n - i - 1):
            # Comparar notas (orden descendente)
            if courses_list[j]["nota"] < courses_list[j + 1]["nota"]:
                # Intercambiar
                courses_list[j], courses_list[j + 1] = courses_list[j + 1], courses_list[j]
                intercambios += 1
                hubo_intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            break
    
    print(f"✅ Cursos ordenados por nota exitosamente.")
    print(f"Se realizaron {intercambios} intercambios.")
    print("\nLista ordenada:")
    mostrar_todos_cursos()


def ordenar_por_nombre_insercion():
    """
    Ordena los cursos por nombre usando el algoritmo de inserción (alfabético)
    """
    print("\n--- ORDENAR CURSOS POR NOMBRE (INSERCIÓN) ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para ordenar.")
        return
    
    if len(courses_list) <= 1:
        print("✅ Solo hay un curso o menos, no es necesario ordenar.")
        return
    
    print(f"Ordenando {len(courses_list)} cursos por nombre (alfabéticamente)...")
    
    # Algoritmo de ordenamiento por inserción
    comparaciones = 0
    
    for i in range(1, len(courses_list)):
        curso_actual = courses_list[i]
        j = i - 1
        
        # Mover elementos que son mayores que curso_actual hacia adelante
        while j >= 0 and courses_list[j]["nombre"].lower() > curso_actual["nombre"].lower():
            comparaciones += 1
            courses_list[j + 1] = courses_list[j]
            j -= 1
        
        if j >= 0:  # Si se hizo al menos una comparación válida
            comparaciones += 1
        
        courses_list[j + 1] = curso_actual
    
    print(f"✅ Cursos ordenados por nombre exitosamente.")
    print(f"Se realizaron {comparaciones} comparaciones.")
    print("\nLista ordenada:")
    mostrar_todos_cursos()

def buscar_curso_binario():
    """
    Busca un curso por nombre usando búsqueda binaria
    Requiere que la lista esté ordenada por nombre
    """
    print("\n--- BÚSQUEDA BINARIA DE CURSO ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para buscar.")
        return
    
    # Verificar si la lista está ordenada por nombre
    lista_ordenada = sorted(courses_list, key=lambda x: x["nombre"].lower())
    
    # Comprobar si la lista original está ordenada
    esta_ordenada = all(courses_list[i]["nombre"].lower() <= courses_list[i+1]["nombre"].lower() 
                       for i in range(len(courses_list)-1))
    
    if not esta_ordenada:
        print("⚠️ La lista no está ordenada por nombre.")
        respuesta = input("¿Desea ordenarla temporalmente para la búsqueda? (s/n): ").lower()
        if respuesta != 's':
            print("Operación cancelada. Use la opción 9 para ordenar la lista permanentemente.")
            return
        else:
            lista_busqueda = lista_ordenada
            print("Lista ordenada temporalmente para la búsqueda.")
    else:
        lista_busqueda = courses_list
    
    nombre_buscar = input("Ingrese el nombre exacto del curso a buscar: ").strip()
    
    if not nombre_buscar:
        print("❌ Debe ingresar un nombre válido.")
        return
    
    # Algoritmo de búsqueda binaria
    inicio = 0
    fin = len(lista_busqueda) - 1
    encontrado = False
    iteraciones = 0
    
    while inicio <= fin:
        iteraciones += 1
        medio = (inicio + fin) // 2
        nombre_medio = lista_busqueda[medio]["nombre"].lower()
        nombre_buscar_lower = nombre_buscar.lower()
        
        if nombre_medio == nombre_buscar_lower:
            curso = lista_busqueda[medio]
            estado = "APROBADO" if curso["nota"] >= 60 else "REPROBADO"
            print(f"\n✅ Curso encontrado en {iteraciones} iteraciones:")
            print("-" * 40)
            print(f"Curso: {curso['nombre']}")
            print(f"Nota: {curso['nota']:.2f}")
            print(f"Estado: {estado}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscar_lower:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    if not encontrado:
        print(f"❌ No se encontró el curso '{nombre_buscar}' después de {iteraciones} iteraciones.")
        print("Nota: La búsqueda binaria requiere coincidencia exacta del nombre.")

def simular_cola_revisiones():
    """
    Simula una cola de solicitudes de revisión de notas (FIFO)
    """
    print("\n--- SIMULACIÓN DE COLA DE REVISIONES ---")
    
    if not courses_list:
        print("❌ No hay cursos registrados para enviar a revisión.")
        return
    
    global cola_revisiones
    cola_revisiones = []  # Reiniciar la cola
    
    # Mostrar cursos disponibles para revisión (solo los reprobados)
    cursos_reprobados = [curso for curso in courses_list if curso["nota"] < 60]
    
    if not cursos_reprobados:
        print("✅ ¡Excelente! No hay cursos reprobados que requieran revisión.")
        return
    
    print("Cursos reprobados que pueden solicitar revisión:")
    for i, curso in enumerate(cursos_reprobados, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")
    
    # Agregar cursos a la cola
    print("\n¿Qué cursos desea enviar a revisión?")
    print("Ingrese los números separados por comas (ej: 1,3,4) o 'todos' para todos:")
    
    seleccion = input("Selección: ").strip().lower()
    
    if seleccion == 'todos':
        for curso in cursos_reprobados:
            cola_revisiones.append(curso["nombre"])
    else:
        try:
            indices = [int(x.strip()) for x in seleccion.split(',')]
            for indice in indices:
                if 1 <= indice <= len(cursos_reprobados):
                    cola_revisiones.append(cursos_reprobados[indice-1]["nombre"])
                else:
                    print(f"⚠️ Índice {indice} fuera de rango, ignorado.")
        except ValueError:
            print("❌ Formato inválido. No se agregaron cursos a la cola.")
            return
    
    if not cola_revisiones:
        print("❌ No se agregaron cursos a la cola de revisiones.")
        return
    
    print(f"\n✅ {len(cola_revisiones)} curso(s) agregado(s) a la cola de revisiones.")
    print("\nCola de revisiones (FIFO - Primero en entrar, primero en salir):")
    
    for i, curso in enumerate(cola_revisiones, 1):
        print(f"{i}. {curso}")
    
    # Simular procesamiento de la cola
    print("\n--- PROCESANDO COLA DE REVISIONES ---")
    input("Presione Enter para comenzar el procesamiento...")
    
    procesados = 0
    while cola_revisiones:
        curso_actual = cola_revisiones.pop(0)  # FIFO: remove from front
        procesados += 1
        
        print(f"\n🔍 Procesando revisión #{procesados}: {curso_actual}")
        
        # Simular tiempo de procesamiento
        import time
        time.sleep(1)
        
        # Simular resultado de revisión (aleatorio)
        import random
        aprobado = random.choice([True, False, False])  # 33% chance de aprobación
        
        if aprobado:
            print(f"✅ Revisión aprobada. Se ajustará la nota de '{curso_actual}'.")
            # Aquí podrías actualizar la nota realmente
        else:
            print(f"❌ Revisión denegada. La nota de '{curso_actual}' se mantiene.")
        
        if cola_revisiones:
            print(f"📋 Quedan {len(cola_revisiones)} solicitudes en cola.")
            continuar = input("¿Continuar con la siguiente revisión? (s/n): ").lower()
            if continuar != 's':
                print("Procesamiento pausado.")
                break
    
    if not cola_revisiones:
        print(f"\n🎉 ¡Cola de revisiones completamente procesada!")
        print(f"Total de solicitudes procesadas: {procesados}")


def mostrar_historial_cambios():
    """
    Muestra el historial de cambios usando estructura de pila (LIFO)
    """
    print("\n--- HISTORIAL DE CAMBIOS (PILA LIFO) ---")
    
    if not pila_historial:
        print("📋 No hay cambios registrados en el historial.")
        print("El historial se actualiza cuando actualiza o elimina cursos.")
        return
    
    print(f"Total de cambios registrados: {len(pila_historial)}")
    print("\nHistorial (del más reciente al más antiguo):")
    print("=" * 60)
    
    # Mostrar historial en orden LIFO (último en entrar, primero en salir)
    for i in range(len(pila_historial) - 1, -1, -1):
        cambio = pila_historial[i]
        numero = len(pila_historial) - i
        
        print(f"\n#{numero} - Acción: {cambio['accion'].upper()}")
        print(f"    Curso: {cambio['curso']}")
        
        if cambio['accion'] == 'actualizado':
            print(f"    Nota anterior: {cambio['nota_anterior']:.2f}")
            print(f"    Nota nueva: {cambio['nota_nueva']:.2f}")
            diferencia = cambio['nota_nueva'] - cambio['nota_anterior']
            if diferencia > 0:
                print(f"    Cambio: +{diferencia:.2f} (mejoró)")
            else:
                print(f"    Cambio: {diferencia:.2f} (empeoró)")
        elif cambio['accion'] == 'eliminado':
            print(f"    Nota del curso eliminado: {cambio['nota_anterior']:.2f}")
        
        print("-" * 40)
    
    # Opciones del historial
    print("\nOpciones del historial:")
    print("1. Ver detalle de un cambio específico")
    print("2. Limpiar historial")
    print("3. Volver al menú principal")
    
    opcion = input("Seleccione una opción (1-3): ").strip()
    
    if opcion == '1':
        try:
            num_cambio = int(input(f"Ingrese el número del cambio (1-{len(pila_historial)}): "))
            if 1 <= num_cambio <= len(pila_historial):
                indice = len(pila_historial) - num_cambio  # Convertir a índice real
                cambio = pila_historial[indice]
                print(f"\nDetalle completo del cambio #{num_cambio}:")
                print(f"Acción: {cambio['accion']}")
                print(f"Curso afectado: {cambio['curso']}")
                if cambio['nota_anterior'] is not None:
                    print(f"Nota anterior: {cambio['nota_anterior']:.2f}")
                if cambio['nota_nueva'] is not None:
                    print(f"Nota nueva: {cambio['nota_nueva']:.2f}")
            else:
                print("❌ Número de cambio inválido.")
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
    
    elif opcion == '2':
        confirmacion = input("¿Está seguro de limpiar todo el historial? (s/n): ").lower()
        if confirmacion == 's':
            pila_historial.clear()
            print("✅ Historial limpiado exitosamente.")
        else:
            print("Operación cancelada.")
    
    elif opcion == '3':
        pass  # Volver al menú principal
    
    else:
        print("❌ Opción inválida.")


if __name__ == "__main__":
    main()