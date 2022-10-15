grammar Parser;
import Scanner;

program:	(class)+ EOF ;
class: CLASS name=TYPE (INHERITS inherits=TYPE)? LBRACE (feature SEMICOLON)* RBRACE SEMICOLON   #ClassDec;  
feature: name=ID LPAREN (parameter=param (COMMA param)*)* RPAREN COLON TYPE LBRACE right=expr RBRACE #MethodFeature
    |   ID COLON left=TYPE (ASSIGN right=expr)?    #AssignFeature
    ;

param: ID COLON TYPE;

expr: 
    name=ID LPAREN (first=expr (COMMA second=expr)*)* RPAREN        # MethodParenExpr
    | left=expr (AT TYPE)? PERIOD name=ID LPAREN (first=expr (COMMA second=expr)*)* RPAREN        # MethodDotExpr
    | IF first=expr THEN second=expr ELSE third=expr FI        # IfThenExpr
    | WHILE left=expr LOOP right=expr POOL        # WhileExpr
    | LBRACE (expr SEMICOLON)+ RBRACE        # BraceExpr
    | LET ID COLON TYPE (ASSIGN first=expr)? (COMMA ID COLON TYPE (ASSIGN second=expr)?)* IN third=expr        # LetExpr
    | NEW right=TYPE        # NewExpr
    | NEG right=expr        # NegExpr
    | ISVOID right=expr        # IsvoidExpr
    | LPAREN right=expr RPAREN        # ParenExpr
    | left=expr MUL right=expr        # MulExpr
    | left=expr DIV right=expr        # DivExpr
    | left=expr ADD right=expr        # AddExpr
    | left=expr MINUS right=expr        # MinusExpr
    | left=expr LEQUALS right=expr        # LequalExpr
    | left=expr LT right=expr        # LtExpr
    | left=expr EQUALS right=expr        # EqualsExpr
    | NOT right=expr        # NotExpr
    | INT        # IntExpr
    | STRING        # StringExpr
    | TRUE        # TrueExpr
    | FALSE        # FalseExpr
    | ID        # IdExpr
    | left=ID ASSIGN right=expr        # AssignExpr
    ;
