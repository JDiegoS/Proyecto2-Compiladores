# Generated from Parser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,
        1,5,1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,
        2,41,8,2,10,2,12,2,44,9,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,63,8,2,3,2,65,8,2,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,
        5,4,82,8,4,10,4,12,4,85,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,106,8,4,11,4,12,4,107,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,118,8,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,126,8,4,5,4,128,8,4,10,4,12,4,131,9,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,155,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,181,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,189,8,4,10,4,12,4,192,9,4,5,4,194,8,4,
        10,4,12,4,197,9,4,1,4,5,4,200,8,4,10,4,12,4,203,9,4,1,4,0,1,8,5,
        0,2,4,6,8,0,0,238,0,11,1,0,0,0,2,17,1,0,0,0,4,64,1,0,0,0,6,66,1,
        0,0,0,8,154,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,
        11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,
        0,17,18,5,6,0,0,18,21,5,7,0,0,19,20,5,5,0,0,20,22,5,7,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,29,5,30,0,0,24,25,3,4,2,0,
        25,26,5,9,0,0,26,28,1,0,0,0,27,24,1,0,0,0,28,31,1,0,0,0,29,27,1,
        0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,31,0,0,33,
        34,5,9,0,0,34,3,1,0,0,0,35,36,5,27,0,0,36,47,5,28,0,0,37,42,3,6,
        3,0,38,39,5,36,0,0,39,41,3,6,3,0,40,38,1,0,0,0,41,44,1,0,0,0,42,
        40,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,45,37,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,
        1,0,0,0,50,51,5,29,0,0,51,52,5,32,0,0,52,53,5,7,0,0,53,54,5,30,0,
        0,54,55,3,8,4,0,55,56,5,31,0,0,56,65,1,0,0,0,57,58,5,27,0,0,58,59,
        5,32,0,0,59,62,5,7,0,0,60,61,5,33,0,0,61,63,3,8,4,0,62,60,1,0,0,
        0,62,63,1,0,0,0,63,65,1,0,0,0,64,35,1,0,0,0,64,57,1,0,0,0,65,5,1,
        0,0,0,66,67,5,27,0,0,67,68,5,32,0,0,68,69,5,7,0,0,69,7,1,0,0,0,70,
        71,6,4,-1,0,71,72,5,27,0,0,72,83,5,28,0,0,73,78,3,8,4,0,74,75,5,
        36,0,0,75,77,3,8,4,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,
        79,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,73,1,0,0,0,82,85,1,0,0,
        0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,155,
        5,29,0,0,87,88,5,13,0,0,88,89,3,8,4,0,89,90,5,19,0,0,90,91,3,8,4,
        0,91,92,5,20,0,0,92,93,3,8,4,0,93,94,5,12,0,0,94,155,1,0,0,0,95,
        96,5,21,0,0,96,97,3,8,4,0,97,98,5,17,0,0,98,99,3,8,4,0,99,100,5,
        18,0,0,100,155,1,0,0,0,101,105,5,30,0,0,102,103,3,8,4,0,103,104,
        5,9,0,0,104,106,1,0,0,0,105,102,1,0,0,0,106,107,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,31,0,0,110,155,
        1,0,0,0,111,112,5,16,0,0,112,113,5,27,0,0,113,114,5,32,0,0,114,117,
        5,7,0,0,115,116,5,33,0,0,116,118,3,8,4,0,117,115,1,0,0,0,117,118,
        1,0,0,0,118,129,1,0,0,0,119,120,5,36,0,0,120,121,5,27,0,0,121,122,
        5,32,0,0,122,125,5,7,0,0,123,124,5,33,0,0,124,126,3,8,4,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,119,1,0,0,0,128,131,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,
        1,0,0,0,132,133,5,14,0,0,133,155,3,8,4,19,134,135,5,24,0,0,135,155,
        5,7,0,0,136,137,5,35,0,0,137,155,3,8,4,17,138,139,5,15,0,0,139,155,
        3,8,4,16,140,141,5,28,0,0,141,142,3,8,4,0,142,143,5,29,0,0,143,155,
        1,0,0,0,144,145,5,26,0,0,145,155,3,8,4,7,146,155,5,8,0,0,147,155,
        5,47,0,0,148,155,5,10,0,0,149,155,5,11,0,0,150,155,5,27,0,0,151,
        152,5,27,0,0,152,153,5,33,0,0,153,155,3,8,4,1,154,70,1,0,0,0,154,
        87,1,0,0,0,154,95,1,0,0,0,154,101,1,0,0,0,154,111,1,0,0,0,154,134,
        1,0,0,0,154,136,1,0,0,0,154,138,1,0,0,0,154,140,1,0,0,0,154,144,
        1,0,0,0,154,146,1,0,0,0,154,147,1,0,0,0,154,148,1,0,0,0,154,149,
        1,0,0,0,154,150,1,0,0,0,154,151,1,0,0,0,155,201,1,0,0,0,156,157,
        10,14,0,0,157,158,5,39,0,0,158,200,3,8,4,15,159,160,10,13,0,0,160,
        161,5,42,0,0,161,200,3,8,4,14,162,163,10,12,0,0,163,164,5,40,0,0,
        164,200,3,8,4,13,165,166,10,11,0,0,166,167,5,41,0,0,167,200,3,8,
        4,12,168,169,10,10,0,0,169,170,5,44,0,0,170,200,3,8,4,11,171,172,
        10,9,0,0,172,173,5,43,0,0,173,200,3,8,4,10,174,175,10,8,0,0,175,
        176,5,45,0,0,176,200,3,8,4,9,177,180,10,23,0,0,178,179,5,38,0,0,
        179,181,5,7,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,
        182,183,5,37,0,0,183,184,5,27,0,0,184,195,5,28,0,0,185,190,3,8,4,
        0,186,187,5,36,0,0,187,189,3,8,4,0,188,186,1,0,0,0,189,192,1,0,0,
        0,190,188,1,0,0,0,190,191,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,
        0,193,185,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,
        0,196,198,1,0,0,0,197,195,1,0,0,0,198,200,5,29,0,0,199,156,1,0,0,
        0,199,159,1,0,0,0,199,162,1,0,0,0,199,165,1,0,0,0,199,168,1,0,0,
        0,199,171,1,0,0,0,199,174,1,0,0,0,199,177,1,0,0,0,200,203,1,0,0,
        0,201,199,1,0,0,0,201,202,1,0,0,0,202,9,1,0,0,0,203,201,1,0,0,0,
        19,13,21,29,42,47,62,64,78,83,107,117,125,129,154,180,190,195,199,
        201
    ]

