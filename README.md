# PROYECTO TIENDA - Sistema de Gestión de Registros de Servicios
> Asignatura: Programación Orientada a Objetos 
> Proyecto: Segundo Parcial - GUI con Base de Datos
> Jornada: GIG-S-VE-3-2 
> Grupo: GRUPO #1


# Integrantes:
# - Revelo Bravo Genesis
# - Vaque Reyes Daniela


# Descripción General del Sistema
Este sistema es una aplicación de escritorio diseñada para la gestión integral de registros de servicios dentro de una tienda online. Utiliza el paradigma de Programación Orientada a Objetos (POO) y una arquitectura limpia para separar la lógica de negocio de la persistencia de datos. La aplicación proporciona una interfaz gráfica intuitiva que permite al usuario interactuar directamente con una base de datos local en tiempo real, facilitando el control y seguimiento de las solicitudes de servicio técnico o atención al cliente ingresadas mediante formularios dinámicos.



# Funcionalidades Implementadas (CRUD Completos)
El sistema permite administrar el ciclo de vida completo de las solicitudes de servicio mediante operaciones directas:
> Ingresar (Create): Captura nuevos registros de servicios (Código, Fecha, Descripción y Email) mediante campos de entrada interactivos en la GUI y los almacena de forma persistente.
> Visualizar / Consultar (Read): Permite buscar un registro específico introduciendo su código identificador, recuperando la información almacenada en la base de datos para mostrarla en los campos correspondientes.
> Actualizar (Update): Permite modificar los datos de un servicio preexistente (como la fecha o la descripción) de manera segura buscando por su clave primaria.
> Eliminar (Delete): Borra permanentemente un registro de servicio de la base de datos a partir de su código único identificador.



# Tecnologías Utilizadas
> Lenguaje de Programación: Python 3.x
> Biblioteca Gráfica (GUI): PySide6 (Qt para Python)
> Motor de Base de Datos: SQLite (Módulo nativo `sqlite3`)
> Persistencia: Patrón de Diseño DAO (Data Access Object) para aislamiento de consultas SQL.



# Estructura del Proyecto
El código del repositorio está organizado bajo una estructura modular limpia:
text
PROYECTO_TIENDA/
│
├── main.py                 # Controlador principal de la GUI, eventos del formulario y arranque
├── vtn_principal.py        # Clase de la vista (interfaz generada por Qt UI Compiler)
├── tienda.db               # Base de datos SQLite local (Se autogenera al iniciar la app)
│
├── Datos/                  # Capa de Lógica de Negocio y Persistencia (POO)
│   ├── cliente_online.py   # Modelo para cuentas de clientes y validaciones
│   ├── compra_producto.py  # Modelo para compras de productos en la tienda
│   ├── gestor_tienda.py    # Clase de gestión global y métodos polimórficos
│   ├── registro_servicio.py# Modelo para los servicios de la interfaz gráfica
│   ├── servicio_dao.py     # Clase DAO para transacciones y conexión a la base de datos
│   ├── servicio_envio.py   # Modelo para el cálculo y tarifas de distribución de envíos
│   └── servicio_tienda.py  # Superclase base abstracta de servicios
│
└── README.md               # Documentación del repositorio



# PROYECTO_TIENDA
<img width="1365" height="767" alt="Captura de pantalla 2026-07-05 204442" src="https://github.com/user-attachments/assets/e9b4f5d2-ad0e-4ed1-bc9a-29dcfd8149de" />
<img width="1365" height="767" alt="Captura de pantalla 2026-07-05 204558" src="https://github.com/user-attachments/assets/c340cb01-3dfc-4f86-83af-79705d08a30e" />
<img width="1365" height="766" alt="Captura de pantalla 2026-07-05 204625" src="https://github.com/user-attachments/assets/fac938ca-7e80-4dc5-83e2-99aeb43a1021" />
