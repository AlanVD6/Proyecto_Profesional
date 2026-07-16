# PyLite Compiler

Aplicación web en **Flask (arquitectura MVC)** que analiza archivos de código
fuente en **PyLite**, un subconjunto práctico de Python, a través de sus tres
fases clásicas: **análisis léxico**, **análisis sintáctico** (con **ANTLR4**)
y **análisis semántico** (con el patrón **Visitor**).

---

## 1. Alcance del lenguaje (PyLite)

Escribir un compilador para el 100% de Python (con su tipado dinámico,
comprensiones, decoradores, `async`, etc.) no es viable como base para un
análisis semántico significativo dentro de un proyecto de curso. Por eso se
definió **PyLite**, un subconjunto real y ejecutable a mano que cubre lo más
representativo del lenguaje:

| Categoría | Soportado |
|---|---|
| Asignación | `x = 5`, `x += 1`, `-=`, `*=`, `/=` |
| Tipos de dato | enteros, flotantes, cadenas, `True`/`False`/`None` |
| Expresiones | aritméticas (`+ - * / // % **`), relacionales (`== != < > <= >=`), lógicas (`and or not`), paréntesis |
| Control de flujo | `if` / `elif` / `else`, `while`, `for x in range(...)` |
| Funciones | `def nombre(params):`, `return`, llamadas anidadas |
| Otras sentencias | `pass`, `break`, `continue`, comentarios `#` |
| Bloques | **por indentación real**, igual que Python (vía tokens `INDENT`/`DEDENT`) |

No soportado por el **parser** (aunque el **lexer** ya los reconoce como
palabras reservadas, ver sección 3.4): `class`, `import`, `try/except`,
`lambda`, `with`, `async/await`, `yield`, listas/diccionarios como literal,
f-strings, anotaciones de tipo. Si se usan, el analizador se detiene
correctamente en la **fase sintáctica** indicando que el token es válido
léxicamente pero no está contemplado por la gramática de PyLite.

---

## 2. Arquitectura MVC

```
pyLiteCompiler/
├── app.py                        # Punto de entrada (crea Flask, registra generated/ en sys.path)
├── config.py                     # Configuración centralizada
│
├── models/                       # MODELO: lógica de negocio, sin HTTP
│   ├── analysis_result.py        #   Estructuras de datos del resultado
│   ├── error_listener.py         #   ErrorListeners de ANTLR (léxico/sintáctico)
│   ├── symbol_table.py           #   Tabla de símbolos con ámbitos anidados
│   ├── semantic_visitor.py       #   Analizador semántico (hereda de PyLiteParserVisitor)
│   └── compiler_service.py       #   Orquesta las 3 fases en orden
│
├── controllers/                  # CONTROLADOR: rutas HTTP
│   └── analysis_controller.py    #   GET / , POST /api/analyze
│
├── views/templates/              # VISTA: Jinja2 (HTML)
│   └── index.html
│
├── static/                       # CSS y JS nativos (sin frameworks)
│   ├── css/style.css
│   └── js/main.js                #   AJAX (fetch), barra de progreso
│
├── grammar/                      # Gramática ANTLR (fuente)
│   ├── PyLiteLexer.g4             #   Catálogo completo de tokens (ver 3.4)
│   ├── PyLiteParser.g4            #   Gramática simplificada (expr recursiva)
│   └── PyLiteLexerBase.py         #   Manejo de INDENT/DEDENT (código propio)
│
├── generated/                    # Código Python generado por ANTLR
├── uploads/                      # Copia de los archivos analizados
├── build_grammar.ps1             # Script para regenerar generated/ en Windows
└── requirements.txt
```

**Separación de responsabilidades:**
- Las **vistas** solo contienen HTML/Jinja2 y no saben nada de ANTLR.
- El **controlador** (`analysis_controller.py`) solo traduce HTTP ⇄ Python: no
  contiene ni una línea de lógica de análisis.
- El **modelo** concentra toda la inteligencia del compilador y podría
  reutilizarse tal cual en una CLI, una API distinta, o pruebas unitarias,
  sin tocar Flask.

---

## 3. Las tres fases (`models/compiler_service.py`)

