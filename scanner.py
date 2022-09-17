from Clases import Error
from Clases import Token
# alfabeto = {letras}, {numeros}, <, >, /, ., =, [, ]

class Scanner:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
    def analyze(self,contenido):
        self.listaTokens = []
        self.listaErrores = []
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
                    if buffer == 'Tipo':
                        self.listaTokens.append(Token(buffer, 'TK_TIPO', line, column))
                    elif buffer == 'Operacion':
                        self.listaTokens.append(Token(buffer, 'TK_OPERACION', line, column))
                    elif buffer == 'Numero':
                        self.listaTokens.append(Token(buffer, 'TK_NUMERO', line, column))
                    elif buffer == 'Texto':
                        self.listaTokens.append(Token(buffer, 'TK_TEXTO_R', line, column))
                    elif buffer == 'Funcion':
                        self.listaTokens.append(Token(buffer, 'TK_FUNCION', line, column))
                    elif buffer == 'Titulo':
                        self.listaTokens.append(Token(buffer, 'TK_TITULO', line, column))
                    elif buffer == 'Descripcion':
                        self.listaTokens.append(Token(buffer, 'TK_DESCRIPCION', line, column))
                    elif buffer == 'Contenido':
                        self.listaTokens.append(Token(buffer, 'TK_CONTENIDO', line, column))
                    elif buffer == 'Estilo':
                        self.listaTokens.append(Token(buffer, 'TK_ESTILO', line, column))
                    elif buffer == 'Color':
                        self.listaTokens.append(Token(buffer, 'TK_COLOR', line, column))
                    elif buffer == 'Tamanio':
                        self.listaTokens.append(Token(buffer, 'TK_TAMANIO', line, column))
                    elif buffer == 'SUMA':
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
                if caracter.isalpha():
                    buffer+=caracter
                    column +=1
                    state = 'q_4'
                else:
                    self.listaTokens.append(Token(buffer, 'TK_TEXTO', line, column))
                    buffer = ''
                    indexx -= 1                    
                    state = 'q_0'

            indexx +=1


    def printScannergg(self):
        print("__________ T O K E N S __________")
        for token in self.listaTokens:
            token.getInfoTokens()
        print()
        print("__________ E R R O R E S __________")
        for token in self.listaErrores:
            token.getInfoErrores()
        print()
        


