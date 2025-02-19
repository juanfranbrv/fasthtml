from fasthtml.common import *

# 1) Instanciamos la aplicación FastHTML
app, rt = fast_app()

# 2) Página principal (GET)
@rt("/")
def get():
    # Retornamos una página con título, formulario y varios botones
    return Titled("Demo FastHTML: Botones y Caja de Texto",
        Div(
            H2("Formulario de Ejemplo"),
            Form(action="/submit", method="post")(
                Label("Ingresa texto: "),
                Input(type="text", name="contenido", placeholder="Escribe algo aquí..."),
                Button("Enviar", type="submit"),
            ),
            H2("Botones de Ejemplo"),
            Div(
                # Cada botón hace un POST a una ruta diferente, y se actualiza en la misma página
                Button("Botón A", hx_post="/accionA", hx_target="#resultado"),
                Button("Botón B", hx_post="/accionB", hx_target="#resultado"),
                Button("Botón C", hx_post="/accionC", hx_target="#resultado"),
            ),
            Div(id="resultado")  # Aquí se mostrarán las respuestas
        )
    )

# 3) Manejo de formulario (POST)
@rt("/submit")
def post(contenido: str):
    # Muestra el texto enviado
    return P(f"Has enviado: {contenido}")

# 4) Manejo de botones (POST)
@rt("/accionA")
def post():
    return P("¡Has hecho clic en el Botón A!")

@rt("/accionB")
def post():
    return P("¡Has hecho clic en el Botón B!")

@rt("/accionC")
def post():
    return P("¡Has hecho clic en el Botón C!")

# 5) Arrancar la aplicación con Uvicorn
serve()
