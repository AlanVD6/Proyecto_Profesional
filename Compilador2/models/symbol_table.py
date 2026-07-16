"""
models/symbol_table.py
------------------------
Tabla de simbolos con soporte de ambitos anidados (ambito global + un
ambito nuevo por cada funcion). Se usa durante el analisis semantico
para saber si una variable fue declarada antes de usarse, y para
registrar las funciones definidas por el usuario junto con su numero
de parametros.
"""


class Ambito:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.simbolos = set()

    def definir(self, nombre):
        self.simbolos.add(nombre)

    def resolver(self, nombre):
        """Busca el simbolo en este ambito y, si no esta, en los
        ambitos superiores (encadenamiento lexico)."""
        ambito = self
        while ambito is not None:
            if nombre in ambito.simbolos:
                return ambito
            ambito = ambito.padre
        return None


class TablaSimbolos:
    FUNCIONES_INTEGRADAS = {
        "print": None,   # acepta cualquier numero de argumentos
        "range": None,   # acepta 1 a 3 argumentos
        "len": 1,
        "int": 1,
        "float": 1,
        "str": 1,
        "bool": 1,
    }

    def __init__(self):
        self.ambito_global = Ambito("global")
        self.ambito_actual = self.ambito_global
        self.funciones = {}  # nombre -> numero de parametros

    def apilar_ambito(self, nombre):
        self.ambito_actual = Ambito(nombre, padre=self.ambito_actual)
        return self.ambito_actual

    def desapilar_ambito(self):
        if self.ambito_actual.padre is not None:
            self.ambito_actual = self.ambito_actual.padre

    def definir_variable(self, nombre):
        self.ambito_actual.definir(nombre)

    def esta_definida(self, nombre):
        return self.ambito_actual.resolver(nombre) is not None

    def definir_funcion(self, nombre, num_parametros):
        ya_existia = nombre in self.funciones
        self.funciones[nombre] = num_parametros
        return ya_existia

    def es_funcion(self, nombre):
        return nombre in self.funciones or nombre in self.FUNCIONES_INTEGRADAS

    def num_parametros_funcion(self, nombre):
        if nombre in self.funciones:
            return self.funciones[nombre]
        return self.FUNCIONES_INTEGRADAS.get(nombre, None)

    def todos_los_nombres_variables(self):
        return sorted(self.ambito_global.simbolos)

    def todos_los_nombres_funciones(self):
        return sorted(self.funciones.keys())
