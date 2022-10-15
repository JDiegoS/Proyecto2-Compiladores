from ParserParser import ParserParser
from ParserVisitor import ParserVisitor

from helpers import *

class MyVisitor(ParserVisitor):   
    def __init__(self, table):
        self.table = table
        self.errors = []
        self.hasMain = False
        self.hasMainMethod = False
        self.current_scope = 'Global'
        self.types = ['Bool', 'Int', 'String', 'IO']

        for i in table:
            if i['kind'] == 'class' and i['name'] not in self.types:
                self.types.append(i['name'])
    
    def getTable(self):
        print(str(self.table))
    
    def getAttribute(self, name, scope=None):
        for i in self.table:
            if i['name'] == name:
                if scope != None and i['scope'] != scope and i['scope'] != 'Global':
                    continue
                return i
        return None

    def checkDifferentType(self, l, r, rightText, leftText):
        if (l != r):
            if l != "ID" and r != "ID":
                return True
            else:
                if r == "ID":
                    id = self.getAttribute(rightText)
                    r = id['type']
                else:
                    leftSide = leftText.split('<-')
                    if (len(leftSide) == 1):
                        id = self.getAttribute(leftSide[0])
                    else:
                        id = self.getAttribute(leftSide[1])
                    l = id['type']

                if (l != r):
                    return True
                else:
                    return False
    
    def checkIntOperation(self, ctx, bypass=False):
        if bypass:
            id = self.getAttribute(ctx.left.getText())
            if id != None:
                l = id['type']
            elif ctx.left.getText().isdigit():
                l = 'Int'
            else: 
                l = 'Error'
        else:
            l = self.visit(ctx.left)

        r = self.visit(ctx.right)

        if ctx.right.getText() == 'true' or ctx.right.getText() == 'false':
            r = 'Bool'

        if (l != "Int" or r != "Int"):
            if l != "ID" and r != "ID":
                return True
            else:
                if r == "ID":
                    id = self.getAttribute(ctx.right.getText())
                    if id == None:
                        print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                        self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                        return
                    r = id['type']
                if l == "ID":
                    id = self.getAttribute(ctx.left.getText())
                    if id == None:
                        print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.left.start.line, ctx.left.start.column, ctx.getText()))
                        self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.left.start.line, ctx.left.start.column, ctx.getText()))
                        return
                    l = id['type']
                    

                if (l != 'Int' or r != 'Int'):
                    return True
                else:
                    return False


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
            

    def visitMethodFeature(self, ctx):
        if ctx.name.text == 'main':
            self.hasMainMethod = True
            if ctx.parameter != None:
                self.errors.append("ERROR: El metodo main no puede recibir parametros\n")
                print("ERROR: El metodo main no puede recibir parametros\n")
        return self.visitChildren(ctx)

    def visitIdExpr(self, ctx:ParserParser.IdExprContext):
        return 'ID'

    def visitIntExpr(self, ctx:ParserParser.IntExprContext):
        return 'Int'
    
    def visitStringExpr(self, ctx:ParserParser.StringExprContext):
        if (len(ctx.getText()) > 30):
            print("ERROR: Longitud de string excedida\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: Longitud de string excedida\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            

        return 'String'
    
    def visitTrueExpr(self, ctx:ParserParser.TrueExprContext):
        return 'Bool'
    
    def visitFalseExpr(self, ctx:ParserParser.TrueExprContext):
        return 'Bool'
    
    def visitAddExpr(self, ctx):
        if (self.checkIntOperation(ctx)):
            print("ERROR: No corresponden los tipos de la suma\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la suma\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        
    
        #print(l)
        #print(r)
        #print(ctx.right.getText())
        #print(ctx.left.start)
        #print(ctx.right.start.type)
            return 'Error'
        return 'Int'
    
    def visitMulExpr(self, ctx):
        if (self.checkIntOperation(ctx)):
            print("ERROR: No corresponden los tipos de la multiplicacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la multiplicacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Int'

    def visitNegExpr(self, ctx):
        r = self.visit(ctx.right)
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
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
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            r = id['type']
        if (r != 'Bool'):
            print("ERROR: No corresponden los tipos del not\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText().replace('not', 'not ')))
            self.errors.append("ERROR: No corresponden los tipos del not\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText().replace('not', 'not ')))

            return 'Error'
        return 'Bool'
    
    def visitMinusExpr(self, ctx):
        if (self.checkIntOperation(ctx)):
            print("ERROR: No corresponden los tipos de la resta\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la resta\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Int'
    
    def visitDivExpr(self, ctx):
        if (self.checkIntOperation(ctx)):
            print("ERROR: No corresponden los tipos de la division\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la division\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Int'
    
    def visitEqualsExpr(self, ctx:ParserParser.EqualsExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if l == 'ID':
            id = self.getAttribute(ctx.left.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            l = id['type']
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            r = id['type']

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion =\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion =\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Bool'
    
    def visitLequalExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if l == 'ID':
            id = self.getAttribute(ctx.left.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            l = id['type']
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            r = id['type']

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion <=\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion <=\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

            return 'Error'
        return 'Bool'

    def visitLtExpr(self, ctx:ParserParser.LtExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if l == 'ID':
            id = self.getAttribute(ctx.left.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            l = id['type']
        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            if id is None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.right.getText(), ctx.right.start.line, ctx.right.start.column, ctx.getText()))
                return
            r = id['type']
        

        if (self.checkDifferentType(l, r, ctx.right.getText(), ctx.left.getText())):
            print("ERROR: No corresponden los tipos de la comparacion <\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la comparacion <\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            
            return 'Error'
        return 'Bool'


    def visitAssignExpr(self, ctx:ParserParser.AssignExprContext, fromOp=False):
        operaciones = ['-', '+', '*', '/', '~']
        if fromOp:
            expression = ctx.getText().split('<-')
            left = expression[0]
            right = expression[1]

            id = self.getAttribute(left)
            if id == None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (left, ctx.start.line, ctx.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (left, ctx.start.line, ctx.start.column, ctx.getText()))
                return
            l = id['type']

            if any(op in right for op in operaciones):
                r = 'Int'
                if self.checkIntOperation(ctx, True):
                    print("ERROR: No corresponden los tipos de la operacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: No corresponden los tipos de la operacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            elif '<' in right or '<=' in right:
                r = 'Bool'
            elif self.getAttribute(right) != None:
                r = 'ID'
            elif right.count('"') == 2:
                r = 'String'
            else:
                r = 'Error'
        else:
            r = self.visit(ctx.right)
            if r == None and len(ctx.right.children) > 1:
                for i in ctx.right.children:
                    temp = self.visit(i)
                    if temp != None:
                        r = temp

            id = self.getAttribute(ctx.left.text)
            if id == None:
                print("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.text, ctx.start.line, ctx.start.column, ctx.getText()))
                self.errors.append("ERROR: No se declaro la variable '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.text, ctx.start.line, ctx.start.column, ctx.getText()))
                return
            l = id['type']

            if any(op in ctx.right.getText() for op in operaciones):
                r = 'Int'
            elif '<' in ctx.right.getText() or '<=' in ctx.right.getText():
                r = 'Bool'

        if r == 'ID':
            id = self.getAttribute(ctx.right.getText())
            r = id['type']

        if (l != r):
            print(l)
            print(r)
            print("ERROR: No corresponden los tipos de la asignacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No corresponden los tipos de la asignacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        if fromOp:
            leftT = ctx.left.getText().split('<-')[0]
        else:
            leftT = ctx.left.text
        index = [ x['name'] for x in self.table ].index(leftT)
        self.table[index]['value'] = ctx.right.getText()


    def visitAssignFeature(self, ctx:ParserParser.AssignFeatureContext):
        if (ctx.right != None):
            if (len(ctx.right.getText()) > 0):

                l = ctx.left.text
                r = self.visit(ctx.right)

                if (l != r):
                        print("ERROR: No corresponden los tipos de la asignacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                        self.errors.append("ERROR: No corresponden los tipos de la asignacion\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        return self.visitChildren(ctx)

    def visitNewExpr(self, ctx):
        return ctx.right.text
    
    def visitBraceExpr(self, ctx:ParserParser.BraceExprContext):
        return self.visitChildren(ctx)

    def visitMethodDotExpr(self, ctx):
        exprType = 'Error'
        expr = self.getAttribute(ctx.left.getText(), self.current_scope)
        if expr != None:
            exprType = expr['type']
        elif ctx.left.getText().find('new') != -1 and ctx.left.getText().find('"') == -1:
            exprType = ctx.left.getText().split('new')[1].split(')')[0]
        else:
            exprT = self.visit(ctx.left)
            if exprT == None:
                for i in ctx.left.children:
                    temp = self.visit(i)
                    if temp != None:
                        exprType = temp

        if exprType == 'Error':
            print("ERROR: No se declaro la variable o tipo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: No se declaro la variable o tipo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.start.line, ctx.start.column, ctx.getText()))
            self.visitChildren(ctx)
            return methodType
        exprType = exprType.replace('(', '').replace(')', '')
        attr = self.getAttribute(exprType, self.current_scope)
        if attr != None:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and ((x['scope'] == exprType) or x['scope'] == attr['type'] or x['scope'] == 'Global'), self.table))
        else:
            methodType = list(filter(lambda x: (x['name'] == ctx.name.text) and (x['scope'] == exprType or x['scope'] == 'Global'), self.table ))
        if len(methodType) > 0: 
            methodType = methodType[0]['type']
            if methodType == 'Object':
                methodType = exprType
        
            if methodType == 'SELF_TYPE':
                methodType = exprType
            
        else:
            print("ERROR: El atributo '%s' no contiene el metodo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.name.text, ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: El atributo '%s' no contiene el metodo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (ctx.left.getText(), ctx.name.text, ctx.start.line, ctx.start.column, ctx.getText()))
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
                    else:
                        variable = self.getAttribute(val)
                        if variable != None:
                            vType = variable['type']
                        else:
                            print("ERROR: No se declaro la variable o tipo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (val, ctx.start.line, ctx.start.column, ctx.getText()))
                            self.errors.append("ERROR: No se declaro la variable o tipo '%s'\n\tLinea [%s:%s] \n\t\t%s" % (val, ctx.start.line, ctx.start.column, ctx.getText()))
                    paramTypes.append(vType)
                    
                expectedTypes = list(map(lambda x: x['type'], paramFound))
                if expectedTypes != paramTypes:
                    print("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        self.visitChildren(ctx)
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
                    else:
                        variable = self.getAttribute(val)
                        if variable != None:
                            vType = variable['type']
                    paramTypes.append(vType)

                expectedTypes = list(map(lambda x: x['type'], paramFound))
                if expectedTypes != paramTypes:
                    print("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
                    self.errors.append("ERROR: Tipo(s) de argumentos no coinciden con la definicion del metodo\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        self.visitChildren(ctx)
        return methodType
    
    def visitParenExpr(self, ctx:ParserParser.ParenExprContext):
        return self.visit(ctx.children[1])
    
    def visitIfThenExpr(self, ctx:ParserParser.IfThenExprContext):
        first = self.visit(ctx.first)
        if first != 'Bool':
            print("ERROR: La expresion condicional debe ser de tipo Bool\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: La expresion condicional debe ser de tipo Bool\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        self.visit(ctx.second)
        self.visit(ctx.third)
        return

    def visitWhileExpr(self, ctx:ParserParser.WhileExprContext):
        left = self.visit(ctx.left)
        if left != 'Bool':
            print("ERROR: La expresion condicional debe ser de tipo Bool\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
            self.errors.append("ERROR: La expresion condicional debe ser de tipo Bool\n\tLinea [%s:%s] \n\t\t%s" % (ctx.start.line, ctx.start.column, ctx.getText()))
        self.visit(ctx.right)
        return



    