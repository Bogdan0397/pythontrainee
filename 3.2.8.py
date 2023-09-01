class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func, *args, **kvargs):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return [self.render(x) for x in func().split()]
        # здесь строчки программы
        return wrapper



class RenderDigit():
    def __call__(self, in_str, *args, **kwargs):
        try:
            return int(in_str)
        except:
            return None
@InputValues(render = RenderDigit())
def input_dg():
    return input()



res = input_dg()
print(res)