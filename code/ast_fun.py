import ast
import astpp
import inspect


def function_hello():
    print('hello world')


def remove_hello(function):
    # get the source given a function object
    source = inspect.getsource(function)
    # get the AST and the string
    ast_tree = ast.parse(source)
    st = ast_tree.body[0].body[0].value.args[0]

    # remove hello from the content of the string
    st.s = st.s.replace('hello ', '')
    return compile(ast_tree, __file__, mode='exec')


if __name__ == '__main__':
    function_hello()
    exec(remove_hello(function_hello))
    function_hello()
