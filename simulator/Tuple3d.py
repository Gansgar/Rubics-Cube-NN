class Tuple3d():
    """docstring for Tuple3D"""

    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def fromTuple3d(self, parent: "Tuple3d") -> "Tuple3d":
        return Tuple3d(parent.x, parent.y, parent.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
