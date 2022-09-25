import os
from scanner import Scanner
contenido = ""


def Inicio():
    global contenido
    contenido += """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="shortcut icon" href="ico.png">
    <link rel="stylesheet" href="style.css">
    <title>Reporte de Operaciones</title>
    <script src="https://kit.fontawesome.com/eb496ab1a0.js" crossorigin="anonymous"></script>
</head>
<body>
    <div class="text-dark" style="background-color:#df2fb9">
        <div class="container px-4 text-center ">
            <div class="row gx-5">
                <div class="col">
                    <div style="background-color:#df2fb9">
                        <center>
                            <img src="ico.png" width="150" height="150">
                            <div style="background-color:#df2fb9">
                                <h1>Scanner-APP</h1>
                            </div>
                        </center>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="p-3 mb-2  text-dark" style="background-color:#8408f8">
        <div class="container  text-center">
            <div class="row gx-5">
                <div class="col">
                    <div class="p-3 mb-2 text-white" style="background-color:#8408f8">
                        <h1>
                            <center>Reporte de Operaciones</center>
                        </h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

def finish(operaciones):
    global contenido
    for operacion in operaciones:
        if operacion.texto == 'Suma':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Resta':
            contenido += """
            <div>
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Multiplicación':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Division':
            contenido += """
            <div>
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Potencia':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Raiz':
            contenido += """
            <div>
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Inverso':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(1)+str(operacion.tipo)+str(operacion.numeros[0])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Seno':
            contenido += """
            <div>
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Coseno':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Tangente':
            contenido += """
            <div>
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
        </h2>
    </div>"""
        elif operacion.texto == 'Mod':
            contenido += """
            <div style="background-color:#cefffb">
        <h1>
            Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
        </h1>
        <h2>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
        </h2>
    </div>"""
    contenido += """

<footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img src="xd.ico" alt="Loco Scanner-APP">
                    </a>
                </figure>
            </div>
            <div class="box">
                <br>
                <br>
                    <p>Nombre: Eduardo Josué González Cifuentes</p>
                    <p>Carnet: 201900647</p>
                    <p>Curso: Lenguajes Formales y De Programación</p>
                    <p>Secció: A-</p>
                    <p>Catedrático: Inga. Vivian Damaris Campos</p>
                    <p>Auxiliar: Mario Solis</p>
            </div>
            <div class="box">
                <figure>
                    <a href="#">
                        <a href="https://github.com/Lal0gg" target="_blank"> <img src="git.ico" alt="Loco Scanner-APP" alt="git-image"
                            width=100%>
                </figure>
            </div>
        </div>
        <div class="grupo-2">
            <small>
                <p>&copy; 2022 <b>Scanner-App</b> "- Todos Los Derechos Reservados"</p>
            </small>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>"""


def creararchivo():
    global contenido
    archivo = open('ReporteOpes.html', 'w', encoding='utf8')
    archivo.write(contenido)
    archivo.close()
    os.startfile("ReporteOpes.html")


def generararchivoOp(operaciones):
    Inicio()
    finish(operaciones)
    creararchivo()
