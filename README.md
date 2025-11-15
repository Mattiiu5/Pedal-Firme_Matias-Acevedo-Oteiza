Pedal Firme - Sistema de Gestión de Taller de Bicicletas

Pedal Firme es un sistema diseñado para gestionar las órdenes de trabajo de un taller de bicicletas. Permite a los empleados crear, editar, eliminar y listar órdenes de trabajo, así como generar reportes diarios de ventas. El sistema utiliza archivos CSV para persistir los datos, lo que permite guardar las órdenes entre ejecuciones del programa.

Funcionalidades Principales
Crear una nueva orden: Permite registrar una nueva orden de trabajo con información sobre el cliente, servicios realizados, y el monto total.
Editar una orden existente: Puedes modificar los detalles de una orden ya creada.
Eliminar una orden: Puedes eliminar una orden del sistema.
Listar órdenes por RUT: Muestra todas las órdenes asociadas a un RUT específico.
Generar reportes de ventas: Crea un reporte con la información de las órdenes cerradas, mostrando el total de las ventas.
Exportar e importar datos: El sistema guarda y carga las órdenes desde un archivo CSV, lo que asegura que los datos se mantengan entre sesiones.

Requisitos
Este proyecto está desarrollado en Python 3 y utiliza el módulo estándar csv para manejar la importación y exportación de datos. No es necesario instalar dependencias externas.

Uso
Para ejecutar el programa, simplemente ejecuta el archivo main.py desde la terminal:
python main.py
Esto iniciará el menú del sistema, donde podrás elegir entre las siguientes opciones:

1. Crear una orden
2. Editar una orden
3. Eliminar una orden
4. Listar órdenes por RUT
5. Generar reporte de ventas
6. Salir


Ejemplos de Ejecución

Ejemplo 1: Crear Orden
Opción seleccionada: 1
Crear una nueva orden:
RUT: 12345678-9
Cliente: Juan Pérez
Servicios: Cambio de llantas, Ajuste de frenos
Total: 25000
Orden creada correctamente con ID: f63b

Ejemplo 2: Listar Órdenes
Opción seleccionada: 2
Lista de órdenes:
ID: f63b
RUT: 12345678-9
Cliente: Juan Pérez
Servicios: Cambio de llantas, Ajuste de frenos
Total: 25000
Estado: Abierta

Ejemplo 3: Buscar una Orden por ID
Si buscas el ID f63b:
Opción seleccionada: 3
Introduzca el ID de la orden: f63b
Orden encontrada:
ID: f63b
RUT: 12345678-9
Cliente: Juan Pérez
Servicios: Cambio de llantas, Ajuste de frenos
Total: 25000
Estado: Abierta

Ejemplo 4: Eliminar una Orden

Supón que decides eliminar la orden con ID f63b. El proceso sería:
Opción seleccionada: 5
Introduzca el ID de la orden a eliminar: f63b
Orden eliminada correctamente.

Conclusión

Este sistema te permitirá gestionar de manera sencilla las órdenes de trabajo en un taller de bicicletas, asegurando que los datos se mantengan entre ejecuciones mediante el uso de archivos CSV. Puedes extender las funcionalidades según tus necesidades, como agregar más detalles en las órdenes o mejorar el manejo de errores.
