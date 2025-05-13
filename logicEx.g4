grammar logicEx;

// Parser rules
expression: term (OR term)*;
term: factor (AND factor)*;
factor: NOT? (LPAREN expression RPAREN | IDENTIFIER | BOOL);

// Lexer rules
AND: 'AND' | 'and' | '&&' | '&';
OR: 'OR' | 'or' | '||' | '|';
NOT: 'NOT' | 'not' | '!';
LPAREN: '(';
RPAREN: ')';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;
BOOL: 'TRUE' | 'FALSE' | 'true' | 'false';
WS: [ \t\r\n]+ -> skip; 