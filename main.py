from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Información sobre los principios básicos de Python
principios_basicos = {
    "variables": {
        "descripcion": "Las variables son contenedores para almacenar datos.",
        "ejemplo": "x = 5"
    },
    "tipos_de_datos": {
        "descripcion": "Python tiene varios tipos de datos estándar: enteros, flotantes, cadenas, listas, tuplas, diccionarios, etc.",
        "ejemplo": "x = 5\ny = 3.14\nnombre = 'Juan'\nlista = [1, 2, 3]\ntupla = (4, 5, 6)\ndiccionario = {'clave': 'valor'}"
    },
    "operadores_aritmeticos": {
        "descripcion": "Python soporta operadores aritméticos como suma (+), resta (-), multiplicación (*), división (/), etc.",
        "ejemplo": "x = 10\ny = 3\nsuma = x + y\nresta = x - y\nmultiplicacion = x * y\ndivision = x / y"
    },
    "operadores_logicos": {
        "descripcion": "Python tiene operadores lógicos como AND, OR y NOT.",
        "ejemplo": "a = True\nb = False\nresultado_and = a and b\nresultado_or = a or b\nresultado_not = not a"
    },
    # Agrega más principios básicos con descripción y ejemplos aquí
}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
    <head>
        <title>Principios Básicos de Python</title>
    </head>
    <body>
        <h1>Principios Básicos de Python</h1>
        <ul>
            <li><a href="/principio/variables">Variables</a></li>
            <li><a href="/principio/tipos_de_datos">Tipos de Datos</a></li>
            <li><a href="/principio/operadores_aritmeticos">Operadores Aritméticos</a></li>
            <li><a href="/principio/operadores_logicos">Operadores Lógicos</a></li>
            <li><a href="/principio/operadores_comparativos">Operadores Comparativos</a></li>
            <li><a href="/principio/operadores_asignacion">Operadores de Asignación</a></li>
            <li><a href="/principio/funciones">Funciones</a></li>
            <li><a href="/principio/ciclos">Ciclos</a></li>
            <li><a href="/principio/condiciones">Condiciones</a></li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/principio/{concepto}", response_class=HTMLResponse)
async def read_concept(concepto: str):
    if concepto in principios_basicos:
        html_content = f"""
        <html>
        <head>
            <title>{concepto.replace('_', ' ').title()}</title>
        </head>
        <body>
            <h1>{concepto.replace('_', ' ').title()}</h1>
            <p>{principios_basicos[concepto]}</p>
        </body>
        </html>
        """
        return HTMLResponse(content=html_content, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Concepto no encontrado")



