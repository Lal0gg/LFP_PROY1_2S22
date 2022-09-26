import os
from scanner import Scanner
contenido = ""


def Inicio(color2, tamanio2):
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
                    <div class="p-3 mb-2 text-white" style="background-color:#d8bcf1">
                        <p>
                            <center>

                            <FONT SIZE="""+str(tamanio2)+""" COLOR="""
    if(color2 == 'AZUL'):
        contenido += """\"blue\""""
    elif(color2 == 'ROJO'):
        contenido += """\"red\""""
    elif(color2 == 'AMARILLO'):
        contenido += """\"yellow\""""
    elif(color2 == 'VERDE'):
        contenido += """\"green\""""
    elif(color2 == 'NEGRO'):
        contenido += """\"black\""""
    elif(color2 == 'ROSADO'):
        contenido += """\"magenta\""""
    elif(color2 == 'ANARANJADO'):
        contenido += """\"orange\""""
    elif(color2 == 'MORADO'):
        contenido += '"purple"'
    elif(color2 == 'TURQUESA'):
        contenido += """\"turquoise\""""
    elif(color2 == 'CYAN'):
        contenido += """\"cyan\""""
    elif(color2 == 'NARANJA'):
        contenido += """\"orange\""""
    elif(color2 == 'ROSA'):
        contenido += """\"magenta\""""
    elif(color2 == 'PURPURA'):
        contenido += """\"purple\""""
    elif(color2 == 'CAFE'):
        contenido += """\"brown\""""
    elif(color2 == 'GRIS'):
        contenido += """\"grey\""""
    contenido += """>"""+str('Reporte de Operaciones')+"""
    </FONT>
                            
                            
                            </center>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """


def desc(color1, tamanio1, descripcion):
    global contenido
    contenido += """
    <div>
    <FONT SIZE="""+str(tamanio1)+""" COLOR="""
    if(color1 == 'AZUL'):
        contenido += """\"blue\""""
    elif(color1 == 'ROJO'):
        contenido += """\"red\""""
    elif(color1 == 'AMARILLO'):
        contenido += """\"yellow\""""
    elif(color1 == 'VERDE'):
        contenido += """\"green\""""
    elif(color1 == 'NEGRO'):
        contenido += """\"black\""""
    elif(color1 == 'ROSADO'):
        contenido += """\"magenta\""""
    elif(color1 == 'ANARANJADO'):
        contenido += """\"orange\""""
    elif(color1 == 'MORADO'):
        contenido += '"purple"'
    elif(color1 == 'TURQUESA'):
        contenido += """\"turquoise\""""
    elif(color1 == 'CYAN'):
        contenido += """\"cyan\""""
    elif(color1 == 'NARANJA'):
        contenido += """\"orange\""""
    elif(color1 == 'ROSA'):
        contenido += """\"magenta\""""
    elif(color1 == 'PURPURA'):
        contenido += """\"purple\""""
    elif(color1 == 'CAFE'):
        contenido += """\"brown\""""
    elif(color1 == 'GRIS'):
        contenido += """\"grey\""""
    contenido += """>"""+str(descripcion.replace("\n", "<br>"))+"""
    </FONT>
    </div>
    """


def finish(operaciones, color, tamanio):
    global contenido
    for operacion in operaciones:
        contenido += """<div style="background-color:#cefffb" >
            <FONT SIZE="""+str(tamanio)+""" COLOR="""
        if(color == 'AZUL'):
            contenido += """\"blue\""""
        elif(color == 'ROJO'):
            contenido += """\"red\""""
        elif(color == 'AMARILLO'):
            contenido += """\"yellow\""""
        elif(color == 'VERDE'):
            contenido += """\"green\""""
        elif(color == 'NEGRO'):
            contenido += """\"black\""""
        elif(color == 'ROSADO'):
            contenido += """\"magenta\""""
        elif(color == 'ANARANJADO'):
            contenido += """\"orange\""""
        elif(color == 'MORADO'):
            contenido += '"purple"'
        elif(color == 'TURQUESA'):
            contenido += """\"turquoise\""""
        elif(color == 'CYAN'):
            contenido += """\"cyan\""""
        elif(color == 'NARANJA'):
            contenido += """\"orange\""""
        elif(color == 'ROSA'):
            contenido += """\"magenta\""""
        elif(color == 'PURPURA'):
            contenido += """\"purple\""""
        elif(color == 'CAFE'):
            contenido += """\"brown\""""
        elif(color == 'GRIS'):
            contenido += """\"grey\""""
        contenido += """>"""
        if operacion.texto == 'Suma':
            contenido += """

            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
            """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
                
            </p>
            </FONT>

        </div>"""
        elif operacion.texto == 'Resta':
            contenido += """
                <div style="background-color:#ffffff">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Multiplicación':
            contenido += """
                <div style="background-color:#cefffb">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Division':
            contenido += """
                <div style="background-color:#ffffff">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Potencia':
            contenido += """
                <div style="background-color:#cefffb">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Raiz':
            contenido += """
                <div style="background-color:#ffffff">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Inverso':
            contenido += """
                <div style="background-color:#cefffb">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(1)+str(operacion.tipo)+str(operacion.numeros[0])+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Seno':
            contenido += """
                <div style="background-color:#ffffff">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Coseno':
            contenido += """
                <div style="background-color:#cefffb">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Tangente':
            contenido += """
                <div style="background-color:#ffffff">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.tipo)+str('(')+str(operacion.numeros[0])+str(')')+"="+str(operacion.total)+"""
            </p>
            </FONT>
        </div>"""
        elif operacion.texto == 'Mod':
            contenido += """
                <div style="background-color:#cefffb">
            <p>
                Operacion """+str(operacion.texto)+""" """+str(operacion.contador)+""":
            </p>
            <p>
                """+str(operacion.numeros[0])+str(operacion.tipo)+str(operacion.numeros[1])+"="+str(operacion.total)+"""
            </p>
    </FONT>
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


def generararchivoOp(operaciones, color, tamanio, color1, tamanio1, descripcion, color2, tamanio2):
    Inicio(color2, tamanio2)
    desc(color1, tamanio1, descripcion)
    finish(operaciones, color, tamanio)
    creararchivo()
