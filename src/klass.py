class TestA():
    X = 1
    Y = 1
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y

    def test_a(self, msg):
        print("A : " + msg)

    def test(self, msg):
        print("A test" + msg)

class TestB(TestA):
    X = 2 
    def __init__(self, x=1, y=2):
        self.xb = x
        self.yb = y

    def test(self, msg):
        print("B test: " + msg)

    def test_b(self, msg):
        print( "B : " + msg)

class TestC(TestB, TestA):
	Y = 3
	def __init__(self, x=5, y=6):
		super(TestB, self).__init__(x, y)
		self.c = x
		self.c = y

	def test(self, msg):
		print("C test : " + msg)

	def test_c(slef, msg):
		print( "C : " + msg)

