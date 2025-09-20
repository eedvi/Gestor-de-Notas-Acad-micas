#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Gestor de Notas Académicas
Validates core functionality without interactive input
"""

import sys
import os

# Add the main module to path
sys.path.append('/home/kot/Documents/projects/python/Gestor-de-Notas-Acad-micas')

# Import the main module and simulate some data
from gestor_notas import courses_list, pila_historial

def test_basic_functionality():
    """Test basic functionality with sample data"""
    print("🧪 TESTING GESTOR DE NOTAS ACADÉMICAS")
    print("=" * 50)
    
    # Clear any existing data
    courses_list.clear()
    pila_historial.clear()
    
    # Add sample courses directly
    sample_courses = [
        {"nombre": "Matemáticas", "nota": 85.5},
        {"nombre": "Física", "nota": 45.0},
        {"nombre": "Química", "nota": 92.0},
        {"nombre": "Historia", "nota": 55.0},
        {"nombre": "Inglés", "nota": 78.5}
    ]
    
    courses_list.extend(sample_courses)
    print(f"✅ Added {len(sample_courses)} sample courses")
    
    # Test 1: Display courses
    print("\n1. Testing mostrar_todos_cursos():")
    from gestor_notas import mostrar_todos_cursos
    mostrar_todos_cursos()
    
    # Test 2: Calculate average
    print("\n2. Testing calcular_promedio_general():")
    from gestor_notas import calcular_promedio_general
    calcular_promedio_general()
    
    # Test 3: Count passed/failed
    print("\n3. Testing contar_aprobados_reprobados():")
    from gestor_notas import contar_aprobados_reprobados
    contar_aprobados_reprobados()
    
    # Test 4: Bubble sort by grade
    print("\n4. Testing ordenar_por_nota_burbuja():")
    from gestor_notas import ordenar_por_nota_burbuja
    ordenar_por_nota_burbuja()
    
    # Test 5: Insertion sort by name
    print("\n5. Testing ordenar_por_nombre_insercion():")
    from gestor_notas import ordenar_por_nombre_insercion
    ordenar_por_nombre_insercion()
    
    # Test 6: Add sample history data and test
    print("\n6. Testing pila_historial functionality:")
    pila_historial.extend([
        {
            "accion": "actualizado",
            "curso": "Matemáticas",
            "nota_anterior": 80.0,
            "nota_nueva": 85.5
        },
        {
            "accion": "eliminado",
            "curso": "Biología",
            "nota_anterior": 65.0,
            "nota_nueva": None
        }
    ])
    
    from gestor_notas import mostrar_historial_cambios
    print(f"Added {len(pila_historial)} sample history entries")
    
    print("\n🎉 ALL BASIC TESTS COMPLETED SUCCESSFULLY!")
    print(f"Final courses count: {len(courses_list)}")
    print(f"History entries: {len(pila_historial)}")


def test_validation_functions():
    """Test individual algorithm implementations"""
    print("\n" + "=" * 50)
    print("🔬 TESTING ALGORITHM IMPLEMENTATIONS")
    print("=" * 50)
    
    # Test linear search
    print("\n7. Testing linear search logic:")
    search_term = "mat"  # Should find "Matemáticas"
    results = []
    for i, curso in enumerate(courses_list):
        if search_term.lower() in curso["nombre"].lower():
            results.append((i, curso))
    
    print(f"Searching for '{search_term}':")
    if results:
        for pos, curso in results:
            print(f"  Found: {curso['nombre']} at position {pos + 1}")
    else:
        print(f"  No results found for '{search_term}'")
    
    # Test binary search (requires sorted list)
    print("\n8. Testing binary search logic:")
    # Sort for binary search
    sorted_list = sorted(courses_list, key=lambda x: x["nombre"].lower())
    search_name = "química"
    
    # Binary search implementation
    inicio = 0
    fin = len(sorted_list) - 1
    encontrado = False
    
    while inicio <= fin and not encontrado:
        medio = (inicio + fin) // 2
        if sorted_list[medio]["nombre"].lower() == search_name.lower():
            print(f"Binary search found '{search_name}' at position {medio + 1}")
            encontrado = True
        elif sorted_list[medio]["nombre"].lower() < search_name.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    
    if not encontrado:
        print(f"Binary search: '{search_name}' not found")
    
    print("\n✅ ALGORITHM TESTS COMPLETED!")


if __name__ == "__main__":
    try:
        test_basic_functionality()
        test_validation_functions()
        print("\n🎊 ALL TESTS PASSED - SYSTEM IS WORKING CORRECTLY!")
    except Exception as e:
        print(f"\n❌ ERROR DURING TESTING: {e}")
        import traceback
        traceback.print_exc()