```
archivo subido
      │
      ▼
┌─────────────────┐   error léxico    ┌──────────────────────────┐
│  1. FASE LÉXICA  │ ────────────────▶ │ se detiene aquí, reporta │
│  PyLiteLexer     │                   │ fase="lexico" + detalle  │
└────────┬─────────┘                   └──────────────────────────┘
         │ ok
         ▼
┌─────────────────────┐  error sintáctico ┌──────────────────────────┐
│ 2. FASE SINTÁCTICA   │ ─────────────────▶│ se detiene aquí, reporta │
│ PyLiteParser         │                   │ fase="sintactico"        │
└────────┬─────────────┘                   └──────────────────────────┘
         │ ok (árbol de análisis construido)
         ▼
┌─────────────────────┐  error semántico  ┌──────────────────────────┐
│ 3. FASE SEMÁNTICA    │ ─────────────────▶│ se detiene aquí, reporta │
│ SemanticVisitor      │                   │ fase="semantico"         │
└────────┬─────────────┘                   └──────────────────────────┘
         │ ok
         ▼
    resultado exitoso
 (tokens, funciones, variables, árbol)
```

Si una fase falla, **no se ejecutan las siguientes**: el backend captura la
excepción/errores propios de esa fase y responde con la fase exacta y el
motivo, tal como pide el requerimiento.

### 3.1 Fase léxica
`PyLiteLexer` (generado por ANTLR) tokeniza el archivo. Un
`LexicalErrorListener` (en `models/error_listener.py`) reemplaza al listener
por omisión de ANTLR (que solo imprime a consola) y en su lugar acumula cada
carácter no reconocido como un `CompilerError` con línea/columna/mensaje.

### 3.2 Fase sintáctica
`PyLiteParser` construye el árbol de análisis a partir de los tokens. Un
`SyntacticErrorListener` captura violaciones de la gramática: falta de `:`,
paréntesis sin cerrar, indentación inconsistente, tokens inesperados, etc.

### 3.3 Fase semántica
`SemanticVisitor` (en `models/semantic_visitor.py`) **hereda directamente**
de `PyLiteParserVisitor` (la clase generada por ANTLR) y solo sobreescribe
los métodos `visitXxx` donde hay algo que validar; en el resto de los nodos
el propio Visitor generado recorre el árbol automáticamente. Usa una
**tabla de símbolos con ámbitos anidados** (`models/symbol_table.py`: un
ámbito global + un ámbito nuevo por cada función). Reglas implementadas:

| Código | Regla |
|---|---|
| SEM01 | Variable usada sin haber sido declarada/asignada antes |
| SEM02 | `+=`/`-=`/... sobre una variable inexistente |
| SEM03 | Llamada a una función que no existe |
| SEM04 | Número de argumentos distinto al declarado |
| SEM05 | Redefinición de una función ya declarada |
| SEM06 | `return` fuera de una función |
| SEM07 | `break`/`continue` fuera de un bucle |
| SEM08 | División/módulo entre una constante `0` (detectable estáticamente) |

### 3.4 Catálogo completo de tokens reconocidos por el lexer

Siguiendo el informe de investigación, `PyLiteLexer.g4` cataloga **todos**
los tokens léxicos reales de Python, aunque el **parser** solo utilice un
subconjunto de ellos (el resto queda "reservado": el lexer los reconoce
correctamente, pero usarlos en una posición no soportada produce un error
en la fase **sintáctica**, nunca en la léxica):

- **Palabras reservadas (35):** `False await else import pass None break
  except in raise True class finally is return and continue for lambda
  try as def from nonlocal while assert del global not with async elif
  if or yield`
- **Operadores aritméticos:** `+ - * / // % **`
- **Operadores de comparación:** `== != < > <= >=`
- **Operadores de asignación:** `= += -= *= /= //= %= **= &= |= ^= >>= <<=` y el operador morsa `:=`
- **Operadores a nivel de bits:** `& | ^ ~ << >>`
- **Delimitadores:** `( ) [ ] { } , : . ; @ ...`
- **Identificadores y literales:** `NAME`, `INT`, `FLOAT`, `STRING`

### 3.5 Gramática de expresiones simplificada

En vez de encadenar varias reglas de precedencia (`orExpr → andExpr → ... →
atom`), `PyLiteParser.g4` usa **una sola regla `expr` recursiva** con
alternativas etiquetadas, igual que en los ejercicios sencillos de ANTLR
(por ejemplo, una calculadora). ANTLR resuelve la precedencia
automáticamente según el **orden** de las alternativas (las de arriba se
aplican primero):

```antlr
expr
    : expr LPAREN argList? RPAREN                          # callExpr
    | expr LBRACKET expr RBRACKET                          # indexExpr
    | <assoc=right> expr STAR STAR expr                    # powerExpr
    | (PLUS | MINUS) expr                                  # unaryExpr
    | expr (STAR | SLASH | DOUBLESLASH | PERCENT) expr     # mulExpr
    | expr (PLUS | MINUS) expr                             # addExpr
    | expr (EQ | NEQ | LT | GT | LE | GE) expr              # compareExpr
    | NOT expr                                              # notExpr
    | expr AND expr                                         # andExpr
    | expr OR expr                                          # orExpr
    | atom                                                  # atomExpr
    ;
```

