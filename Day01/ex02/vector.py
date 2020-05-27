class Vector():
    """vector"""

    def __init__(self, *args):
        if isinstance(args[0], list):
            self.val = args[0]
            self.size = len(args[0])
        elif isinstance(args[0], tuple):
            self.nval = 0
            if len(args[0]) == 2:
                self.nval = args[0][0]
                self.size = args[0][1] - args[0][0]
                self.val = []
                for i in range(self.size):
                    self.val.append(float(self.nval))
                    self.nval += 1
        elif isinstance(args[0], int):
            self.nval = 0
            self.size = args[0]
            self.val = []
            for i in range(self.size):
                self.val.append(float(self.nval))
                self.nval += 1
        else:
            print("Bad parameters, enter a size/list/range for the vector")
            exit()

    def __add__(self, new_vec):
        total = []
        if isinstance(new_vec, Vector):
            for i, j in zip(self.val, new_vec.val):
                total.append(i + j)
        elif isinstance(new_vec, int):
            for i in range(len(self.val)):
                total.append(self.val[i] + new_vec)
        return Vector(total)

    def __sub__(self, new_vec):
        total = []
        if isinstance(new_vec, Vector):
            for i, j in zip(self.val, new_vec.val):
                total.append(i - j)
        elif isinstance(new_vec, int):
            for i in range(len(self.val)):
                total.append(self.val[i] - new_vec)
        return Vector(total)

    def __truediv__(self, div):
        if isinstance(div, int):
            total = []
            for i in range(len(self.val)):
                total.append(self.val[i] / div)
            return Vector(total)
        else:
            print("Only scalars accepted for div")
            exit()

    def __mul__(self, new_vec):
        total = []
        if isinstance(new_vec, Vector):
            for i, j in zip(self.val, new_vec.val):
                total.append(i * j)
        elif isinstance(new_vec, int):
            for i in range(len(self.val)):
                total.append(self.val[i] * new_vec)
        return Vector(total)

    def __radd__(self, new_vec):
        if new_vec == 0:
            return self
        else:
            return self.__add__(new_vec)

    def __rsub__(self, new_vec):
        if new_vec == 0:
            return self
        else:
            return self.__sub__(new_vec)

    def __rtruediv__(self, new_vec):
        if new_vec == 0:
            return self
        else:
            return self.__truediv__(new_vec)

    def __rmul__(self, new_vec):
        if new_vec == 0:
            return self
        else:
            return self.__mul__(new_vec)

    def __str__(self):
        return "Vector: {}".format(self.val)

    def __repr__(self):
        return "Vector: \'{}\'".format(self.val)
