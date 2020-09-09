import pickle

# pythonで使うぶんには便利だが、他の言語からアクセスできない


class T(object):
    def __init__(self, name):
        self.name = name


data = {"a": [1, 2, 3], "b": ("test1", "test2"), "d": {"key": "value"}, "c": T("tets")}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
    print(type(data_loaded["a"]))
    print(type(data_loaded["b"]))
    print(type(data_loaded["c"]))
    print(type(data_loaded["d"]))
