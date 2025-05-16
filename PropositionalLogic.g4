grammar PropositionalLogic;

program: expression EOF;

expression: 
    NOT expression                    # NotExpr
    | expression AND expression      # AndExpr
    | expression OR expression       # OrExpr
    | expression IMPLIES expression  # ImpliesExpr
    | expression IFF expression      # IffExpr
    | expression NAND expression      # NandExpr
    | expression NOR expression       # NorExpr
    | expression XOR expression       # XorExpr
    | expression LEFTIMPLIES expression # LeftImpliesExpr
    | expression NIMPLIES expression    # NImpliesExpr
    | expression LNIMPLIES expression   # LNImpliesExpr
    | LPAREN expression RPAREN       # ParenExpr
    | IDENTIFIER                     # IdentifierExpr
    | TRUE                           # TrueExpr
    | FALSE                          # FalseExpr
    ;

NOT: '¬' | 'not';
AND: '∧' | 'and';
OR: '∨' | 'or';
IMPLIES: '->' | 'implies';
IFF: '<->' | 'iff';
TRUE: 'true' | 'True' | 'TRUE';
FALSE: 'false' | 'False' | 'FALSE';
LPAREN: '(';
RPAREN: ')';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
NAND: '↑' | 'nand';
NOR: '↓' | 'nor';
XOR: '⊕' | 'xor';
LEFTIMPLIES: '<-' | 'leftimplies';
NIMPLIES: '↛' | '->~';
LNIMPLIES: '↚' | '<-~'; 