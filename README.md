# Proyecto Programa gestión sociedades

## 1) Objetivo
- El objetivo principal de este proyecto sería crear un pequeño problema que nos permita realizar el logueo y autentificación de usuarios en la base de datos. Realizar la reserva de las mesas por parte de los mismos usuarios y por último también llevar una gestión de los productos y también de las ventas que se realizan en la sociedad.

## 2) Proximos objetivos en el programa para finalizarlo y mejoras
- Añadirle uso de sesiones para poder realizar desde ahí tanto las reservas como la compra de materiales debido a que de momento el proyecto no guarda sesión y solo comprueba y guarda datos directamente en la base de datos cuando se realiza el logueo.
- Una vez acabado con el logueo quiero meterle todas las opciones de compra de los productos. De momento solo quiero que realice y registre en la base de datos quien a comprado que producto y cuanta cantidad. Después también que cuando alguien compre un producto con un trigger se modifique en la base de datos las existencias del producto que quedan en la sociedad.
- Acabado con el apartado de la venta de productos pasaré a realizar el apartado de las reservas donde los socios podrán reservar las diferentes mesas para realizar diversas actividades.
- Una vez acabado todo eso quiero añadirle un sistema visual para que no se realice todo desde la terminal.

## 4) Estructura del proyecto
La estructura de capetas del proyecto sería la siguiente:
```
proyecto_Sociedades/
├── main.py  #Donde se ejecuta el pipline completo
├── data/
│   ├── raw/ 
│   └── processed/ 
├── database/
│   ├── dbModels
|       ├── __init__.py
|       ├── Actividades.py
|       ├── Compra.py
|       ├── Mesas.py
|       ├── Producto.py
|       ├── Reservas.py
|       └── User.py
│   └── conexiónDB.py
├── notebooks/
├── src/
│   ├── api
│   ├── models
|       ├── Usuario.py
│   ├── utils
└──── README.md
```

## 5) Cómo ejecutar
- Primero tienes que crear el entorno escribiendo el siguiente codigo: python -m venv .venv
- Para poder ejecutar el código primero tienes que activar el entorno escribiendo el siguiente código estando en el terminal en la carpeta de project_demo: .\.venv\Scripts\activate
- Antes de lanzar el proyecto tienes que intalar en el .venv todas la librerias que aparecen en el requirements.txt para ello tienes que escribir el siguiente codigo: pip install -r requirements.txt (Todavía tengo que crear el archivo pero hasta no acabar el proyecto no creo que lo cree debido a que todavía le tendré que añadir muchos imports)
- Después simplemente solo tienes que escribir python main.py para ejecutar todo el código.
