class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


# здесь объявляйте остальные классы
class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def check_method(self, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

    def get(self,request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request.keys():
            raise TypeError('request не содержит обязательного ключа url')

        return f"urL: {request['url']}"
    def render_request(self, request, method):
        self.check_method(method)
        return getattr(self,method.lower())(request)
        #self.__getattribute__(method.lower())(request)


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)