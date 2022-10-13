from ParserParser import ParserParser
from ParserVisitor import ParserVisitor
from Quadruple import Quadruple

from helpers import *

class IntermediateCode(ParserVisitor):   
    def __init__(self, table):
        self.table = table
        self.code = []
        self.quads = Quadruple()
        self.tempOp = []
        self.temps = []
    
    def getTable(self):
        print(str(self.table))
    
    def getAttribute(self, name):
        for i in self.table:
            if i['name'] == name:
                return i
        return None
    
    
    #Visits
    def visitClassDec(self, ctx):
        if ctx.name.text == 'Main':
            self.hasMain = True
            if ctx.inherits != None:
                self.errors.append("ERROR: La clase Main no puede heredar\n")
                print("ERROR: La clase Main no puede heredar\n")
                return self.visitChildren(ctx)
        if ctx.inherits != None:
            ''' Herencia multiple
            if ',' in ctx.inherits.text or '.' in ctx.inherits.text:
                self.errors.append("ERROR: No se permite la herencia multiple o recursiva\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                print("ERROR: No se permite la herencia multiple o recursiva\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                return self.visitChildren(ctx)
                '''
            if ctx.inherits.text not in self.types:
                self.errors.append("ERROR: No se encontro la herencia '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.inherits.text, ctx.start.line, ctx.start.column, 'class ' + ctx.name.text + ' inherits ' + ctx.inherits.text))
                print("ERROR: No se encontro la herencia '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.inherits.text, ctx.start.line, ctx.start.column, 'class ' + ctx.name.text + ' inherits ' + ctx.inherits.text))

        self.current_scope = ctx.name.text
        self.visitChildren(ctx)
        self.current_scope = 'Global'
        return 
            
    def visitAssignFeature(self, ctx:ParserParser.AssignFeatureContext):
        print("hola")
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        variable = self.getAttribute(name)
        if (ctx.right != None):
            if (len(ctx.right.getText()) > 0):

                operaciones = ['-', '+', '*', '/', '~']
                self.visitChildren(ctx)
                if len(self.tempOp) > 0:
                    for i in self.tempOp:

                        i[4] = i[4].replace('(', '').replace(')', '')
                        if not any(op in i[0] for op in operaciones):
                            i[0] = 't' + str(self.quads.temp)
                            self.temps.append(['t' + str(self.quads.temp), i[1]])
                            self.quads.newTemp()
                        else:
                            for j in self.temps:
                                if i[4] ==  j[1]:
                                    i[4] = j[0]
                                if i[0] == j[1]:
                                    i[3] = j[0]
                                    i[0] = 't' + str(self.quads.temp)
                                    
                            self.temps.append([i[0], i[1]])
                            self.quads.newTemp()
                        self.quads.generateQuadruple(i[2], i[3], i[4], i[0])    
                        
                    self.tempOp = []
                    print('')


                    
                    self.quads.generateQuadruple('', 't' + str(self.quads.temp-1), '', 'd[' + str(variable['address']) + ']')
                else:
                    self.quads.generateQuadruple('', ctx.right.getText(), '', 'd[' + str(variable['address']) + ']')
        else:
            self.quads.generateQuadruple('', '', '', 'd[' + str(variable['address']) + ']')
        print(self.quads.quadTable)
        
        return 
    
    def visitAssignExpr(self, ctx:ParserParser.AssignExprContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        variable = self.getAttribute(name)
        operaciones = ['-', '+', '*', '/', '~']
        self.visitChildren(ctx)
        if len(self.tempOp) > 0:
            for i in self.tempOp:

                i[4] = i[4].replace('(', '').replace(')', '')
                if not any(op in i[0] for op in operaciones):
                    i[0] = 't' + str(self.quads.temp)
                    self.temps.append(['t' + str(self.quads.temp), i[1]])
                    self.quads.newTemp()
                else:
                    for j in self.temps:
                        if i[4] ==  j[1]:
                            i[4] = j[0]
                        if i[0] == j[1]:
                            i[3] = j[0]
                            i[0] = 't' + str(self.quads.temp)
                            
                    self.temps.append([i[0], i[1]])
                    self.quads.newTemp()
                self.quads.generateQuadruple(i[2], i[3], i[4], i[0])
                
                
            self.tempOp = []
            self.quads.generateQuadruple('', 't' + str(self.quads.temp-1), '', 'd[' + str(variable['address']) + ']')

        else:
            self.quads.generateQuadruple('', ctx.right.getText(), '', 'd[' + str(variable['address']) + ']')
        print('')
        print(self.quads.quadTable)
        return

    
    def visitMethodFeature(self, ctx):
        if ctx.name.text == 'main':
            self.hasMainMethod = True
            if ctx.parameter != None:
                self.errors.append("ERROR: El metodo main no puede recibir parametros\n")
                print("ERROR: El metodo main no puede recibir parametros\n")
        return self.visitChildren(ctx)

    def visitIdExpr(self, ctx:ParserParser.IdExprContext):
        addr = self.getAttribute(ctx.getText())
        if addr is None:
            return 'd[0]'
        return 'd[' + str(addr['address']) + ']'
    
    def visitAddExpr(self, ctx):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(), ctx.getText(), 'add', l, r])
    
    def visitMulExpr(self, ctx):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(),ctx.getText(), 'mult', l, r])

    def visitMinusExpr(self, ctx):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(),ctx.getText(), 'sub', l, r])

    def visitDivExpr(self, ctx):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(),ctx.getText(), 'div', l, r])


    def visitParenExpr(self, ctx:ParserParser.ParenExprContext):
        return self.visit(ctx.children[1])
    
    def visitNegExpr(self, ctx):
        r = self.visit(ctx.right)
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            r = id['type']
        if (r != 'Int'):
            print("ERROR: No corresponden los tipos de la negacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la negacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Int'

    def visitNotExpr(self, ctx):
        r = self.visit(ctx.right)
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            r = id['type']
        if (r != 'Bool'):
            print("ERROR: No corresponden los tipos del not\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText().replace('not', 'not ')))
            self.errors.append("ERROR: No corresponden los tipos del not\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText().replace('not', 'not ')))

            return 'Error'
        return 'Bool'
 
    def visitEqualsExpr(self, ctx:ParserParser.EqualsExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion =\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion =\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Bool'
    
    def visitLequalExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion <=\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion <=\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Bool'

    def visitLtExpr(self, ctx:ParserParser.LtExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion <\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion <\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Bool'

    def visitNewExpr(self, ctx):
        return ctx.right.text

    def visitMethodDotExpr(self, ctx):

        exprType = 'Error'
        
        expr = self.getAttribute(ctx.left.getText())
        if expr != None:
            exprType = expr['type']

        else:
            exprT = self.visit(ctx.left)
            if exprT == None:
                for i in ctx.left.children:
                    temp = self.visit(i)
                    if temp != None:
                        exprType = temp



        attr = self.getAttribute(exprType)
        if attr != None:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and ((x['scope'] == exprType) or x['scope'] == attr['type']), self.table))
        else:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and (x['scope'] == exprType), self.table))
        if len(methodType) > 0: 
            methodType = methodType[0]['type']
            if methodType == 'Object':
                methodType = exprType
        
            if methodType == 'SELF_TYPE':
                methodType = exprType
            return methodType
    
    def visitMethodParenExpr(self, ctx):
        attr = self.getAttribute(self.current_scope)
        if attr != None:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and ((x['scope'] == self.current_scope) or x['scope'] == attr['type']), self.table))
        else:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and (x['scope'] == self.current_scope), self.table))
        if len(methodType) > 0: 
            methodType = methodType[0]['type']
        else:
            methodType = 'Error'

        if (ctx.name.text , 'method', self.current_scope) not in map(lambda x: (x['name'], x['kind'], x['scope']), self.table):
            
            if attr != None:
                if (ctx.name.text, 'method', attr['type']) not in map(lambda x: (x['name'], x['kind'], x['scope']), self.table):
                    print("ERROR: No se encontro el metodo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.name.text, ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: No se encontro el metodo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.name.text, ctx.start.line, ctx.start.column, ctx.getText()))
                    self.visitChildren(ctx)
                    return methodType

        paramFound = list(filter(lambda x: x['scope'] == ctx.name.text, self.table))
        if len(paramFound) != 0 and ctx.first != None:
            indexStart = ctx.getText().index('(')
            if indexStart != -1:
                params = ctx.getText()[indexStart+1:-1].split(',')
                if len(params) != len(paramFound):
                    
                    print("ERROR: Cantidad de argumentos incorrecta\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: Cantidad de argumentos incorrecta\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.visitChildren(ctx)
                    return methodType
                paramNodes = []
                i = 0
                index = -2
                while i != len(paramFound):
                    paramNodes.append(ctx.children[index])
                    index -= 2
                    i += 1
                paramNodes.reverse()
                paramTypes = []
                for i in paramNodes:
                    val = i.getText()
                    vType = 'Error'
                    if val.isdigit():
                        vType = "Int"
                    elif val == 'true' or val == 'TRUE' or val == 'false' or val == 'FALSE':
                        vType = "Bool"
                    elif val.count('"') == 2:
                        vType = "String"
                    paramTypes.append(vType)

                expectedTypes = list(map(lambda x: x['type'], paramFound))
                if expectedTypes != paramTypes:
                    print("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        self.visitChildren(ctx)
        return methodType