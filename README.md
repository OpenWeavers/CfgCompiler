# cfgcompiler
Python Utilities to Parse and Validate Description of Context Free Grammar

# Input Specifications
- Non Terminals must begin with Capital Letter, and can be followed by any number of letters and underscore. Example `MulExpr`.
- Terminals *must* be enclosed within pair of single quotes. Maximum character length is 1. Example `'a`.
- Production head contains a variable, body contains string of variables and terminals. Head and Body are separated by arrow mark `->`. Productions are terminated with full stop (`.`).
- Variable encountered at the head of first production is considered as Starting Symbol of Grammar.

# Sample Grammar

            Expr -> Expr '+' MulExpr | MulExpr.
            MulExpr -> MulExpr '*' GrpExpr | GrpExpr.
            GrpExpr -> '(' Expr ')' | 'a' | Hello.

# Sample Output
Output is a Object Containing CFG `G(V,T,P,S)`.

        {'Expr': True, 'MulExpr': True, 'GrpExpr': True, 'Hello': False}
        {"'+'", "'*'", "')'", "'a'", "'('"}
        defaultdict(<class 'list'>, {'Expr': [['Expr', "'+'", 'MulExpr'], ['MulExpr']], 'MulExpr': [['MulExpr', "'*'", 'GrpExpr'], ['GrpExpr']], 'GrpExpr': [["'('", 'Expr', "')'"], ["'a'"], ['Hello']]})
        Expr

