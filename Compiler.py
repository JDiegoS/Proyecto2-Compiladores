import os
from antlr4 import *
from ParserLexer import ParserLexer
from ParserListener import ParserListener
from MyListener import MyListener
from MyVisitor import MyVisitor
from ParserParser import ParserParser
from ParserVisitor import ParserVisitor
from MyErrorListener import MyErrorListener
from IntermediateCode import IntermediateCode

from SymbolsTable import SymbolTable
from helpers import *

class Compiler(object):
    def __init__(self):
        
        self.errors = []

    def compile(self, file, text):
        data = FileStream(file)
        lexer = ParserLexer(data)
        stream = CommonTokenStream(lexer)
        parser = ParserParser(stream)
        parser.removeErrorListeners()
        myErrorListener = MyErrorListener()
        parser.addErrorListener(myErrorListener)
        tree = parser.program()

        syntaxErrors = myErrorListener.getErrors()
        self.errors += syntaxErrors
        
        #Arbol
        #os.system('grun Parser program test2.cl -gui -tokens')

        print("\n\n")

        # Tabla
        printer = MyListener()
        walker = ParseTreeWalker()

        # Predefinir clases IO, Int, Bool, String
        printer.symbol_table.insert('IO', 'Object', 'class', 'Global', 0)
        printer.symbol_table.insert('Bool', 'Object', 'class', 'Global', 0)
        printer.symbol_table.insert('Int', 'Object', 'class', 'Global', 0)
        printer.symbol_table.insert('String', 'Object', 'class', 'Global', 0)
        printer.symbol_table.insert('out_string', 'SELF_TYPE', 'method', 'IO', 0)
        printer.symbol_table.insert('string', 'String', 'parameter', 'out_string', 0)
        printer.symbol_table.insert('in_string', 'String', 'method', 'IO', 0)
        printer.symbol_table.insert('out_int', 'SELF_TYPE', 'method', 'IO', 0)
        printer.symbol_table.insert('number', 'Int', 'parameter', 'out_int', 0)
        printer.symbol_table.insert('in_int', 'Int', 'method', 'IO', 0)
        printer.symbol_table.insert('length', 'Int', 'method', 'String', 0)
        printer.symbol_table.insert('concat', 'String', 'method', 'String', 0)
        printer.symbol_table.insert('s', 'String', 'parameter', 'concat', 0)
        printer.symbol_table.insert('substr', 'String', 'method', 'String', 0)
        printer.symbol_table.insert('i', 'Int', 'parameter', 'substr', 0)
        printer.symbol_table.insert('l', 'Int', 'parameter', 'substr', 0)

        walker.walk(printer, tree)
        
        table = printer.getTable()
        self.errors += printer.symbol_table.errors

        # Errores semanticos
        visitor = MyVisitor(table)
        visitor.visit(tree)
        self.errors += visitor.errors

        if visitor.hasMain == False:
            self.errors.append("ERROR: No se encontro la clase Main\n")
            print("ERROR: No se encontro la clase Main\n")

        if visitor.hasMainMethod == False:
            self.errors.append("ERROR: No se encontro el metodo main\n")
            print("ERROR: No se encontro el metodo main\n")

        if len(self.errors) == 0:
            self.errors.append("Analizado sin errores!")
            print("Analizado sin errores!")

        finalTable = SymbolTable()
        finalTable.table = visitor.table
        print("\n TABLA DE SIMBOLOS\n")
        print(str(finalTable) + "\n")


        print("\n CODIGO INTERMEDIO\n")

        visitor = IntermediateCode(finalTable.table)
        visitor.visit(tree)
        code = visitor.writeCode()

        for i in code:
            print(i)

    

    

    
text=open('aritmetica').read()
main = Compiler()
main.compile('aritmetica', text)