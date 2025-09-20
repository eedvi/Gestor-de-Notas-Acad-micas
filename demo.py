#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script - Gestor de Notas Académicas
Demuestra la funcionalidad del sistema con datos de ejemplo
"""

import sys
import os

# Importar las funciones necesarias
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def demo_sistema():
    """Demuestra el funcionamiento del sistema con datos de ejemplo"""
    
    # Importar módulos después de agregar al path
    import gestor_notas
    
    print("🎓 DEMO DEL GESTOR DE NOTAS ACADÉMICAS")
    print("=" * 60)
    
    # Limpiar datos existentes
    gestor_notas.courses_list.clear()
    gestor_notas.pila_historial.clear()
    
    # Agregar cursos de ejemplo
    cursos_ejemplo = [
        {"nombre": "Cálculo Diferencial", "nota": 88.5},
        {"nombre": "Física I", "nota": 42.0},
        {"nombre": "Programación", "nota": 95.0},
        {"nombre": "Química General", "nota": 67.5},
        {"nombre": "Historia Universal", "nota": 55.0},
        {"nombre": "Inglés Técnico", "nota": 78.0}
    ]
    
    gestor_notas.courses_list.extend(cursos_ejemplo)
    
    print(f"✅ Se agregaron {len(cursos_ejemplo)} cursos de ejemplo")
    print("\n" + "="*50)
    
    # Demo 1: Mostrar cursos
    print("📋 1. MOSTRAR TODOS LOS CURSOS")
    print("-" * 30)
    gestor_notas.mostrar_todos_cursos()
    
    print("\n" + "="*50)
    
    # Demo 2: Calcular promedio
    print("📊 2. PROMEDIO GENERAL")
    print("-" * 30)
    gestor_notas.calcular_promedio_general()
    
    print("\n" + "="*50)
    
    # Demo 3: Análisis de aprobados/reprobados
    print("📈 3. ANÁLISIS DE RENDIMIENTO")
    print("-" * 30)
    gestor_notas.contar_aprobados_reprobados()
    
    print("\n" + "="*50)
    
    # Demo 4: Ordenamiento por nota
    print("🔄 4. ORDENAMIENTO POR NOTA (BURBUJA)")
    print("-" * 30)
    print("Antes del ordenamiento:")
    for i, curso in enumerate(gestor_notas.courses_list, 1):
        print(f"{i}. {curso['nombre']}: {curso['nota']}")
    
    # Simular ordenamiento burbuja manualmente para demo
    print("\nAplicando algoritmo de ordenamiento burbuja...")
    n = len(gestor_notas.courses_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if gestor_notas.courses_list[j]["nota"] < gestor_notas.courses_list[j + 1]["nota"]:
                gestor_notas.courses_list[j], gestor_notas.courses_list[j + 1] = gestor_notas.courses_list[j + 1], gestor_notas.courses_list[j]
    
    print("Después del ordenamiento (mayor a menor):")
    for i, curso in enumerate(gestor_notas.courses_list, 1):
        print(f"{i}. {curso['nombre']}: {curso['nota']}")
    
    print("\n" + "="*50)
    
    # Demo 5: Simular historial
    print("📚 5. SIMULACIÓN DEL HISTORIAL")
    print("-" * 30)
    
    # Agregar algunos cambios al historial
    cambios_ejemplo = [
        {
            "accion": "actualizado",
            "curso": "Física I",
            "nota_anterior": 42.0,
            "nota_nueva": 65.0
        },
        {
            "accion": "eliminado",
            "curso": "Biología",
            "nota_anterior": 70.0,
            "nota_nueva": None
        }
    ]
    
    gestor_notas.pila_historial.extend(cambios_ejemplo)
    
    print("Historial de cambios (LIFO - último en entrar, primero en salir):")
    for i in range(len(gestor_notas.pila_historial) - 1, -1, -1):
        cambio = gestor_notas.pila_historial[i]
        numero = len(gestor_notas.pila_historial) - i
        print(f"#{numero} - {cambio['accion'].upper()}: {cambio['curso']}")
        if cambio['accion'] == 'actualizado':
            print(f"    {cambio['nota_anterior']} → {cambio['nota_nueva']}")
        elif cambio['accion'] == 'eliminado':
            print(f"    Nota eliminada: {cambio['nota_anterior']}")
    
    print("\n" + "="*50)
    
    # Demo 6: Búsqueda lineal
    print("🔍 6. BÚSQUEDA LINEAL")
    print("-" * 30)
    termino = "prog"
    print(f"Buscando cursos que contengan '{termino}':")
    
    resultados = []
    for i, curso in enumerate(gestor_notas.courses_list):
        if termino.lower() in curso["nombre"].lower():
            resultados.append((i, curso))
    
    if resultados:
        for pos, curso in resultados:
            print(f"  ✓ Encontrado: {curso['nombre']} (Nota: {curso['nota']})")
    else:
        print(f"  ✗ No se encontraron cursos con '{termino}'")
    
    print("\n" + "="*50)
    
    # Resumen final
    print("📊 RESUMEN DEL DEMO")
    print("-" * 30)
    print(f"Total de cursos: {len(gestor_notas.courses_list)}")
    print(f"Promedio general: {sum(c['nota'] for c in gestor_notas.courses_list) / len(gestor_notas.courses_list):.2f}")
    aprobados = sum(1 for c in gestor_notas.courses_list if c['nota'] >= 60)
    print(f"Cursos aprobados: {aprobados}/{len(gestor_notas.courses_list)}")
    print(f"Cambios en historial: {len(gestor_notas.pila_historial)}")
    
    print("\n🎉 ¡DEMO COMPLETADO!")
    print("\nPara usar el sistema completo, ejecute:")
    print("python3 gestor_notas.py")


if __name__ == "__main__":
    try:
        demo_sistema()
    except Exception as e:
        print(f"❌ Error durante el demo: {e}")
        import traceback
        traceback.print_exc()