Esto reduce la gramática de 8 reglas anidadas a 1, y el Visitor semántico
puede sobreescribir directamente `visitCallExpr`, `visitMulExpr`, etc., sin
necesidad de navegar manualmente por una cadena larga de sub-reglas.

---

## 4. Frontend (AJAX + barra de progreso)

`static/js/main.js` envía el archivo con `fetch` + `FormData` a
`POST /api/analyze` **sin recargar la página**. Mientras la petición está en
vuelo, anima una barra de progreso por etapas (subida → léxico → sintáctico →
semántico); al llegar la respuesta, salta directamente a la etapa real en la
que el análisis se detuvo (o al 100% si todo fue exitoso) y pinta el
contenedor de resultados en la parte inferior con:

- Si hay éxito: cantidad de tokens, nodos del árbol, funciones y variables
  detectadas, y una vista previa del árbol sintáctico.
- Si hay error: la fase exacta y, por cada error, línea, columna y mensaje.

---

## 5. Cómo ejecutar el proyecto

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate        # Windows PowerShell
# source venv/bin/activate   # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python app.py
```

Abre `http://127.0.0.1:5000/` en el navegador, sube un archivo `.py` y pulsa
**Analizar código**.

> El código ya viene generado dentro de `generated/`, así que **no necesitas
> tener Java ni ANTLR instalados para ejecutar la app**. Solo los necesitas si
> vas a **modificar la gramática** (`grammar/*.g4`).

---

## 6. Cómo regenerar la gramática (si la modificas)

Ya tienes ANTLR en `D:\Automatas ll\ANTLR\antlr-4.13.2-complete.jar`, así que
basta con correr, desde la raíz del proyecto, en PowerShell:

```powershell
.\build_grammar.ps1
```

Esto vuelve a generar `PyLiteLexer.py`, `PyLiteParser.py` y
`PyLiteParserVisitor.py` dentro de `generated/`. Si tu jar está en otra ruta,
edita la variable `$AntlrJar` al inicio del script.

Comando equivalente manual (por si prefieres ejecutarlo tú mismo):

```powershell
cd grammar
java -jar "D:\Automatas ll\ANTLR\antlr-4.13.2-complete.jar" -Dlanguage=Python3 -visitor -no-listener -o ..\generated PyLiteLexer.g4
java -jar "D:\Automatas ll\ANTLR\antlr-4.13.2-complete.jar" -Dlanguage=Python3 -visitor -no-listener -o ..\generated -lib ..\generated PyLiteParser.g4
cd ..
copy grammar\PyLiteLexerBase.py generated\PyLiteLexerBase.py
```

---

## 7. Manejo de la indentación (INDENT/DEDENT)

ANTLR trabaja de forma nativa con gramáticas libres de contexto, pero la
sintaxis de Python **no es** libre de contexto en sentido estricto: el
significado de un bloque depende de su nivel de sangría, algo que un lexer
"puro" no puede resolver por sí solo.

La solución, implementada en `grammar/PyLiteLexerBase.py` (clase base del
lexer generado), sigue la técnica estándar usada por la gramática oficial
`Python3` del repositorio `antlr/grammars-v4`:

1. Se mantiene una pila de niveles de indentación abiertos.
2. La regla léxica `NEWLINE` captura el salto de línea real **más** los
   espacios/tabs de la línea siguiente.
3. Se compara ese ancho contra la cima de la pila para decidir si hay que
   insertar un token sintético `INDENT`, uno o varios `DEDENT`, o ninguno.
4. Las líneas en blanco y los comentarios no disparan cambios de
   indentación.
5. Dentro de paréntesis/corchetes abiertos, los saltos de línea se ignoran
   (igual que en Python real).

El detalle completo está documentado como comentarios dentro del propio
archivo `PyLiteLexerBase.py`.

---

## 8. Ejemplos de prueba

**Éxito** (`ejemplos/factorial.py` — inclúyelo tú mismo para probar):
```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

**Error léxico** (carácter fuera del catálogo de Python):
```python
x = 5
y = x $ 3
```

**Error sintáctico** (falta `:`):
```python
if x > 3
    print(x)
```

**Error semántico** (variable no declarada):
```python
x = 5
print(y)
```

---

## 9. Posibles extensiones futuras

- Soporte de listas `[1, 2, 3]` como literal (no solo indexación).
- Anotaciones de tipo (`x: int = 5`) para una inferencia de tipos más rica.
- Tabla de símbolos exportable como JSON descargable desde la interfaz.
- Resaltado de la línea con error directamente sobre el código fuente en la
  vista de resultados.
