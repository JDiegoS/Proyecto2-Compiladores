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
        self.current_scope = 'Global'
        self.temps = []
    
    def getTable(self):
        print(str(self.table))
    
    def getAttribute(self, name, line=None):
        for i in self.table:
            if i['name'] == name:
                if line != None and i['line'] != line and i['scope'] != line:
                    
                    continue
                return i
        return None

    #Write code
    def writeCode(self):
        for i in self.quads.quadTable:
            if i['op'] == 'not':
                self.code.append(i['result'] + ' = ' + i['op'] + ' ' + i['arg1'] + ';')
                continue
            elif i['op'] == 'goto':
                self.code.append(i['op'] + ' ' + i['result'] + ';')
                continue
            elif i['op'] == 'IFFALSE':
                self.code.append(i['op'] + ' ' + i['arg1'] + ' goto ' + i['result'] + ';')
                continue
            elif i['op'] != '' and i['op'][0] == 'L':
                self.code.append('')
                self.code.append(i['op'] + ':')
                continue
            elif i['op'] == 'method':
                self.code.append(i['result'] + ':')
                continue
            elif i['op'] == 'BeginFunc' or i['op'] == 'EndFunc':
                self.code.append(i['op'] + ';')
                self.code.append('')

                continue
            elif i['op'] == 'param':
                self.code.append('param ' + i['result'] + ';')
                continue
            elif i['op'] == 'call':
                if i['result'] == '':
                    self.code.append(i['op'] + ' ' + i['arg1'] + ', ' + i['arg2'] +';')
                else:
                    self.code.append(i['result'] + ' = ' + i['op'] + ' ' + i['arg1'] + ', ' + i['arg2'] +';')
                continue

            self.code.append((i['result'] + ' = ' + i['arg1'] + ' ' + i['op'] + ' ' + i['arg2'] + ';').replace('  ', ''))
        return self.code
    
    #Visits
    def visitClassDec(self, ctx):
        self.current_scope = ctx.name.text
        self.visitChildren(ctx)
        self.current_scope = 'Global'
        return 
            
    def visitAssignFeature(self, ctx:ParserParser.AssignFeatureContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        variable = self.getAttribute(name, self.current_scope)
        if (ctx.right != None):
            if (len(ctx.right.getText()) > 0):

                if ctx.right.getText().find('"') == -1 and ctx.right.getText().find('new') != -1:
                    newVariable = self.getAttribute(ctx.right.getText().split('new')[1].split(')')[0])
                    if newVariable == None:
                        newVariable = {'address': -1, 'size': 0, 'type': 'error', 'name': 'error'}
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
        variable = self.getAttribute(name, self.current_scope)
        if variable == None:
            variable = {'address': -1}
        operaciones = ['-', '+', '*', '/', '~', '<', '<=', '=']
        self.visitChildren(ctx)
        if len(self.tempOp) > 0:
            if ctx.right.getText().find('"') == -1 and ctx.right.getText().find('new') != -1:
                    newVariable = self.getAttribute(ctx.right.getText().split('new')[1].split(')')[0])
                    if variable == None:
                        newVariable = {'address': -1, 'size': 0, 'type': 'error'}
                    self.quads.generateQuadruple(str(newVariable['size']), 'allocate', '<' + str(newVariable['name']) + '>', 'd[' + str(variable['address']) + ']')
                    return

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
            newVariable = self.getAttribute(ctx.right.getText().split('new')[1].split(')')[0])
            if newVariable == None:
                newVariable = {'address': -1, 'size': 0, 'type': 'error'}
            self.quads.generateQuadruple(str(newVariable['size']), 'allocate', '<' + str(newVariable['type']) + '>', 'd[' + str(newVariable['address']) + ']')
        elif ctx.right.getText().find('.') != -1 and ctx.right.getText().find('(') != -1:
            self.quads.quadTable[-1]['result'] = 'd[' + str(variable['address']) + ']'

        else:
            self.quads.generateQuadruple('', ctx.right.getText(), '', 'd[' + str(variable['address']) + ']')
        return

    
    def visitMethodFeature(self, ctx):
        self.quads.generateQuadruple('method', '', '', self.current_scope + '.' + ctx.name.text)
        self.quads.generateQuadruple('BeginFunc', '', '', '')

        paramFound = list(filter(lambda x: x['scope'] == ctx.name.text, self.table))
        for i in paramFound:
            self.quads.generateQuadruple(str(i['size']), 'allocate', '<' + str(i['type']) + '>', 'd[' + str(i['address']) + ']')

        self.visitChildren(ctx)

        operaciones = ['-', '+', '*', '/', '~', '<', '<=', '=']
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

        self.quads.generateQuadruple('EndFunc', '', '', '')
        
        return 

    def visitIdExpr(self, ctx:ParserParser.IdExprContext):
        addr = self.getAttribute(ctx.getText(), self.current_scope)
        if addr is None:
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

        paramFound = list(filter(lambda x: x['scope'] == ctx.name.text, self.table))
        if len(paramFound) != 0 and ctx.first != None:
            dotIndex = ctx.getText().index('.')
            indexStart = ctx.getText()[dotIndex:].index('(')
            if indexStart != -1:
                params = ctx.getText()[dotIndex + indexStart+1:-1].split(',')
                indx = 0
                
                while indx < len(params) and indx < len(paramFound):
                    variable = self.getAttribute(params[indx], ctx.name.text)
                    if variable != None:
                        self.quads.generateQuadruple('param', '', '', 'd[' + str(variable['address']) + ']')
                    else:
                        self.quads.generateQuadruple('param', '', '', params[indx])
                   
                    indx += 1


            self.quads.generateQuadruple('call', ctx.name.text, str(indx), '')
        else:
            self.quads.generateQuadruple('call', ctx.name.text, '0', '')
        return self.visitChildren(ctx)
    
    def visitMethodParenExpr(self, ctx):


        paramFound = list(filter(lambda x: x['scope'] == ctx.name.text, self.table))
        if len(paramFound) != 0 and ctx.first != None:
            indexStart = ctx.getText().index('(')
            if indexStart != -1:
                params = ctx.getText()[indexStart+1:-1].split(',')
                indx = 0
                
                while indx < len(params) and indx < len(paramFound):
                    variable = self.getAttribute(params[indx], ctx.name.text)
                    if variable != None:
                        self.quads.generateQuadruple('param', '', '', 'd[' + str(variable['address']) + ']')
                    else:
                        self.quads.generateQuadruple('param', '', '', params[indx])
                   
                    indx += 1


            self.quads.generateQuadruple('call', ctx.name.text, str(indx), '')
        
        return self.visitChildren(ctx)