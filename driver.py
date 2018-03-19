from cfgcompiler.CfgCompiler import CfgCompiler

if __name__ == '__main__':
    compiler = CfgCompiler('test_grammar')
    print(compiler.compile())
    compiler.draw_parse_tree()
