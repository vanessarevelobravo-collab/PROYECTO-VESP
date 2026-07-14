
# - REVELO BRAVO GENESIS VANESSA 
# - VAQUE REYES DANIELA DESIREE

class ClienteOnline:
    """Representa un cliente registrado en la tienda online."""

    def __init__(self, id_cliente, nombre, email, es_premium=False):
        self._id_cliente = id_cliente
        self.nombre = nombre        # usa setter con validación
        self.email = email          # usa setter con validación
        self._es_premium = es_premium
        self._servicios = []        # lista de servicios asociados al cliente

    # --- id_cliente ---
    @property
    def id_cliente(self):
        return self._id_cliente

    # --- nombre ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._nombre = valor

    # --- email ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor or "@" not in valor:
            raise ValueError("El email no es válido.")
        self._email = valor

    # --- es_premium ---
    @property
    def es_premium(self):
        return self._es_premium

    @es_premium.setter
    def es_premium(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("es_premium debe ser True o False.")
        self._es_premium = valor

    # --- servicios ---
    def agregar_servicio(self, servicio):
        self._servicios.append(servicio)

    def listar_servicios(self):
        if not self._servicios:
            print(f"  El cliente {self._nombre} no tiene servicios registrados.")
        for s in self._servicios:
            print(f"  {s}")

    def total_gastado(self):
        return round(sum(s.calcular_costo() for s in self._servicios), 2)

    def __str__(self):
        tipo = "PREMIUM" if self._es_premium else "Regular"
        return (f"Cliente [{tipo}] ID: {self._id_cliente} | "
                f"Nombre: {self._nombre} | Email: {self._email} | "
                f"Total gastado: ${self.total_gastado():.2f}")
