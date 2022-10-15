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
    
    def getAttribute(self, name, line=None):
        for i in self.table:
            if i['name'] == name:
                if line != None and i['line'] != line:
                    continue
                return i
        return None

    #Write code
    def writeCode(self):
        for i in self.quads.quadTable:
            if i['op'] == 'not':
                self.code.append(i['result'] + ' = ' + i['op'] + ' ' + i['arg1'])
                continue
            elif i['op'] == 'goto':
                self.code.append(i['op'] + ' ' + i['result'])
                continue
            elif i['op'] == 'IFFALSE':
                self.code.append(i['op'] + ' ' + i['arg1'] + ' goto ' + i['result'])
                continue
            elif i['op'] != '' and i['op'][0] == 'L':
                self.code.append('')
                self.code.append(i['op'] + ':')
                continue

            self.code.append(i['result'] + ' = ' + i['arg1'] + ' ' + i['op'] + ' ' + i['arg2'])
        return self.code
    
    #Visits
    def visitClassDec(self, ctx):
        
        return self.visitChildren(ctx)
            
    def visitAssignFeature(self, ctx:ParserParser.AssignFeatureContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        variable = self.getAttribute(name, ctx.start.line)
        if (ctx.right != None):
            if (len(ctx.right.getText()) > 0):

                if ctx.right.getText().find('"') == -1 and ctx.right.getText().find('new') != -1:
                    newVariable = self.getAttribute(ctx.right.getText().split('new')[1])
                    if variable == None:
                        newVariable = {'address': -1, 'size': 0, 'type': 'error'}
                    self.quads.generateQuadruple(str(newVariable['size']), 'allocate', '<' + str(newVariable['name']) + '>', 'd[' + str(variable['address']) + ']')
                    return

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
        else:
            self.quads.generateQuadruple(str(variable['size']), 'allocate', '<' + str(variable['type']) + '>', 'd[' + str(variable['address']) + ']')
        
        return 
    
    def visitAssignExpr(self, ctx:ParserParser.AssignExprContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        variable = self.getAttribute(name, ctx.start.line)
        if variable == None:
            variable = {'address': -1}
        operaciones = ['-', '+', '*', '/', '~', '<', '<=', '=']
        self.visitChildren(ctx)
        if len(self.tempOp) > 0:
            for i in self.tempOp:

                i[4] = i[4].replace('(', '').replace(')', '')
                i[0] = i[0].replace('(', '').replace(')', '')
                i[3] = i[3].replace('(', '').replace(')', '')
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

        elif ctx.right.getText().find('"') == -1 and ctx.right.getText().find('new') != -1:
            newVariable = self.getAttribute(ctx.right.getText().split('new')[1])
            if variable == None:
                newVariable = {'address': -1, 'size': 0, 'type': 'error'}
            self.quads.generateQuadruple(str(newVariable['size']), 'allocate', '<' + str(newVariable['type']) + '>', 'd[' + str(newVariable['address']) + ']')
        else:
            self.quads.generateQuadruple('', ctx.right.getText(), '', 'd[' + str(variable['address']) + ']')
        return

    
    def visitMethodFeature(self, ctx):
        
        return self.visitChildren(ctx)

    def visitIdExpr(self, ctx:ParserParser.IdExprContext):
        addr = self.getAttribute(ctx.getText(), ctx.start.line)
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
 
    def visitEqualsExpr(self, ctx:ParserParser.EqualsExprContext):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(), ctx.getText(), 'beq', l, r])
    
    def visitLequalExpr(self, ctx):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(), ctx.getText(), 'ble', l, r])

    def visitLtExpr(self, ctx:ParserParser.LtExprContext):
        l = self.visit(ctx.left)
        if l is None:
            l = ctx.left.getText()
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.left.getText(), ctx.getText(), 'blt', l, r])

    def visitIfThenExpr(self, ctx:ParserParser.IfThenExprContext):
        self.visit(ctx.first)
                
        for i in self.tempOp:
            i[0] = i[0].replace('(', '').replace(')', '')
            i[3] = i[3].replace('(', '').replace(')', '')
            if not any(op in i[0] for op in ('<', '<=', '=')):
                    i[0] = 't' + str(self.quads.temp)
                    self.temps.append(['t' + str(self.quads.temp), i[1]])
                    self.quads.newTemp()
            else:
                for j in self.temps:
                    if i[0] == j[1]:
                        i[3] = j[0]
                        i[0] = 't' + str(self.quads.temp)
                        
                self.temps.append([i[0], i[1]])
                self.quads.newTemp()
            
            self.quads.generateQuadruple(i[2], i[3], i[4], i[0])

            
        self.quads.generateQuadruple('IFFALSE', 't' + str(self.quads.temp-1), '', 'L' + str(self.quads.loop))
        self.tempOp = []

        self.visit(ctx.second)
        self.quads.generateQuadruple('goto', '', '', 'L' + str(self.quads.loop + 1))
        self.quads.generateQuadruple('L' + str(self.quads.loop), '', '', '')
        self.quads.newLoop()
        self.tempOp = []

        self.visit(ctx.third)
        self.quads.generateQuadruple('L' + str(self.quads.loop), '', '', '')
        self.tempOp = []


        return
    
    def visitWhileExpr(self, ctx:ParserParser.WhileExprContext):
        self.quads.generateQuadruple('L' + str(self.quads.loop), '', '', '')
        self.quads.newLoop()

        self.visit(ctx.left)

        for i in self.tempOp:
            i[0] = i[0].replace('(', '').replace(')', '')
            i[3] = i[3].replace('(', '').replace(')', '')
            if not any(op in i[0] for op in ('<', '<=', '=')):
                    i[0] = 't' + str(self.quads.temp)
                    self.temps.append(['t' + str(self.quads.temp), i[1]])
                    self.quads.newTemp()
            else:
                for j in self.temps:
                    if i[0] == j[1]:
                        i[3] = j[0]
                        i[0] = 't' + str(self.quads.temp)
                        
                self.temps.append([i[0], i[1]])
                self.quads.newTemp()
            
            self.quads.generateQuadruple(i[2], i[3], i[4], i[0])

            
        self.quads.generateQuadruple('IFFALSE', 't' + str(self.quads.temp-1), '', 'L' + str(self.quads.loop))
        self.tempOp = []

        self.visit(ctx.right)
        self.quads.generateQuadruple('goto', '', '', 'L' + str(self.quads.loop - 1))
        self.quads.generateQuadruple('L' + str(self.quads.loop), '', '', '')
        self.quads.newLoop()

        return


    def visitNewExpr(self, ctx):
        return ctx.right.text

    def visitParenExpr(self, ctx:ParserParser.ParenExprContext):
        return self.visit(ctx.children[1])
    
    def visitNegExpr(self, ctx):
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.right.getText(), ctx.getText(), 'mult', '-1', r])

    def visitNotExpr(self, ctx):
        r = self.visit(ctx.right)
        if r is None:
            r = ctx.right.getText()
        return self.tempOp.append([ctx.right.getText(), ctx.getText(), 'not', r, ''])

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
        return self.visitChildren(ctx)