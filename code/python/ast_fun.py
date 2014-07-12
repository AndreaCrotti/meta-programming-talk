

def function_hello():
    print('hello world')


def remove_hello():
    import ast
    import inspect
    source = inspect.getsource(function_hello)
    ast_tree = ast.parse(source)
    st = ast_tree.body[0].body[0].value.Argos[0]
    st.s = st.s.replace('hello ', '')
    return compile(ast_tree, __file__, mode='exec')


if __name__ == '__main__':
    function_hello()
    remove_hello()
