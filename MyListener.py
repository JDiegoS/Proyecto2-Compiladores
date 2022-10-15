from ParserListener import ParserListener
from ParserParser import ParserParser


from SymbolsTable import SymbolTable
from helpers import *


class MyListener(ParserListener):   
    def __init__(self):
        self.symbol_table = SymbolTable()
        

    def getTable(self):
        return self.symbol_table.getTable()

    def assign_value(self, ctx: ParserParser.ExprContext):
        self.symbol_table.set(ctx.children[0].getText(), ctx.children[0].symbol.line, ctx.children[2].getText())

    def insert_self(self, line: int):
        name = 'self'
        kind = ATTR
        typ = SELF_TYPE
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_class(self, ctx: ParserParser.ClassContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[1]
        kind = 'class'
        ind = indx(children, 'inherits')
        typ = children[ind + 1] if ind != -1 and (children[ind + 1], 'class') in map(lambda x: (x['name'], x['kind']), self.symbol_table.table) else 'Object'
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_feature(self, ctx: ParserParser.FeatureContext):

        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = METHOD if children[1] != ':' else ATTR
        ind = indx(children, ':')
        typ = children[ind + 1]
        line = ctx.children[0].symbol.line
        value = None
        scope = self.symbol_table.get_scope()

        if kind == 'method':
            
            self.symbol_table.push_scope(children[0])
        else:
            index = indx(children, '<-')
            if index != -1:
                value = children[index + 1]
                '''
                if value.find('"') == -1 and value.find('new') != -1:
                    typ = value.split('new')[1]
                '''

        self.symbol_table.insert(name, typ, kind, scope, line, value)
    
    def insert_param(self, ctx: ParserParser.ParamContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = PARAMETER
        typ = children[2]
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    # Enter a parse tree produced by ParserParser#class.
    def enterClassDec(self, ctx):
        self.insert_class(ctx)
        self.symbol_table.push_scope(ctx.children[1].getText())
        self.insert_self(ctx.children[0].symbol.line)

    # Exit a parse tree produced by ParserParser#class.
    def exitClassDec(self, ctx):
        self.symbol_table.pop_scope()

    # Enter a parse tree produced by ParserParser#feature.
    def enterMethodFeature(self, ctx: ParserParser.MethodFeatureContext):
        self.insert_feature(ctx)
    
    def enterAssignFeature(self, ctx: ParserParser.AssignFeatureContext):
        self.insert_feature(ctx)

    
    # Exit a parse tree produced by ParserParser#feature.
    def exitMethodFeature(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    def exitAssignFeature(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    # Enter a parse tree produced by ParserParser#Param.
    def enterParam(self, ctx: ParserParser.ParamContext):
        if len(ctx.children) > 2:
            self.insert_param(ctx)

    # Enter a parse tree produced by ParserParser#expr.
    def enterExpr(self, ctx: ParserParser.ExprContext):
        children = list(map(lambda x: x.getText(), ctx.children))
        if '<-' in children:
            self.assign_value(ctx)
