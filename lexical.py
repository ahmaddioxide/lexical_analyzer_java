import ply.lex as lex

# List of token names for the lexer
# Tokens are the smallest unit of a program that is meaningful to the compiler or interpreter.

tokens = ['IDENTIFIER',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'ASSIGN',
          'LPAREN',
          'RPAREN',
          'LBRACE',
          'RBRACE',
          'SEMICOLON',
          'COMMA',
          'DOT',
          'EQUAL',
          'NOTEQUAL',
          'LESSTHAN',
          'LESSEQUAL',
          'GREATERTHAN',
          'GREATEREQUAL',
          'COMMENT'
          'NEWLINE',
          'WHITESPACE'
          'HASH',
          'DOUBLESLASH',
          'SINGLESLASH',
          'ASTERISK',
          'ATTHERATE',
          'COLON',
          'DOUBLEQUOTE',
          'SINGLEQUOTE',
          'BACKSLASH',
          'LBRACKET',
          'RBRACKET',
          'EXCLAMATION',
          'AND',

        'KEYWORD',
          ]


#Now we have to define the regular expressions for the tokens using the t_ prefix
#here prefix t_ is used to indicate that the function is a token definition
#for example, the regular expression for the token PLUS is r'\+'. 


# Regular expression for keywords
def t_KEYWORD(t):
    r'public|class|static|void|main|String|int|System|out|println|return|if|else|while|for|do|break|continue|switch|case|default|try|catch|finally|throw|throws|import|package|interface|implements|extends|abstract|final|native|synchronized|strictfp|transient|volatile|super|this|new|instanceof|enum|assert|boolean|char|byte|short|long|float|double|true|false|null'
    return t

#For Identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


# for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Regular expression for operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_LESSEQUAL = r'<='
t_GREATERTHAN = r'>'
t_GREATEREQUAL = r'>='

# For braces, semicolon, comma, dot
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','


#for Hasg '#' ADDITIONAL
def t_HASH(t):
    r'\#'  # Regular expression f
    return t

# for '&' ADDITIONAL
def t_AND(t): 
    r'&'  # Regular expression for and
    return t
# for '@' ADDITIONAL
t_ATTHERATE = r'@'

# for dot ADDITIONAL
t_DOT = r'\.'



#for slashes
t_DOUBLESLASH = r'//'
t_SINGLESLASH = r'/'
t_BACKSLASH = r'\\'


# Regular expression for special characters
t_ASTERISK = r'\*'
t_COLON = r':'

# Regular expression for quotes
t_DOUBLEQUOTE = r'\"'
t_SINGLEQUOTE = r'\''


# Regular expression for brackets
def t_LBRACKET(t):
    r'\['  # Regular expression for left bracket
    return t
def t_RBRACKET(t):
    r'\]'  # Regular expression for right bracket
    return t

# for exclamation
def t_EXCLAMATION(t):
    r'!'  # Regular expression for exclamation
    return t


# for comments
def t_COMMENT(t):
    r'//.*'
    pass


#  for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# for whitespace
t_ignore = ' \t'


# for invalid characters
def t_error(t):
    print(f"Yeh kya dal dia he bhai jaan aap ne ? Illegal character he '{t.value[0]}' at position {t.lexer.lineno}")
    t.lexer.skip(1)


# The lexer
lexer = lex.lex()

# Test code of java of which we have to do lexical analysis
java_code = """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello,& World!");
    }
}
"""

# Lexical analysis
lexer.input(java_code)

while True: 
    # Tokenize the input code
    tok = lexer.token()
    if not tok: # If there are no more tokens
        break
    print(tok) # Print the token 
