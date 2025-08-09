# Gestor de Notas Académicas

## Redacción del Problema

El Gestor de Notas Académicas es un sistema desarrollado para estudiantes universitarios que necesitan organizar, analizar y gestionar las calificaciones de sus cursos de manera eficiente. Este sistema está diseñado para funcionar completamente en consola, proporcionando una interfaz simple pero poderosa que permite a los estudiantes llevar un control detallado de su rendimiento académico.

El sistema surge de la necesidad de contar con una herramienta práctica que permita no solo registrar notas, sino también realizar análisis estadísticos básicos, búsquedas eficientes y mantener un historial de cambios. Está dirigido específicamente a estudiantes que desean tener un control centralizado de sus calificaciones sin depender de plataformas externas complejas.

La aplicación cubre necesidades fundamentales como el cálculo automático de promedios, la identificación de cursos aprobados y reprobados, la organización de datos mediante diferentes criterios de ordenamiento, y la simulación de procesos académicos como solicitudes de revisión de notas.

## Requisitos del Sistema

### Requisitos Funcionales

1. **Registrar un nuevo curso y nota:** El sistema debe permitir ingresar el nombre de un curso y su calificación correspondiente, validando que la nota esté en el rango de 0 a 100 puntos.

2. **Mostrar todas las notas registradas:** Debe presentar una lista completa de todos los cursos registrados junto con sus respectivas calificaciones de manera clara y organizada.

3. **Realizar análisis estadístico básico:** El sistema debe calcular automáticamente el promedio general de todas las notas y contar cuántos cursos están aprobados (nota ≥ 60) y cuántos reprobados.

4. **Búsqueda de cursos:** Implementar dos tipos de búsqueda: búsqueda lineal que permita encontrar cursos por coincidencia parcial de nombre, y búsqueda binaria para mayor eficiencia cuando los datos estén ordenados.

5. **Ordenamiento de datos:** Proporcionar opciones para ordenar los cursos tanto por nota (usando algoritmo burbuja) como por nombre (usando algoritmo de inserción).

6. **Gestión de cambios:** Permitir actualizar y eliminar cursos existentes, manteniendo un historial de todos los cambios realizados usando una estructura de pila.

7. **Simulación de cola de revisiones:** Implementar una funcionalidad que simule el proceso de envío de cursos para revisión usando una estructura de cola.

### Requisitos No Funcionales

- **Plataforma:** El sistema se ejecuta exclusivamente en consola usando Python como lenguaje de programación.
- **Dependencias:** No se utilizarán librerías externas, solo las funcionalidades básicas del lenguaje Python.
- **Estructura de control:** El sistema debe implementar bucles repetitivos para el menú principal y condicionales para la navegación entre opciones.
- **Almacenamiento:** Los datos se almacenarán en memoria usando listas de Python durante la ejecución del programa.
- **Validación:** Debe incluir validaciones básicas para entradas del usuario, especialmente para las notas (rango 0-100).
- **Interfaz:** Mensajes claros y legibles para guiar al usuario en cada operación del sistema.

## Estructura del Proyecto

```
/GestorNotas/
├── gestor_notas.py          # Código fuente principal del sistema
├── pseudocodigo.txt         # Documento con el pseudocódigo general
├── README.md                # Descripción del proyecto y reflexión personal
├── manual_tecnico.pdf       # Manual técnico del sistema
├── manual_usuario.pdf       # Manual de uso del sistema
└── evidencia/               # (Opcional) Capturas de ejecución
```

## Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado en tu sistema
2. Descarga el archivo `gestor_notas.py`
3. Abre una terminal o línea de comandos
4. Navega hasta el directorio donde guardaste el archivo
5. Ejecuta: `python gestor_notas.py`
6. Sigue las instrucciones del menú interactivo

## Reflexión Personal

*(Esta sección se completará una vez finalizado el desarrollo del proyectooooooooo)*

### ¿Qué aprendí con este proyecto?

### ¿Qué fue lo más desafiante de resolver?

### ¿Qué mejoraría si tuviera más tiempo?