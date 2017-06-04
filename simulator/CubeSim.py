import CubeMath as cm
from Cell import *
from Tuple3d import *


class Cube2():
    """A simulation of a 2x2x2 Rubic's Cube, where R is front and Y is up
    The coordinate system is!!!
      Y▲
       │
       │
       ╳───▶X
      ╱
    Z▼

    """

    cube = []  # *24

    def __init__(self):
        for i in range(0, 6):
            cells = []
            # init as front face
            for j in range(0, 4):
                cells.append(Cell(Tuple3d(j // 2 * 2 - 1, (j % 2) * 2 - 1, 1), Tuple3d(0, 0, 1), i))

            rotator = None
            angle = None
            if i is 0:  # front
                pass
            elif i is 1:  # bottom
                rotator = cm.rotateXAxis
                angle = cm.math.pi / 2
            elif i is 2:  # back
                rotator = cm.rotateXAxis
                angle = cm.math.pi
            elif i is 3:  # top
                rotator = cm.rotateXAxis
                angle = -cm.math.pi / 2
            elif i is 4:  # left
                rotator = cm.rotateYAxis
                angle = -cm.math.pi / 2
            elif i is 5:  # right
                rotator = cm.rotateYAxis
                angle = cm.math.pi / 2

            if rotator is not None and angle is not None:
                for c in cells:
                    cm.rotateNode(c, rotator, angle)

            self.cube[i * 4: (i + 1) * 4] = cells

    def getAsFacingDict(self) -> dict:
        faces = {
            'L': [[None] * 2, [None] * 2],
            'R': [[None] * 2, [None] * 2],
            'U': [[None] * 2, [None] * 2],
            'D': [[None] * 2, [None] * 2],
            'F': [[None] * 2, [None] * 2],
            'B': [[None] * 2, [None] * 2],
        }

        for c in self.cube:
            loc = c.getLocation()
            s = (loc.x * c.getNormal().x, loc.y * c.getNormal().y, loc.z * c.getNormal().z)  # scalarproduct

            if sum([x is 1 for x in s]) == 1:
                x = (loc.x + 1) // 2
                y = (loc.y + 1) // 2
                z = (loc.z + 1) // 2

                def inv(p, b):
                    return p if b else 1 - p

                if s[0]:
                    if False:
                        print(c.getColor(), ":", s, "-", loc, "*", c.getNormal())
                        print(1 - y, inv(z, not x))
                    faces['R' if x else 'L'][1 - y][inv(z, not x)] = c
                elif s[1]:
                    if False:
                        print(c.getColor(), ":", s, "-", loc, "*", c.getNormal())
                        print(inv(z, y), x)
                    faces['U' if y else 'D'][inv(z, y)][x] = c
                elif s[2]:
                    if False:
                        print(c.getColor(), ":", s, "-", loc, "*", c.getNormal())
                        print(y, x)
                    faces['F' if z else 'B'][1 - y][inv(x, z)] = c
        return faces

    def __str__(self, color=lambda c: c.getColor(), sep="|", space=" ") -> str:
        # Block building ┌┐└┘ OR — + |

        faces = self.getAsFacingDict()
        # print(faces)
        return_string = ""
        for i in range(0, 2):
            return_string += " " * 4 + sep + space.join([color(c) for c in faces['U'][i]]) + sep + "\n"
        for i in range(0, 2):
            for f in "LFRB":
                return_string += sep + space.join([color(c) for c in faces[f][i]])
            return_string += sep + "\n"
        for i in range(0, 2):
            return_string += " " * 4 + sep + space.join([color(c) for c in faces['D'][i]]) + sep + "\n"
        return return_string

    def __repr__(self) -> str:
        return self.__str__(lambda c: c.getXTermColor(), sep="", space="")

    def doAction(self, actions: str):
        for a in actions.split(" "):
            angle = cm.math.pi / 2 * (1 - (len(a) > 1 and a[1] == "'") * 2)
            mode = None

            if a[0] is "F":
                def decider(l): return l.z == 1
                mode = cm.rotateZAxis
                angle *= -1
            elif a[0] is "B":
                def decider(l): return l.z == -1
                mode = cm.rotateZAxis
            elif a[0] is "L":
                def decider(l): return l.x == -1
                mode = cm.rotateXAxis
            elif a[0] is "R":
                def decider(l): return l.x == 1
                mode = cm.rotateXAxis
                angle *= -1
            elif a[0] is "U":
                def decider(l): return l.y == 1
                mode = cm.rotateYAxis
                angle *= -1
            elif a[0] is "D":
                def decider(l): return l.y == -1
                mode = cm.rotateYAxis

            cache = []
            for c in self.cube:
                if decider(c.getLocation()):
                    cache.append(c)

            # print(len(cache))

            for c in cache:
                cm.rotateNode(c, mode, angle)


if __name__ == '__main__':
    c = Cube2()
    # print(c.getAsFacingDict())
    # print(c)
    print(c.__repr__())
    for x in "R B R' B' R B R' F' R B' R' B R B' R' F".split(" "):
        input()
        print("Do:", x)
        c.doAction(x)
        print(c.__repr__())

    # c.doAction("R B R' B' R B R' F' R B' R' B R B' R' F")
    # print(c.__repr__())
