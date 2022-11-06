INF_POINT = None


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.points = []
        self.generators =[]
        self.definePoints()
        #self.find_generators()

    def definePoints(self):
        self.points.append(INF_POINT)
        for x in range(self.p):
            for y in range(self.p):
                if self.equalModp(y * y, x * x * x + self.a * x + self.b):
                    self.points.append((x, y))

    def addition(self, P1, P2):
        if P1 == INF_POINT:
            return P2
        if P2 == INF_POINT:
            return P1

        x1 = P1[0]
        y1 = P1[1]
        x2 = P2[0]
        y2 = P2[1]

        if self.equalModp(x1, x2) and self.equalModp(y1, -y2):
            return INF_POINT

        if self.equalModp(x1, x2) and self.equalModp(y1, y2):
            u = self.reduceModp((3 * x1 * x1 + self.a) * self.inverseModp(2 * y1))
        else:
            u = self.reduceModp((y1 - y2) * self.inverseModp(x1 - x2))

        v = self.reduceModp(y1 - u * x1)
        x3 = self.reduceModp(u * u - x1 - x2)
        y3 = self.reduceModp(-u * x3 - v)

        return (x3, y3)

    def multiply(self, P1, x):
        sum = P1
        for i in range(x-1):
            #print(i)
            sum = self.addition(sum, P1)
            #print(sum)
        return sum

    def inverse(self, P1):
        return (P1[0], self.reduceModp(-1*P1[1]))

    def find_generators(self):
        for i in self.points:
            vals = []
            for j in range(1, len(self.points)+1):
                x = self.multiply(i, j)
                print(i, j ,x)
                if x not in vals:
                    vals.append(x)
            if len(vals)==len(self.points):
                self.generators.append(i)




    def testAssociativity(self):
        n = len(self.points)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    P = self.addition(self.points[i], self.addition(self.points[j], self.points[k]))
                    Q = self.addition(self.addition(self.points[i], self.points[j]), self.points[k])
                    if P != Q:
                        return False
        return True

    def numberPoints(self):
        return len(self.points)

    def discriminant(self):
        D = -16 * (4 * self.a * self.a * self.a + 27 * self.b * self.b)
        return self.reduceModp(D)

    def printPoints(self):
        print(self.points)

    # helper functions

    def reduceModp(self, x):
        return x % self.p

    def equalModp(self, x, y):
        return self.reduceModp(x - y) == 0

    def inverseModp(self, x):
        for y in range(self.p):
            if self.equalModp(x * y, 1):
                return y
        return None


# p = 67
# a = 2
# b = 3
# ec = EllipticCurve(a, b, p)
# print("a=" + str(a) + "   b=" + str(b))
# print("discriminant=" + str(ec.discriminant()))
# print("number points=" + str(ec.numberPoints()))
# print("associative=" + str(ec.testAssociativity()))
# #ec.printPoints()
# print(ec.generators)