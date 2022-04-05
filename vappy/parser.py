from sly import Parser
from sly.yacc import _decorator as rule

from vappy.ast import StatementList, Function, Variable, Assignment, Statement, Value, Print, FunctionCall, If, IfElse, \
    Return, FunctionCallAssign, BinOp, For, While
from vappy.lexer import VappyLexer


class VappyParser(Parser):
    debugfile = 'parser.out'
    tokens = VappyLexer.tokens

    precedence = (
        ('nonassoc', LT, GT, EQ),  # Nonassociative operators
        ('left', TIMES, DIVIDE),
        ('left', PLUS, MINUS),
    )

    def __init__(self):
        self.names = {}

    @rule('START statements END')
    def program(self, p):
        return p.statements

    ###
    # STATEMENTS
    ###

    @rule('statement statements')
    def statements(self, p):
        return StatementList([p.statement] + p.statements.statements)

    @rule('statement')
    def statements(self, p):
        return StatementList([p.statement])

    ###
    # STATEMENT
    ###

    @rule('FN_DEF_1 NAME COMMA FN_DEF_2 NAME FN_DEF_3 statements END')
    def statement(self, p):
        self.names[p.NAME1] = Function([p.NAME0], p.statements)
        return Statement()

    @rule('FN_DEF_1_PLURAL vars COMMA FN_DEF_2 NAME FN_DEF_3 statements END')
    def statement(self, p):
        self.names[p.NAME] = Function(p.vars, p.statements)
        return Statement()

    @rule("IF_1 expr COMMA statements ELSE statements END")
    def statement(self, p):
        return IfElse(p.expr, p.statements0, p.statements1)

    @rule("IF_1 expr COMMA statements END")
    def statement(self, p):
        return If(p.expr, p.statements)

    @rule("NAME FOR_1 expr FOR_2 expr FOR_3 statements END")
    def statement(self, p):
        return For(p.NAME, p.expr0, p.expr1, p.statements)

    @rule("WHILE_1 expr WHILE_2 statements END")
    def statement(self, p):
        return While(p.expr, p.statements)

    @rule("RETURN expr PERIOD")
    def statement(self, p):
        return Return(p.expr)

    @rule('NAME ASSIGNMENT expr PERIOD')
    def statement(self, p):
        return Assignment(p.NAME, p.expr)

    @rule("FN_CALL_1 exprs COMMA NAME FN_CALL_2_ASSIGN NAME PERIOD")
    def statement(self, p):
        function_name = p.NAME0
        return FunctionCallAssign(function_name, p.exprs, p.NAME1)

    @rule('PRINT expr PERIOD')
    def statement(self, p):
        return Print(p.expr)

    @rule('COMMENT')
    def statement(self, _):
        return Statement()

    ###
    # VARS
    ###

    @rule('NAME COMMA vars_sub')
    def vars(self, p):
        return [p.NAME] + p.vars_sub

    @rule('NAME AND NAME')
    def vars(self, p):
        return [p.NAME0, p.NAME1]

    @rule('NAME')
    def vars(self, p):
        return [p.NAME]

    @rule('NAME COMMA vars_sub')
    def vars_sub(self, p):
        return [p.NAME] + p.vars_sub

    @rule('NAME AND NAME')
    def vars_sub(self, p):
        return [p.NAME0, p.NAME1]

    ###
    # EXPRS
    ###

    @rule('exprs_sub AND expr')
    def exprs(self, p):
        return p.exprs_sub + [p.expr]

    @rule('expr')
    def exprs(self, p):
        return [p.expr]

    @rule('exprs_sub COMMA expr')
    def exprs_sub(self, p):
        return p.exprs_sub + [p.expr]

    @rule('expr')
    def exprs_sub(self, p):
        return [p.expr]

    ###
    # EXPR
    ###

    @rule("FN_CALL_1 exprs COMMA NAME FN_CALL_2 PERIOD")
    def expr(self, p):
        function_name = p.NAME
        return FunctionCall(function_name, p.exprs)

    @rule("expr PLUS expr")
    def expr(self, p):
        """+"""
        return BinOp("+", p.expr0, p.expr1)

    @rule("expr MINUS expr")
    def expr(self, p):
        """-"""
        return BinOp("-", p.expr0, p.expr1)

    @rule("expr TIMES expr")
    def expr(self, p):
        """*"""
        return BinOp("*", p.expr0, p.expr1)

    @rule("expr DIVIDE expr")
    def expr(self, p):
        """/"""
        return BinOp("/", p.expr0, p.expr1)

    @rule("expr EQ expr")
    def expr(self, p):
        """=="""
        return BinOp("==", p.expr0, p.expr1)

    @rule("expr LT expr")
    def expr(self, p):
        """<"""
        return BinOp("<", p.expr0, p.expr1)

    @rule("expr GT expr")
    def expr(self, p):
        """>"""
        return BinOp(">", p.expr0, p.expr1)

    @rule("QUOTE NAME QUOTE")
    def expr(self, p):
        """string"""
        return Value(p.NAME)

    @rule('NUMBER')
    def expr(self, p):
        """int"""
        return Value(int(p.NUMBER))

    @rule('STRING')
    def expr(self, p):
        """string"""
        return Value(p.STRING[1:-1])

    @rule('NAME')
    def expr(self, p):
        """variable"""
        return Variable(p.NAME)