class ParserParser ( Parser ):

    grammarFileName = "Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "':'", "'<-'", "'=>'", "'~'", "','", 
                     "'.'", "'@'", "'*'", "'+'", "'-'", "'/'", "'<'", "'<='", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "WS", "SINGLECOMMENT", "MULTICOMMENT", 
                      "INHERITS", "CLASS", "TYPE", "INT", "SEMICOLON", "TRUE", 
                      "FALSE", "FI", "IF", "IN", "ISVOID", "LET", "LOOP", 
                      "POOL", "THEN", "ELSE", "WHILE", "CASE", "ESAC", "NEW", 
                      "OF", "NOT", "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COLON", "ASSIGN", "DARROW", "NEG", "COMMA", "PERIOD", 
                      "AT", "MUL", "ADD", "MINUS", "DIV", "LT", "LEQUALS", 
                      "EQUALS", "ERROR", "STRING" ]

    RULE_program = 0
    RULE_class = 1
    RULE_feature = 2
    RULE_param = 3
    RULE_expr = 4

    ruleNames =  [ "program", "class", "feature", "param", "expr" ]

    EOF = Token.EOF
    NEWLINE=1
    WS=2
    SINGLECOMMENT=3
    MULTICOMMENT=4
    INHERITS=5
    CLASS=6
    TYPE=7
    INT=8
    SEMICOLON=9
    TRUE=10
    FALSE=11
    FI=12
    IF=13
    IN=14
    ISVOID=15
    LET=16
    LOOP=17
    POOL=18
    THEN=19
    ELSE=20
    WHILE=21
    CASE=22
    ESAC=23
    NEW=24
    OF=25
    NOT=26
    ID=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    COLON=32
    ASSIGN=33
    DARROW=34
    NEG=35
    COMMA=36
    PERIOD=37
    AT=38
    MUL=39
    ADD=40
    MINUS=41
    DIV=42
    LT=43
    LEQUALS=44
    EQUALS=45
    ERROR=46
    STRING=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ParserParser.EOF, 0)

        def class_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ClassContext)
            else:
                return self.getTypedRuleContext(ParserParser.ClassContext,i)


        def getRuleIndex(self):
            return ParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.class_()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParserParser.CLASS):
                    break

            self.state = 15
            self.match(ParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserParser.RULE_class

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ClassDecContext(ClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ClassContext
            super().__init__(parser)
            self.name = None # Token
            self.inherits = None # Token
            self.copyFrom(ctx)

        def CLASS(self):
            return self.getToken(ParserParser.CLASS, 0)
        def LBRACE(self):
            return self.getToken(ParserParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ParserParser.RBRACE, 0)
        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.SEMICOLON)
            else:
                return self.getToken(ParserParser.SEMICOLON, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.TYPE)
            else:
                return self.getToken(ParserParser.TYPE, i)
        def INHERITS(self):
            return self.getToken(ParserParser.INHERITS, 0)
        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.FeatureContext)
            else:
                return self.getTypedRuleContext(ParserParser.FeatureContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDec" ):
                listener.enterClassDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDec" ):
                listener.exitClassDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDec" ):
                return visitor.visitClassDec(self)
            else:
                return visitor.visitChildren(self)



    def class_(self):

        localctx = ParserParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.ClassDecContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(ParserParser.CLASS)
            self.state = 18
            localctx.name = self.match(ParserParser.TYPE)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ParserParser.INHERITS:
                self.state = 19
                self.match(ParserParser.INHERITS)
                self.state = 20
                localctx.inherits = self.match(ParserParser.TYPE)


            self.state = 23
            self.match(ParserParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParserParser.ID:
                self.state = 24
                self.feature()
                self.state = 25
                self.match(ParserParser.SEMICOLON)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(ParserParser.RBRACE)
            self.state = 33
            self.match(ParserParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignFeatureContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.FeatureContext
            super().__init__(parser)
            self.left = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)
        def TYPE(self):
            return self.getToken(ParserParser.TYPE, 0)
        def ASSIGN(self):
            return self.getToken(ParserParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignFeature" ):
                listener.enterAssignFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignFeature" ):
                listener.exitAssignFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignFeature" ):
                return visitor.visitAssignFeature(self)
            else:
                return visitor.visitChildren(self)


    class MethodFeatureContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.FeatureContext
            super().__init__(parser)
            self.name = None # Token
            self.parameter = None # ParamContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ParserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ParserParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)
        def TYPE(self):
            return self.getToken(ParserParser.TYPE, 0)
        def LBRACE(self):
            return self.getToken(ParserParser.LBRACE, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)

        def RBRACE(self):
            return self.getToken(ParserParser.RBRACE, 0)
        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ParamContext)
            else:
                return self.getTypedRuleContext(ParserParser.ParamContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodFeature" ):
                listener.enterMethodFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodFeature" ):
                listener.exitMethodFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodFeature" ):
                return visitor.visitMethodFeature(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = ParserParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ParserParser.MethodFeatureContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                localctx.name = self.match(ParserParser.ID)
                self.state = 36
                self.match(ParserParser.LPAREN)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ParserParser.ID:
                    self.state = 37
                    localctx.parameter = self.param()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ParserParser.COMMA:
                        self.state = 38
                        self.match(ParserParser.COMMA)
                        self.state = 39
                        self.param()
                        self.state = 44
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(ParserParser.RPAREN)
                self.state = 51
                self.match(ParserParser.COLON)
                self.state = 52
                self.match(ParserParser.TYPE)
                self.state = 53
                self.match(ParserParser.LBRACE)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(ParserParser.RBRACE)
                pass

            elif la_ == 2:
                localctx = ParserParser.AssignFeatureContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(ParserParser.ID)
                self.state = 58
                self.match(ParserParser.COLON)
                self.state = 59
                localctx.left = self.match(ParserParser.TYPE)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ParserParser.ASSIGN:
                    self.state = 60
                    self.match(ParserParser.ASSIGN)
                    self.state = 61
                    localctx.right = self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ParserParser.ID, 0)

        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)

        def TYPE(self):
            return self.getToken(ParserParser.TYPE, 0)

        def getRuleIndex(self):
            return ParserParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ParserParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ParserParser.ID)
            self.state = 67
            self.match(ParserParser.COLON)
            self.state = 68
            self.match(ParserParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class WhileExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ParserParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(ParserParser.LOOP, 0)
        def POOL(self):
            return self.getToken(ParserParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileExpr" ):
                listener.enterWhileExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileExpr" ):
                listener.exitWhileExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileExpr" ):
                return visitor.visitWhileExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(ParserParser.MUL, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ParserParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrueExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(ParserParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class IfThenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ParserParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def THEN(self):
            return self.getToken(ParserParser.THEN, 0)
        def ELSE(self):
            return self.getToken(ParserParser.ELSE, 0)
        def FI(self):
            return self.getToken(ParserParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenExpr" ):
                listener.enterIfThenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenExpr" ):
                listener.exitIfThenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenExpr" ):
                return visitor.visitIfThenExpr(self)
            else:
                return visitor.visitChildren(self)


    class LetExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(ParserParser.LET, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.ID)
            else:
                return self.getToken(ParserParser.ID, i)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COLON)
            else:
                return self.getToken(ParserParser.COLON, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.TYPE)
            else:
                return self.getToken(ParserParser.TYPE, i)
        def IN(self):
            return self.getToken(ParserParser.IN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.ASSIGN)
            else:
                return self.getToken(ParserParser.ASSIGN, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpr" ):
                listener.enterLetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpr" ):
                listener.exitLetExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpr" ):
                return visitor.visitLetExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def NEG(self):
            return self.getToken(ParserParser.NEG, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class LtExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(ParserParser.LT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtExpr" ):
                listener.enterLtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtExpr" ):
                listener.exitLtExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLtExpr" ):
                return visitor.visitLtExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(ParserParser.ADD, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class BraceExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(ParserParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ParserParser.RBRACE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.SEMICOLON)
            else:
                return self.getToken(ParserParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraceExpr" ):
                listener.enterBraceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraceExpr" ):
                listener.exitBraceExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraceExpr" ):
                return visitor.visitBraceExpr(self)
            else:
                return visitor.visitChildren(self)


    class IsvoidExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(ParserParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsvoidExpr" ):
                listener.enterIsvoidExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsvoidExpr" ):
                listener.exitIsvoidExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsvoidExpr" ):
                return visitor.visitIsvoidExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(ParserParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(ParserParser.ASSIGN, 0)
        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class MethodDotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.name = None # Token
            self.first = None # ExprContext
            self.second = None # ExprContext
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(ParserParser.PERIOD, 0)
        def LPAREN(self):
            return self.getToken(ParserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ParserParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def AT(self):
            return self.getToken(ParserParser.AT, 0)
        def TYPE(self):
            return self.getToken(ParserParser.TYPE, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDotExpr" ):
                listener.enterMethodDotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDotExpr" ):
                listener.exitMethodDotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDotExpr" ):
                return visitor.visitMethodDotExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def DIV(self):
            return self.getToken(ParserParser.DIV, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def EQUALS(self):
            return self.getToken(ParserParser.EQUALS, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualsExpr" ):
                listener.enterEqualsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualsExpr" ):
                listener.exitEqualsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualsExpr" ):
                return visitor.visitEqualsExpr(self)
            else:
                return visitor.visitChildren(self)


    class NewExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.right = None # Token
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(ParserParser.NEW, 0)
        def TYPE(self):
            return self.getToken(ParserParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpr" ):
                listener.enterNewExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpr" ):
                listener.exitNewExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpr" ):
                return visitor.visitNewExpr(self)
            else:
                return visitor.visitChildren(self)


    class MethodParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.first = None # ExprContext
            self.second = None # ExprContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ParserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ParserParser.RPAREN, 0)
        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodParenExpr" ):
                listener.enterMethodParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodParenExpr" ):
                listener.exitMethodParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodParenExpr" ):
                return visitor.visitMethodParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class LequalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def LEQUALS(self):
            return self.getToken(ParserParser.LEQUALS, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLequalExpr" ):
                listener.enterLequalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLequalExpr" ):
                listener.exitLequalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLequalExpr" ):
                return visitor.visitLequalExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ParserParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ParserParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ParserParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ParserParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class MinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(ParserParser.MINUS, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpr" ):
                listener.enterMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpr" ):
                listener.exitMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusExpr" ):
                return visitor.visitMinusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ParserParser.MethodParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 71
                localctx.name = self.match(ParserParser.ID)
                self.state = 72
                self.match(ParserParser.LPAREN)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INT) | (1 << ParserParser.TRUE) | (1 << ParserParser.FALSE) | (1 << ParserParser.IF) | (1 << ParserParser.ISVOID) | (1 << ParserParser.LET) | (1 << ParserParser.WHILE) | (1 << ParserParser.NEW) | (1 << ParserParser.NOT) | (1 << ParserParser.ID) | (1 << ParserParser.LPAREN) | (1 << ParserParser.LBRACE) | (1 << ParserParser.NEG) | (1 << ParserParser.STRING))) != 0):
                    self.state = 73
                    localctx.first = self.expr(0)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ParserParser.COMMA:
                        self.state = 74
                        self.match(ParserParser.COMMA)
                        self.state = 75
                        localctx.second = self.expr(0)
                        self.state = 80
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(ParserParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = ParserParser.IfThenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(ParserParser.IF)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(ParserParser.THEN)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(ParserParser.ELSE)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(ParserParser.FI)
                pass

            elif la_ == 3:
                localctx = ParserParser.WhileExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(ParserParser.WHILE)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(ParserParser.LOOP)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(ParserParser.POOL)
                pass

            elif la_ == 4:
                localctx = ParserParser.BraceExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(ParserParser.LBRACE)
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 102
                    self.expr(0)
                    self.state = 103
                    self.match(ParserParser.SEMICOLON)
                    self.state = 107 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INT) | (1 << ParserParser.TRUE) | (1 << ParserParser.FALSE) | (1 << ParserParser.IF) | (1 << ParserParser.ISVOID) | (1 << ParserParser.LET) | (1 << ParserParser.WHILE) | (1 << ParserParser.NEW) | (1 << ParserParser.NOT) | (1 << ParserParser.ID) | (1 << ParserParser.LPAREN) | (1 << ParserParser.LBRACE) | (1 << ParserParser.NEG) | (1 << ParserParser.STRING))) != 0)):
                        break

                self.state = 109
                self.match(ParserParser.RBRACE)
                pass

            elif la_ == 5:
                localctx = ParserParser.LetExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(ParserParser.LET)
                self.state = 112
                self.match(ParserParser.ID)
                self.state = 113
                self.match(ParserParser.COLON)
                self.state = 114
                self.match(ParserParser.TYPE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ParserParser.ASSIGN:
                    self.state = 115
                    self.match(ParserParser.ASSIGN)
                    self.state = 116
                    self.expr(0)


                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ParserParser.COMMA:
                    self.state = 119
                    self.match(ParserParser.COMMA)
                    self.state = 120
                    self.match(ParserParser.ID)
                    self.state = 121
                    self.match(ParserParser.COLON)
                    self.state = 122
                    self.match(ParserParser.TYPE)
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ParserParser.ASSIGN:
                        self.state = 123
                        self.match(ParserParser.ASSIGN)
                        self.state = 124
                        self.expr(0)


                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 132
                self.match(ParserParser.IN)
                self.state = 133
                self.expr(19)
                pass

            elif la_ == 6:
                localctx = ParserParser.NewExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(ParserParser.NEW)
                self.state = 135
                localctx.right = self.match(ParserParser.TYPE)
                pass

            elif la_ == 7:
                localctx = ParserParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(ParserParser.NEG)
                self.state = 137
                localctx.right = self.expr(17)
                pass

            elif la_ == 8:
                localctx = ParserParser.IsvoidExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(ParserParser.ISVOID)
                self.state = 139
                self.expr(16)
                pass

            elif la_ == 9:
                localctx = ParserParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(ParserParser.LPAREN)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(ParserParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = ParserParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(ParserParser.NOT)
                self.state = 145
                localctx.right = self.expr(7)
                pass

            elif la_ == 11:
                localctx = ParserParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(ParserParser.INT)
                pass

            elif la_ == 12:
                localctx = ParserParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(ParserParser.STRING)
                pass

            elif la_ == 13:
                localctx = ParserParser.TrueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(ParserParser.TRUE)
                pass

            elif la_ == 14:
                localctx = ParserParser.FalseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(ParserParser.FALSE)
                pass

            elif la_ == 15:
                localctx = ParserParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(ParserParser.ID)
                pass

            elif la_ == 16:
                localctx = ParserParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                localctx.left = self.match(ParserParser.ID)
                self.state = 152
                self.match(ParserParser.ASSIGN)
                self.state = 153
                localctx.right = self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 199
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = ParserParser.MulExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 157
                        self.match(ParserParser.MUL)
                        self.state = 158
                        localctx.right = self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = ParserParser.DivExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 160
                        self.match(ParserParser.DIV)
                        self.state = 161
                        localctx.right = self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = ParserParser.AddExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 163
                        self.match(ParserParser.ADD)
                        self.state = 164
                        localctx.right = self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = ParserParser.MinusExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 166
                        self.match(ParserParser.MINUS)
                        self.state = 167
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = ParserParser.LequalExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 169
                        self.match(ParserParser.LEQUALS)
                        self.state = 170
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = ParserParser.LtExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 172
                        self.match(ParserParser.LT)
                        self.state = 173
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = ParserParser.EqualsExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 175
                        self.match(ParserParser.EQUALS)
                        self.state = 176
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = ParserParser.MethodDotExprContext(self, ParserParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 180
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ParserParser.AT:
                            self.state = 178
                            self.match(ParserParser.AT)
                            self.state = 179
                            self.match(ParserParser.TYPE)


                        self.state = 182
                        self.match(ParserParser.PERIOD)
                        self.state = 183
                        localctx.name = self.match(ParserParser.ID)
                        self.state = 184
                        self.match(ParserParser.LPAREN)
                        self.state = 195
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INT) | (1 << ParserParser.TRUE) | (1 << ParserParser.FALSE) | (1 << ParserParser.IF) | (1 << ParserParser.ISVOID) | (1 << ParserParser.LET) | (1 << ParserParser.WHILE) | (1 << ParserParser.NEW) | (1 << ParserParser.NOT) | (1 << ParserParser.ID) | (1 << ParserParser.LPAREN) | (1 << ParserParser.LBRACE) | (1 << ParserParser.NEG) | (1 << ParserParser.STRING))) != 0):
                            self.state = 185
                            localctx.first = self.expr(0)
                            self.state = 190
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==ParserParser.COMMA:
                                self.state = 186
                                self.match(ParserParser.COMMA)
                                self.state = 187
                                localctx.second = self.expr(0)
                                self.state = 192
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 197
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 198
                        self.match(ParserParser.RPAREN)
                        pass

             
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 23)
         




