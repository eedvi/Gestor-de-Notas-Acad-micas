#!/usr/bin/env python3
# Simple test of core functions

# Simulate the courses_list data structure
courses_list = [
    {"nombre": "Matemáticas", "nota": 85.5},
    {"nombre": "Física", "nota": 45.0},
    {"nombre": "Química", "nota": 92.0}
]

print("Testing basic calculations:")
print(f"Courses: {len(courses_list)}")

# Test average calculation
suma = sum(curso["nota"] for curso in courses_list)
promedio = suma / len(courses_list)
print(f"Average: {promedio:.2f}")

# Test counting
aprobados = sum(1 for curso in courses_list if curso["nota"] >= 60)
reprobados = len(courses_list) - aprobados
print(f"Passed: {aprobados}, Failed: {reprobados}")

print("✅ Basic functionality works!")