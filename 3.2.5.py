class HandlerGET:

    def __init__(self,func):
        self.func = func


    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


    def __call__(self, request, *args, **kwargs):
        if "method" in dict.keys(request):
            if request["method"] != "GET":
                return None
        return self.get(self.func,request)




