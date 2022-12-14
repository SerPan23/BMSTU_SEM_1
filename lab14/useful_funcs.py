def input_with_params(input_text, error_text, expression):
    var = None
    while var is None:
        try:
            var = input(input_text)
            tmp = expression.split()
            tmp[tmp.index('var')] = str(var)
            tmp = ''.join(tmp)
            if eval(tmp):
                raise Exception()
        except:
            var = None
            print(error_text)
    return var