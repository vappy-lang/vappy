from sly import Lexer


class VappyLexer(Lexer):
    tokens = {
        START, FN_DEF_1, FN_DEF_1_PLURAL, FN_DEF_2, FN_DEF_3,
        FN_CALL_1, FN_CALL_2, FN_CALL_2_ASSIGN,
        IF_1, ELSE,
        FOR_1, FOR_2, FOR_3,
        WHILE_1, WHILE_2,
        PRINT, ASSIGNMENT,
        AND, END, NAME, COMMENT,
        RETURN, NUMBER, STRING,
        EQ, LT, GT,
        PLUS, TIMES, MINUS, DIVIDE,
        LPAREN, RPAREN,
        COMMA, QUOTE, PERIOD
    }

    START = r'Hey guys, did you know that...'
    FN_DEF_1 = r'With their ability'
    FN_DEF_1_PLURAL = r'With their abilities'
    FN_DEF_2 = r'they can easily'
    FN_DEF_3 = r'with enough water.'
    FN_CALL_1 = r'In terms of'
    FN_CALL_2 = r'is the most cool.'
    FN_CALL_2_ASSIGN = r'is the most compatible Pokemon for'
    IF_1 = r"Also, if you ensure that"
    ELSE = r"you can make your Vaporeon turn white."
    FOR_1 = r"are an average of"
    FOR_2 = r"feet tall and"
    FOR_3 = r"pounds."
    WHILE_1 = r"You can easily have sex with one as long as"
    WHILE_2 = r"without getting sore."
    RETURN = r"No other Pokemon comes close to this level of"
    PRINT = r"There's no doubt in my mind that an aroused Vaporeon would say"
    ASSIGNMENT = r'can be rough with'
    EQ = "is rough with"
    LT = "is small enough for"
    GT = "is large enough for"
    AND = r'and'
    END = r'Vaporeon is literally built for human dick.'

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    COMMENT = r'#[^#]*#'
    STRING = r'"[^"]*"'

    # Special symbols
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    QUOTE = r'\"'
    PERIOD = r'.'


    ignore = ' \t'

    # Ignored pattern
    ignore_newline = r'\n+'

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
