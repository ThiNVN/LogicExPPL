grammar PropositionalLogic;

expression: 
      expression binaryOp expression   # BinaryExpression
    | unaryOp expression               # UnaryExpression
    | atom                             # AtomExpression
    | '(' expression ')'               # ParenthesizedExpression
    ;

binaryOp
    : AND
    | OR
    | NAND
    | NOR
    ;

unaryOp
    : NOT
    ;

atom
    : TRUE
    | FALSE
    | ID
    ;

NOT: '~' | '!';
AND: '&';
OR: '|' | '+';
NAND: '^' | '!&';
NOR: '*' | '!+' ;

TRUE: '1';
FALSE: '0';

ID: [a-zA-Z][a-zA-Z0-9_]*;

LPAREN: '(';
RPAREN: ')';

WS: [ \t\r\n]+ -> skip;