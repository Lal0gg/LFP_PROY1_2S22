from cmath import cos, sin, tan
from Clases import Error
from Clases import Token
from operacion import Operacion
import math
# alfabeto = {letras}, {numeros}, <, >, /, ., =, [, ], {colores}, {signos}


class Scanner:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.signos=['?','¿','¡','!','.',',',':',';']
        self.colores=['AZUL','ROJO','AMARILLO', 'VERDE','NEGRO', 'ROSADO', 'ANARANJADO', 'MORADO','TURQUESA','CYAN','NARANJA','ROSA','PURPURA','CAFÉ','CAFE','GRIS']
        self.contador= 0
        self.operaciones = []
        self.contadors=0
        self.contadorr=0
        self.contadorm=0
        self.contadord=0
        self.contadorp=0
        self.contadorra=0
        self.contadori=0
        self.contadorsen=0
        self.contadorcos=0
        self.contadortan=0
        self.contadormod=0
        
    def analyze(self,contenido):
        self.listaTokens = []
        self.listaErrores = []
        try :
            if (self.listaTokens and self.listaErrores) !=  None:
                contenido += '$'
                line = 1
                column =1
                indexx = 0
                buffer =""
                state= 'q_0'
                while indexx < len(contenido):
                    caracter = contenido[indexx]
                    if state ==  'q_0':
                        if caracter == '=':
                            buffer= caracter
                            column +=1
                            self.listaTokens.append(Token(buffer,'TK_IGUAL', line,column))
                            buffer=''
                            state = 'q_0'
                        elif caracter == '<':
                            buffer = caracter
                            column+=1
                            self.listaTokens.append(Token(buffer,'TK_MENOR_QUE',line,column))
                            buffer=''
                            state='q_0'
                        elif caracter == '>':
                            buffer = caracter
                            column+=1
                            self.listaTokens.append(Token(buffer,'TK_MAYOR_QUE',line,column))
                            buffer=''
                            state='q_0'
                        elif caracter =='/':
                            buffer = caracter
                            column+=1
                            self.listaTokens.append(Token(buffer,'Tk_DIAGONAL',line,column))
                            buffer=''
                            state='q_0'
                        elif caracter =='[':
                            buffer = caracter
                            column+=1
                            self.listaTokens.append(Token(buffer,'Tk_CORCHETE_E',line,column))
                            buffer=''
                            state='q_0'
                        elif caracter ==']':
                            buffer = caracter
                            column+=1
                            self.listaTokens.append(Token(buffer,'Tk_CORCHETE_S',line,column))
                            buffer=''
                            state='q_0'
                        elif caracter .isalpha() and (not caracter.isdigit()):
                            buffer = caracter
                            column+=1
                            state ='q_1'
                        elif caracter == '\n':
                            column = 1
                            line += 1
                        elif caracter == ' ':
                            column += 1
                        elif caracter == '\t':
                            column += 1
                        elif caracter.isdigit():
                            buffer = caracter
                            column += 1
                            state = 'q_2'
                        # elif caracter == '"':
                        #     buffer = caracter
                        #     column += 1
                        #     state = 'q_4'
                        elif caracter in self.colores:
                            buffer = caracter
                            column+=1
                            state='q_5'
                        elif caracter == '$':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(Token(buffer, '¡FINISH HIM!' , line, column))
                            buffer = ''
                            state ='q_0'
                            print('Análisis Exitoso')
                        else:
                            self.listaErrores.append(Error(caracter, "ERROR", 'No es reconocido Como Token de Este Lenguaje', line, column)) 
                            buffer = ''
                            column += 1
                    elif state =='q_1':
                        if caracter.isalpha() and (not caracter.isdigit()):
                            buffer += caracter
                            column += 1
                            state ='q_1'
                        else:
                            if buffer.upper() == 'TIPO':
                                self.listaTokens.append(Token(buffer, 'TK_TIPO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'OPERACION':
                                self.listaTokens.append(Token(buffer, 'TK_OPERACION', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'OPERACIONES':
                                self.listaTokens.append(Token(buffer, 'TK_OPERACIONES', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'COMPLEJAS':
                                self.listaTokens.append(Token(buffer, 'TK_COMPLEJAS', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'SIMPLES':
                                self.listaTokens.append(Token(buffer, 'TK_SIMPLES', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'NUMERO':
                                self.listaTokens.append(Token(buffer, 'TK_NUMERO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'TEXTO':
                                self.listaTokens.append(Token(buffer, 'TK_R_TEXTO_', line, column))
                                buffer =''
                                if contenido[indexx]=='>' and contenido[indexx-6]!='/':
                                    buffer+=caracter
                                    self.listaTokens.append(Token(buffer, 'TK_MAYOR_QUE', line, column))
                                    buffer =''
                                indexx+=1
                                state= 'q_4'
                            elif buffer.upper() == 'FUNCION':
                                self.listaTokens.append(Token(buffer, 'TK_FUNCION', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'TITULO':
                                self.listaTokens.append(Token(buffer, 'TK_TITULO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'DESCRIPCION':
                                self.listaTokens.append(Token(buffer, 'TK_DESCRIPCION', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'CONTENIDO':
                                self.listaTokens.append(Token(buffer, 'TK_CONTENIDO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'ESTILO':
                                self.listaTokens.append(Token(buffer, 'TK_ESTILO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'COLOR':
                                self.listaTokens.append(Token(buffer, 'TK_R_COLOR_', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'TAMANIO':
                                self.listaTokens.append(Token(buffer, 'TK_TAMANIO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer.upper() == 'SUMA':
                                self.listaTokens.append(Token(buffer, 'TK_SUMA', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'RESTA':
                                self.listaTokens.append(Token(buffer, 'TK_RESTA', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'MULTIPLICACION':
                                self.listaTokens.append(Token(buffer, 'TK_MULTIPLICACION', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'DIVISION':
                                self.listaTokens.append(Token(buffer, 'TK_DIVISION', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'POTENCIA':
                                self.listaTokens.append(Token(buffer, 'TK_POTENCIA', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'RAIZ':
                                self.listaTokens.append(Token(buffer, 'TK_RAIZ', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'INVERSO':
                                self.listaTokens.append(Token(buffer, 'TK_INVERSO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'SENO':
                                self.listaTokens.append(Token(buffer, 'TK_SENO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'COSENO':
                                self.listaTokens.append(Token(buffer, 'TK_COSENO', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'TANGENTE':
                                self.listaTokens.append(Token(buffer, 'TK_TANGENTE', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'MOD':
                                self.listaTokens.append(Token(buffer, 'TK_MOD', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer == 'ESCRIBIR':
                                self.listaTokens.append(Token(buffer, 'TK_ESCRIBIR', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            elif buffer in self.colores:
                                self.listaTokens.append(Token(buffer, 'TK_COLOR', line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                            else:
                                self.listaErrores.append(Error(buffer,  'ERROR',"No Es Reconocido Como Token de Este Lenguaje", line, column))
                                buffer=''
                                state='q_0'
                                indexx-=1
                                
                                
                    elif state =='q_2':
                        if caracter.isdigit():
                            buffer += caracter 
                            column +=1
                            state = 'q_2'
                        elif caracter =='.':
                            buffer += caracter 
                            column +=1
                            state = 'q_3'
                        else:
                            self.listaTokens.append(Token(buffer, 'TK_ENTERO', line, column))
                            buffer = ''
                            indexx -= 1
                            state='q_0'
                    elif state =='q_3':
                        if caracter.isdigit():
                            buffer += caracter 
                            column +=1
                            state = 'q_3'
                        else:
                            self.listaTokens.append(Token(buffer, 'TK_DECIMAL', line, column))
                            buffer = ''
                            indexx -= 1
                            state='q_0'
                    elif state == 'q_4':
                        if caracter== '<':
                            column += 1
                            self.listaTokens.append(Token(buffer, 'TK_CONTENIDO_TXT', line, column))
                            buffer = ''
                            state = 'q_0'
                            indexx-=1
                        elif caracter =='\n':
                            column = 1
                            line += 1
                        else:
                            buffer += caracter
                            column += 1
                            state = 'q_4'
                    indexx +=1
                print("Operaicone: " + str(self.contador))
            else:
                print("No se puede analizar")
        except:
            pass


    def printScannergg(self):
        print("__________ T O K E N S __________")
        for token in self.listaTokens:
            token.getInfoTokens()
        print()
        print("__________ E R R O R E S __________")
        for token in self.listaErrores:
            token.getInfoErrores()
        print()

    def printList(self):
        print("_________________L I S T  A T O K E N S________________")
        for token in self.listaTokens:
            token.getToken()
        print()

    def Operar(self):
        contador = 1
        for i in range(len(self.listaTokens)):
            if  self.listaTokens[i].tipo == 'TK_OPERACION':
                #print(i.tipo + " | Lexema " + i.lexeme)
                t1 = self.listaTokens[i+2]
                contador = i+5
                listaNums = []
                while self.listaTokens[contador].tipo== 'TK_NUMERO':
                    listaNums.append(self.listaTokens[contador+2])
                    contador+=8
                if t1.lexeme == 'SUMA':
                    if t1.lexeme== 'SUMA':
                        self.contadors+=1
                    listaSumasSimps =[]
                    Ope = Operacion('+')
                    total = 0
                    for j in range (len(listaNums)):
                        listaSumasSimps.append(float(listaNums[j].lexeme))
                    print('Suma: ',listaSumasSimps)
                    suma= listaSumasSimps[0]+listaSumasSimps[1]
                    Ope.numeros=listaSumasSimps
                    Ope.total=suma
                    Ope.contador =self.contadors
                    Ope.texto='Suma'
                    self.operaciones.append(Ope)
                    print("Resultado: " + str(suma))
                    print('Número de Sumas: ',self.contadors)
                elif t1.lexeme == 'RESTA':
                    if t1.lexeme== 'RESTA':
                        self.contadorr+=1
                    listaRestasSimps=[]
                    Ope1 = Operacion('-')
                    tot = 0
                    for x in range (len(listaNums)):
                        listaRestasSimps.append(float(listaNums[x].lexeme))
                    print('Resta: ',listaRestasSimps)
                    print('Número de Restas: ',self.contadorr)
                    resta= listaRestasSimps[0]-listaRestasSimps[1]
                    Ope1.numeros=listaRestasSimps
                    Ope1.total=resta
                    Ope1.contador=self.contadorr
                    Ope1.texto='Resta'
                    self.operaciones.append(Ope1)
                    print("Resultado: " + str(resta))
                elif t1.lexeme == 'MULTIPLICACION':
                    if t1.lexeme== 'MULTIPLICACION':
                        self.contadorm+=1
                    listaMultiSimps=[]
                    Ope2=Operacion('x')
                    tot2 = 0
                    for y in range (len(listaNums)):
                        listaMultiSimps.append(float(listaNums[y].lexeme))
                    print('Multi: ',listaMultiSimps)
                    print('Número de Multi: ',self.contadorm)
                    multi= listaMultiSimps[0]*listaMultiSimps[1]
                    Ope2.numeros=listaMultiSimps
                    Ope2.total=multi
                    Ope2.contador =self.contadorm
                    Ope2.texto='Multiplicación'
                    self.operaciones.append(Ope2)
                    print("Resultado: " + str(multi))
                elif t1.lexeme == 'DIVISION':
                    if t1.lexeme== 'DIVISION':
                        self.contadord+=1
                    listaDivSimps=[]
                    Op3=Operacion('/')
                    tot2 = 0
                    for ewe in range (len(listaNums)):
                        listaDivSimps.append(float(listaNums[ewe].lexeme))
                    print('Divison: ',listaDivSimps)
                    print('Número de Div: ',self.contadord)
                    div= listaDivSimps[0]/listaDivSimps[1]
                    Op3.numeros=listaDivSimps
                    Op3.total=div
                    Op3.contador=self.contadord
                    Op3.texto='Division'
                    self.operaciones.append(Op3)
                    print("Resultado: " + str(div))
                elif t1.lexeme == 'POTENCIA':
                    if t1.lexeme== 'POTENCIA':
                        self.contadorp+=1
                    listaPotenciaSimps=[]
                    Op4=Operacion('^')
                    tot2 = 0
                    for uwu in range (len(listaNums)):
                        listaPotenciaSimps.append(float(listaNums[uwu].lexeme))
                    print('Potencia: ' ,listaPotenciaSimps)
                    pot= pow(listaPotenciaSimps[0],listaPotenciaSimps[1])
                    Op4.numeros=listaPotenciaSimps
                    Op4.total=pot
                    Op4.contador=self.contadorp
                    Op4.texto='Potencia'
                    self.operaciones.append(Op4)
                    print("Resultado: " + str(pot))
                    print('Número de Potencia: ',self.contadorp)
                elif t1.lexeme == 'RAIZ':
                    if t1.lexeme== 'RAIZ':
                        self.contadorra+=1
                    listaRaizSimps=[]
                    Op5=Operacion('√')
                    tot2 = 0
                    for e in range (len(listaNums)):
                        listaRaizSimps.append(float(listaNums[e].lexeme))
                    print('Raiz: ' ,listaRaizSimps)
                    raiz = pow(listaRaizSimps[1],(1/(listaRaizSimps[0])))
                    Op5.numeros=listaRaizSimps
                    Op5.total=raiz
                    Op5.contador=self.contadorra
                    Op5.texto='Raiz'
                    self.operaciones.append(Op5)
                    print("Resultado: " + str(raiz))
                    print('Número de Raiz: ',self.contadorra)
                elif t1.lexeme == 'INVERSO':
                    if t1.lexeme== 'INVERSO':
                        self.contadori+=1
                    listaInversoSimps=[]
                    Op6=Operacion('/')
                    tot2 = 0
                    for xd in range (len(listaNums)):
                        listaInversoSimps.append(float(listaNums[xd].lexeme))
                    print('Inverso: ' ,listaInversoSimps)
                    inverso = 1/(listaInversoSimps[0])
                    Op6.numeros=listaInversoSimps
                    Op6.total=inverso
                    Op6.contador=self.contadori
                    Op6.texto='Inverso'
                    self.operaciones.append(Op6)
                    print("Resultado: " + str(inverso))
                    print('Número de Inverso: ',self.contadori)
                elif t1.lexeme == 'SENO':
                    if t1.lexeme== 'SENO':
                        self.contadorsen+=1
                    listaSenoSimps=[]
                    Op7=Operacion('Sen')
                    tot2 = 0
                    for lol in range (len(listaNums)):
                        listaSenoSimps.append(float(listaNums[lol].lexeme))
                    print('Seno: ' ,listaSenoSimps)
                    senn = sin(listaSenoSimps[0])
                    Op7.numeros=listaSenoSimps
                    Op7.total=senn
                    Op7.contador=self.contadorsen
                    Op7.texto='Seno'
                    self.operaciones.append(Op7)
                    print("Resultado: " + str(senn))
                    print('Número de Seno: ',self.contadorsen)
                elif t1.lexeme == 'COSENO':
                    if t1.lexeme== 'COSENO':
                        self.contadorcos+=1
                    listaCosenoSimps=[]
                    Op8=Operacion('Cos')
                    tot2 = 0
                    for n in range (len(listaNums)):
                        listaCosenoSimps.append(float(listaNums[n].lexeme))
                    print('Coseno: ' ,listaCosenoSimps)
                    coss = cos(listaCosenoSimps[0])
                    Op8.numeros=listaCosenoSimps
                    Op8.total=coss
                    Op8.contador= self.contadorcos
                    Op8.texto='Coseno'
                    self.operaciones.append(Op8)
                    print("Resultado: " + str(coss))
                    print('Número de Coseno: ',self.contadorcos)
                elif t1.lexeme == 'TANGENTE':
                    if t1.lexeme== 'TANGENTE':
                        self.contadortan+=1
                    listaTangenteSimps=[]
                    Op9=Operacion('Tan')
                    tot2 = 0
                    for unu in range (len(listaNums)):
                        listaTangenteSimps.append(float(listaNums[unu].lexeme))
                    print('Tangente: ' ,listaTangenteSimps)
                    tann = tan(listaTangenteSimps[0])
                    Op9.numeros=listaTangenteSimps
                    Op9.total=tann
                    Op9.contador=self.contadortan
                    Op9.texto='Tangente'
                    self.operaciones.append(Op9)
                    print("Resultado: " + str(tann))
                    print('Número de Tangente: ',self.contadortan)
                elif t1.lexeme == 'MOD':
                    if t1.lexeme== 'MOD':
                        self.contadormod+=1
                    listaModSimps=[]
                    Op10=Operacion('%')
                    tot2 = 0
                    for owo in range (len(listaNums)):
                        listaModSimps.append(float(listaNums[owo].lexeme))
                    print('Mod: ' ,listaModSimps)
                    modd = listaModSimps[0] % listaModSimps[1]
                    Op10.numeros=listaModSimps
                    Op10.total=modd
                    Op10.contador=self.contadormod
                    Op10.texto='Mod'
                    self.operaciones.append(Op10)
                    print("Resultado: " + str(modd))
                    print('Número de Mod: ',self.contadormod)
                elif t1.lexeme == 'Operacion':
                    pass
        for i in self.operaciones:
            print("Tipo: ", i.texto,'Números: ' , i.numeros, 'Total: ', i.total, 'No. Operaciones: ' ,i.contador)
                    




            # elif token.tipo == 'TK_RESTA':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_MULTIPLICACION':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo =='TK_DIVISION':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_POTENCIA':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_RAIZ':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_INVERSO':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_SENO':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_COSENO':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_TANGENTE':
            #     print(token.tipo + " | Lexema " + token.lexeme)
            # elif token.tipo == 'TK_MOD':
            #     print(token.tipo + " | Lexema " + token.lexeme)



