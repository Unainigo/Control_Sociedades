# Proyecto Programa gestión sociedades

## 1) Descripción
- Permite la gestión de socios, productos y reservas mediante una base de datos PostgreSQL. 

## 2) Funcionalidades
- Gestión de socios
- Gestión de productos
- Gestión de reservas
- Autentificación de socios

## 3) Tecnologías
- Python
- SQLAlchemy
- PostgreSQL
- Bcrypt
- Pandas

## 4) Instalación

### 4.1) Clonación del repositorio
- git clone https://github.com/Unainigo/Control_Sociedades.git 

### 4.2) Creación del entorno virtual
- python -m venv .venv

### 4.3) Activación del entorno
- Windows: .venv\Scripts\activate
- linux/mac: source .venv/bin/activate

### 4.4) Instalar dependencias
- pip install -r requirements.txt 

## 5) Como ejecutar el proceso
- python main.py

## 6) Próximas mejoras
- Implementación de sesiones de usuario para mantener la autenticación activa durante la ejecución del sistema.
- Sistema completo de compra de productos:
    - Registro de compras por usuario
    - Control de stock en base de datos
    - Uso de triggers para actualizar existencias automáticamente
- Implementación del sistema de reservas de mesas para socios.
- Desarrollo de una interfaz visual (GUI o web) para sustituir el uso exclusivo de terminal.

## 7) Actualizaciones realizadas

### 7.1) 08/06/2026 
- Implementado sistema de login de usuarios.
- Inicio del sistema de autenticación (pendiente de sesiones para persistencia).

## 8) Estructura del proyecto
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

## 9) Autor
- Unai Iñigo
- GitHub: https://github.com/Unainigo
