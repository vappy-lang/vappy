class Function(object):
    def __init__(self, var_list, statement_list):
        self.var_list = var_list
        self.statement_list = statement_list

    def exec(self, scope, args):
        """Args should be evaluated already"""
        temp_scope = scope.copy()
        assert len(self.var_list) == len(args)
        for name, arg in zip(self.var_list, args):
            temp_scope[name] = arg
        return self.statement_list.exec(temp_scope)


class StatementList(object):
    def __init__(self, statements):
        self.statements = statements

    def exec(self, scope):
        for statement in self.statements:
            result = statement.exec(scope)
            if result is not None:
                return result


class Statement(object):
    def exec(self, scope):
        return None


class Assignment(Statement):
    def __init__(self, left, right):
        # Left is a string, right is an expr
        self.left = left
        self.right = right

    def exec(self, scope):
        # Returns nothing
        scope[self.left] = self.right.exec(scope)


class If(Statement):
    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def exec(self, scope):
        if self.condition.exec(scope):
            return self.statements.exec(scope)


class IfElse(Statement):
    def __init__(self, condition, if_statements, else_statements):
        self.condition = condition
        self.if_statements = if_statements
        self.else_statements = else_statements

    def exec(self, scope):
        if self.condition.exec(scope):
            return self.if_statements.exec(scope)
        return self.else_statements.exec(scope)


class For(Statement):
    def __init__(self, var, lower, upper, statements):
        self.var = var
        self.lower = lower
        self.upper = upper
        self.statements = statements

    def exec(self, scope):
        lower_bound = self.lower.exec(scope)
        upper_bound = self.upper.exec(scope)
        if lower_bound >= upper_bound:
            return
        for i in range(lower_bound, upper_bound):
            scope[self.var] = i
            self.statements.exec(scope)


class While(Statement):
    def __init__(self, cond, statements):
        self.cond = cond
        self.statements = statements

    def exec(self, scope):
        while self.cond.exec(scope):
            self.statements.exec(scope)


class Return(Statement):
    def __init__(self, expr):
        self.expr = expr

    def exec(self, scope):
        return self.expr.exec(scope)


class Print(Statement):
    def __init__(self, expr):
        self.expr = expr

    def exec(self, scope):
        print(self.expr.exec(scope))


class Expr(object):
    """Expr always returns something"""
    def exec(self, scope):
        pass


class BinOp(Expr):
    def __init__(self, op, e1, e2):
        self.op = op
        self.e1 = e1
        self.e2 = e2

    def exec(self, scope):
        if self.op == "+":
            return self.e1.exec(scope) + self.e2.exec(scope)
        if self.op == "-":
            return self.e1.exec(scope) - self.e2.exec(scope)
        elif self.op == "==":
            return self.e1.exec(scope) == self.e2.exec(scope)
        elif self.op == "<":
            return self.e1.exec(scope) < self.e2.exec(scope)
        elif self.op == ">":
            return self.e1.exec(scope) > self.e2.exec(scope)
        else:
            pass


class FunctionCall(Expr):
    def __init__(self, function, args):
        self.function = function
        self.args = args

    def exec(self, scope):
        actual_args = [arg.exec(scope) for arg in self.args]
        try:
            actual_function = scope[self.function]
        except KeyError:
            raise LookupError(f"Function {self.function} not found")
        return actual_function.exec(scope, actual_args)


class FunctionCallAssign(FunctionCall):
    def __init__(self, function, args, dest):
        super().__init__(function, args)
        self.dest = dest

    def exec(self, scope):
        result = FunctionCall.exec(self, scope)
        scope[self.dest] = result


class Value(Expr):
    def __init__(self, value):
        self.value = value

    def exec(self, scope):
        return self.value


class Variable(Expr):
    def __init__(self, name):
        self.name = name

    def exec(self, scope):
        try:
            return scope[self.name]
        except LookupError:
            print("Undefined name '%s'" % self.name)
            return 0
