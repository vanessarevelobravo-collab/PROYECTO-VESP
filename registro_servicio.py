# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

from Datos.servicio_tienda import ServicioTienda


class RegistroServicio(ServicioTienda):
    """Representa un registro simple de servicio capturado desde el
    formulario principal (codigo, fecha, descripcion, email del cliente).

    Hereda de ServicioTienda para reutilizar la validación de
    codigo / descripcion / fecha, y agrega el correo del cliente
    asociado a la solicitud."""

    def __init__(self, codigo, descripcion, fecha, email):
        super().__init__(codigo, descripcion, fecha)
        self.email = email  # usa setter con validación

    # --- email ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor or "@" not in valor:
            raise ValueError("El email no es válido.")
        self._email = valor

    # --- Implementación de métodos polimórficos ---
    def calcular_costo(self):
        """Este tipo de registro no tiene costo asociado."""
        return 0.0

    def mostrar_info(self):
        return (f"REGISTRO | Código: {self._codigo} | Fecha: {self._fecha} | "
                f"Descripción: {self._descripcion} | Email: {self._email}")

    def __str__(self):
        return super().__str__() + f" | Email: {self._email}"
