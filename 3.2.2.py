class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions


    def __call__(self, *args, **kwargs):
        for i in self.extensions:
            if '.'+i in args[0]:
                return args[0]




fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpg", "png"))
res = filter(acceptor, fs)

print(set(res) == set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]))# "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"

acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"