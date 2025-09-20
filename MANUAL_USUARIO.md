# Manual de Usuario - Gestor de Notas Académicas

## 📚 Descripción del Sistema

El **Gestor de Notas Académicas** es un sistema completo desarrollado en Python para gestionar, analizar y organizar las calificaciones de cursos universitarios. El sistema funciona completamente en consola y permite realizar múltiples operaciones sobre los datos académicos.

## 🚀 Cómo Ejecutar el Programa

1. Abra una terminal en el directorio del proyecto
2. Ejecute el comando:
   ```bash
   python3 gestor_notas.py
   ```
3. Siga las instrucciones en pantalla

## 📋 Funcionalidades Principales

### 1. Registrar Nuevo Curso
- **Opción**: 1
- **Descripción**: Permite registrar un nuevo curso con su respectiva nota
- **Validaciones**:
  - El nombre del curso no puede estar vacío
  - La nota debe estar entre 0 y 100
  - No permite cursos duplicados
- **Ejemplo de uso**:
  ```
  Nombre del curso: Matemáticas I
  Nota: 85.5
  ```

### 2. Mostrar Todos los Cursos
- **Opción**: 2
- **Descripción**: Muestra una lista completa de todos los cursos registrados
- **Información mostrada**:
  - Número de orden
  - Nombre del curso
  - Nota
  - Estado (APROBADO/REPROBADO)

### 3. Calcular Promedio General
- **Opción**: 3
- **Descripción**: Calcula y muestra el promedio de todas las notas
- **Información mostrada**:
  - Cantidad de cursos
  - Suma total de notas
  - Promedio general
  - Estado general del estudiante

### 4. Análisis de Aprobados y Reprobados
- **Opción**: 4
- **Descripción**: Proporciona estadísticas detalladas sobre el rendimiento
- **Información mostrada**:
  - Cantidad y porcentaje de cursos aprobados
  - Cantidad y porcentaje de cursos reprobados
  - Lista detallada por categoría
  - Análisis del rendimiento general

### 5. Búsqueda Lineal de Cursos
- **Opción**: 5
- **Descripción**: Busca cursos por nombre usando algoritmo de búsqueda lineal
- **Características**:
  - Permite coincidencias parciales
  - No sensible a mayúsculas/minúsculas
  - Muestra todos los resultados encontrados

### 6. Actualizar Nota de Curso
- **Opción**: 6
- **Descripción**: Modifica la nota de un curso existente
- **Características**:
  - Validación de la nueva nota (0-100)
  - Confirmación antes de actualizar
  - Registro automático en el historial
  - Muestra el cambio realizado

### 7. Eliminar Curso
- **Opción**: 7
- **Descripción**: Elimina un curso de la lista
- **Características**:
  - Confirmación obligatoria antes de eliminar
  - Registro automático en el historial
  - Información sobre cursos restantes

### 8. Ordenamiento por Nota (Algoritmo Burbuja)
- **Opción**: 8
- **Descripción**: Ordena los cursos por nota de mayor a menor
- **Características**:
  - Implementa el algoritmo de ordenamiento burbuja
  - Orden descendente (mejores notas primero)
  - Muestra estadísticas del proceso de ordenamiento

### 9. Ordenamiento por Nombre (Algoritmo Inserción)
- **Opción**: 9
- **Descripción**: Ordena los cursos alfabéticamente por nombre
- **Características**:
  - Implementa el algoritmo de ordenamiento por inserción
  - Orden alfabético ascendente
  - Muestra estadísticas del proceso

### 10. Búsqueda Binaria de Cursos
- **Opción**: 10
- **Descripción**: Busca cursos usando algoritmo de búsqueda binaria
- **Características**:
  - Requiere lista ordenada por nombre
  - Búsqueda por nombre exacto
  - Mayor eficiencia que la búsqueda lineal
  - Opción de ordenar automáticamente si es necesario

### 11. Simulación de Cola de Revisiones
- **Opción**: 11
- **Descripción**: Simula un sistema de cola FIFO para revisión de notas
- **Características**:
  - Solo incluye cursos reprobados (nota < 60)
  - Procesamiento FIFO (Primero en entrar, primero en salir)
  - Simulación interactiva del procesamiento
  - Resultados aleatorios de revisión

### 12. Historial de Cambios (Pila)
- **Opción**: 12
- **Descripción**: Muestra el historial de cambios realizados
- **Características**:
  - Estructura de pila LIFO (Último en entrar, primero en salir)
  - Registro automático de actualizaciones y eliminaciones
  - Vista detallada de cada cambio
  - Opciones para limpiar historial

### 13. Salir
- **Opción**: 13
- **Descripción**: Termina la ejecución del programa

## 📊 Estructuras de Datos Utilizadas

### Lista de Cursos (courses_list)
```python
[
    {
        "nombre": "Nombre del curso",
        "nota": valor_numerico
    }
]
```

### Pila de Historial (pila_historial)
```python
[
    {
        "accion": "actualizado" | "eliminado",
        "curso": "Nombre del curso",
        "nota_anterior": valor,
        "nota_nueva": valor | None
    }
]
```

### Cola de Revisiones (cola_revisiones)
```python
["curso1", "curso2", "curso3", ...]
```

## 🔍 Algoritmos Implementados

1. **Búsqueda Lineal**: O(n) - Para buscar cursos con coincidencias parciales
2. **Búsqueda Binaria**: O(log n) - Para buscar cursos específicos en listas ordenadas
3. **Ordenamiento Burbuja**: O(n²) - Para ordenar por nota
4. **Ordenamiento por Inserción**: O(n²) - Para ordenar por nombre
5. **Pila (LIFO)**: Para gestionar historial de cambios
6. **Cola (FIFO)**: Para simular procesamiento de revisiones

## ⚠️ Consideraciones Importantes

- Las notas deben estar entre 0 y 100
- Un curso se considera aprobado con nota ≥ 60
- Los nombres de cursos no pueden estar vacíos
- La búsqueda binaria requiere que la lista esté ordenada por nombre
- Los cambios se registran automáticamente en el historial
- Los datos se pierden al cerrar el programa (almacenamiento en memoria)

## 💡 Consejos de Uso

1. **Registre varios cursos** antes de probar las funciones de análisis
2. **Use la búsqueda lineal** para encontrar cursos con nombres parciales
3. **Ordene por nombre** antes de usar la búsqueda binaria
4. **Revise el historial** después de hacer cambios para verificar las operaciones
5. **Use la simulación de cola** para entender el proceso de revisiones académicas

## 🎯 Ejemplos de Flujo de Trabajo

### Flujo Básico:
1. Registrar cursos (Opción 1)
2. Ver todos los cursos (Opción 2)
3. Calcular promedio (Opción 3)
4. Analizar aprobados/reprobados (Opción 4)

### Flujo de Búsqueda:
1. Buscar curso específico (Opción 5)
2. Ordenar por nombre (Opción 9)
3. Búsqueda binaria eficiente (Opción 10)

### Flujo de Gestión:
1. Actualizar notas (Opción 6)
2. Verificar historial (Opción 12)
3. Eliminar cursos si es necesario (Opción 7)

## 🐛 Solución de Problemas

- **Error de nota inválida**: Asegúrese de ingresar números entre 0 y 100
- **Curso no encontrado**: Verifique la escritura exacta del nombre
- **Lista vacía**: Registre al menos un curso antes de usar otras funciones
- **Búsqueda binaria falla**: Ordene la lista por nombre primero (Opción 9)

¡Disfrute usando el Gestor de Notas Académicas! 🎓