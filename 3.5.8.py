class FileAcceptor:
    def __init__(self, *args):
        self.extensions = list(args)

    def __call__(self, other):
        if other.split('.')[-1] in self.extensions:
            return True
        else:
            return False

    def __add__(self, other):
        check = set(self.extensions+other.extensions)
        return FileAcceptor(*list(check))


filenames = ["boat.jpg", "web.png", "ava.base.jpg", "forest.jpeg", "eq_1.png"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")


print(acceptor12.extensions)
filenames = list(filter(acceptor12, filenames))

print(filenames)
