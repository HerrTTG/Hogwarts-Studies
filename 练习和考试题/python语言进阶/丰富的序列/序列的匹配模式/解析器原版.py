# 可以看到解析器原版就是方法，用于解析exp。
# 每一个elif都在进行判断第一项，然后进行拆包。
# 之后在做对应的工作。

def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment."
    if isinstance(exp, Symbol):  # variable reference
        return env[exp]
    # end::EVAL_IF_TOP[]
    elif not isinstance(exp, list):  # constant literal
        return exp
    # tag::EVAL_IF_MIDDLE[]
    elif exp[0] == 'quote':  # (quote exp)
        (_, x) = exp
        return x
    elif exp[0] == 'if':  # (if test conseq alt)
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda':  # (lambda (parm…) body…)
        (_, parms, *body) = exp
        return Procedure(parms, body, env)
    elif exp[0] == 'define':  # (define (name,parm...) body1 body2)
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
    # end::EVAL_IF_MIDDLE[]
    elif exp[0] == 'set!':
        (_, name, value_exp) = exp
        env.change(name, evaluate(value_exp, env))
    else:  # (proc arg…)
        (func_exp, *args) = exp
        proc = evaluate(func_exp, env)
        args = [evaluate(arg, env) for arg in args]
        return proc(*args)
