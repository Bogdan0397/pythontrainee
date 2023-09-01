class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __setattr__(self, key, value):
        if value not in ('ul', 'ol'):
            self.type_list = 'ul'
        else:
            object.__setattr__(self,key,value)

    def __call__(self, l, *args, **kwargs):
        tag = [('<li>' + x + '</li>' + '\n') for x in l]
        string = ''.join(x for x in tag)
        return f'<{self.type_list}>\n{string}</{self.type_list}>'



lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)