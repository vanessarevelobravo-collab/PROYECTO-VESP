# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

import os
import sqlite3

from Datos.registro_servicio import RegistroServicio

# Ruta de la base de datos: se crea automáticamente junto al proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "tienda.db")


class ServicioDAO:
    """Acceso a datos (SQLite) para los registros de servicio de la tienda."""

    @staticmethod
    def _conectar():
        conexion = sqlite3.connect(DB_PATH)
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS servicios (
                codigo      TEXT PRIMARY KEY,
                fecha       TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                email       TEXT NOT NULL
            )
            """
        )
        return conexion

    @staticmethod
    def insertar(registro: RegistroServicio) -> int:
        """Inserta un nuevo registro. Devuelve 1 si tuvo éxito, 0 si el código ya existe."""
        try:
            with ServicioDAO._conectar() as conexion:
                conexion.execute(
                    "INSERT INTO servicios (codigo, fecha, descripcion, email) VALUES (?, ?, ?, ?)",
                    (registro.codigo, registro.fecha, registro.descripcion, registro.email),
                )
                return 1
        except sqlite3.IntegrityError:
            return 0

    @staticmethod
    def actualizar(registro: RegistroServicio) -> int:
        """Actualiza un registro existente. Devuelve el número de filas afectadas."""
        with ServicioDAO._conectar() as conexion:
            cursor = conexion.execute(
                "UPDATE servicios SET fecha = ?, descripcion = ?, email = ? WHERE codigo = ?",
                (registro.fecha, registro.descripcion, registro.email, registro.codigo),
            )
            return cursor.rowcount

    @staticmethod
    def eliminar(codigo: str) -> int:
        """Elimina un registro por código. Devuelve el número de filas afectadas."""
        with ServicioDAO._conectar() as conexion:
            cursor = conexion.execute("DELETE FROM servicios WHERE codigo = ?", (codigo,))
            return cursor.rowcount

    @staticmethod
    def seleccionar_x_codigo(codigo: str):
        """Busca un registro por código. Devuelve un RegistroServicio o None."""
        with ServicioDAO._conectar() as conexion:
            cursor = conexion.execute(
                "SELECT codigo, fecha, descripcion, email FROM servicios WHERE codigo = ?",
                (codigo,),
            )
            fila = cursor.fetchone()
            if fila:
                codigo, fecha, descripcion, email = fila
                return RegistroServicio(codigo=codigo, descripcion=descripcion, fecha=fecha, email=email)
            return None

    @staticmethod
    def listar_todos():
        """Devuelve todos los registros almacenados."""
        with ServicioDAO._conectar() as conexion:
            cursor = conexion.execute("SELECT codigo, fecha, descripcion, email FROM servicios")
            return [
                RegistroServicio(codigo=c, descripcion=d, fecha=f, email=e)
                for c, f, d, e in cursor.fetchall()
            ]
