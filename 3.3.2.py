class Model:
    def query(self, **kwargs):
        self.data_base = kwargs
        self.doc = "Model: "
        self.doc += ', '.join(f"{i} = {j}" for i, j in self.data_base.items())


    def __repr__(self):

        return self.doc


m = Model()

m.query(id=1, fio='Sergey', old=33)

print(m)
