from Clases import Error
from Clases import Token
# alfabeto = {letras}, {numeros}, <, >, /, ., =, [, ], {colores}, {signos}


class Scanner:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.signos=['?','¿','¡','!','.',',',':',';']
        self.colores=['AZUL','ROJO','AMARILLO', 'VERDE','NEGRO', 'ROSADO', 'ANARANJADO', 'MORADO','TURQUESA','CYAN','NARANJA','ROSA','PURPURA','CAFÉ','CAFE','GRIS']
        self.contador= 0
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
                        elif caracter == '"':
                            buffer = caracter
                            column += 1
                            state = 'q_4'
                        elif caracter in self.colores:
                            buffer = caracter
                            column+=1
                            state='q_5'
                        elif caracter == '$':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(Token(buffer, '<<EOF>>' , line, column))
                            buffer = ''
                            state ='q_0'
                            print('Análisis Exitoso')
                        else:
                            self.listaErrores.append(Error(caracter + "No Es Reconocido Como Token de Este Lenguaje...", 'lexico', line, column)) 
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
                            elif buffer.upper() == 'OPERACION':
                                self.listaTokens.append(Token(buffer, 'TK_OPERACION', line, column))
                            elif buffer.upper() == 'OPERACIONES':
                                self.listaTokens.append(Token(buffer, 'TK_OPERACIONES', line, column))
                            elif buffer.upper() == 'NUMERO':
                                self.listaTokens.append(Token(buffer, 'TK_NUMERO', line, column))
                            elif buffer.upper() == 'TEXTO':
                                self.listaTokens.append(Token(buffer, 'TK_R_TEXTO_', line, column))
                            elif buffer.upper() == 'FUNCION':
                                self.listaTokens.append(Token(buffer, 'TK_FUNCION', line, column))
                            elif buffer.upper() == 'TITULO':
                                self.listaTokens.append(Token(buffer, 'TK_TITULO', line, column))
                            elif buffer.upper() == 'DESCRIPCION':
                                self.listaTokens.append(Token(buffer, 'TK_DESCRIPCION', line, column))
                            elif buffer.upper() == 'CONTENIDO':
                                self.listaTokens.append(Token(buffer, 'TK_CONTENIDO', line, column))
                            elif buffer.upper() == 'ESTILO':
                                self.listaTokens.append(Token(buffer, 'TK_ESTILO', line, column))
                            elif buffer.upper() == 'COLOR':
                                self.listaTokens.append(Token(buffer, 'TK_R_COLOR_', line, column))
                            elif buffer.upper() == 'TAMANIO':
                                self.listaTokens.append(Token(buffer, 'TK_TAMANIO', line, column))
                            elif buffer.upper() == 'SUMA':
                                self.listaTokens.append(Token(buffer, 'TK_SUMA', line, column))
                            elif buffer == 'RESTA':
                                self.listaTokens.append(Token(buffer, 'TK_RESTA', line, column))
                            elif buffer == 'MULTIPLICACION':
                                self.listaTokens.append(Token(buffer, 'TK_MULTIPLICACION', line, column))
                            elif buffer == 'DIVISION':
                                self.listaTokens.append(Token(buffer, 'TK_DIVISION', line, column))
                            elif buffer == 'POTENCIA':
                                self.listaTokens.append(Token(buffer, 'TK_POTENCIA', line, column))
                            elif buffer == 'RAIZ':
                                self.listaTokens.append(Token(buffer, 'TK_RAIZ', line, column))
                            elif buffer == 'INVERSO':
                                self.listaTokens.append(Token(buffer, 'TK_INVERSO', line, column))
                            elif buffer == 'SENO':
                                self.listaTokens.append(Token(buffer, 'TK_SENO', line, column))
                            elif buffer == 'COSENO':
                                self.listaTokens.append(Token(buffer, 'TK_COSENO', line, column))
                            elif buffer == 'TANGENTE':
                                self.listaTokens.append(Token(buffer, 'TK_TANGENTE', line, column))
                            elif buffer == 'MOD':
                                self.listaTokens.append(Token(buffer, 'TK_MOD', line, column))
                            elif buffer == 'ESCRIBIR':
                                self.listaTokens.append(Token(buffer, 'TK_ESCRIBIR', line, column))
                            elif buffer in self.colores:
                                self.listaTokens.append(Token(buffer, 'TK_COLOR', line, column))
                            else:
                                self.listaErrores.append(Error(buffer  + "  | No Es Reconocido Como Token de Este Lenguaje...", 'lexico', line, column))
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
                        if caracter == '"':
                            buffer += caracter
                            column += 1
                            self.listaTokens.append(Token(buffer, 'TK_CADENA', line, column))
                            buffer = ''
                            state = 'q_0'
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
        


