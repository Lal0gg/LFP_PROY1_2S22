class Token:
    def __init__(self,lexeme, type, line, column):
        self.lexeme = lexeme
        self.type = type
        self.line = line
        self.column = column 

    def getInfoTokens(self):
        print('_'*40)
        print('Lexema: ', self.lexeme , ' |Tipo: ', self.type, 'Linea: ' , self.line, 'Columna: ', self.column)

class Error:
    def __init__(self,caracter, description, type, line, column):
        self.caracter = caracter
        self.description = description
        self.type = type
        self.line = line
        self.column = column

    def getInfoErrores(self):
        print('_'*40)
        print(self.caracter,'Descripcion: ', self.description , '|Tipo: ', self.type, 'Linea: ' , self.line, 'Columna: ', self.column)



