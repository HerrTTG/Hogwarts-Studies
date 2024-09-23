def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment."
    match exp:
        # end::EVAL_MATCH_TOP[]
        case int(x) | float(x):
            return x
        case Symbol() as name:
            return env[name]
        # tag::EVAL_MATCH_MIDDLE[]
        case ['quote', x]:  # <1>
            return x
        case ['if', test, consequence, alternative]:  # <2>
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:  # <3>
            return Procedure(parms, body, env)
        case ['define', Symbol() as name, value_exp]:  # <4>
            env[name] = evaluate(value_exp, env)
        # end::EVAL_MATCH_MIDDLE[]
        case ['define', [Symbol() as name, *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case ['set!', Symbol() as name, value_exp]:
            env.change(name, evaluate(value_exp, env))
        case [func_exp, *args] if func_exp not in KEYWORDS:
            proc = evaluate(func_exp, env)
            values = [evaluate(arg, env) for arg in args]
            return proc(*values)
        # tag::EVAL_MATCH_BOTTOM[]
        case _:  # <5>
            raise SyntaxError(lispstr(exp))
# end::EVAL_MATCH_BOTTOM[]
