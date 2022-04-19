class test:
    a = 1
    def A(self):
        self.a = 2
        print(self.a)

    def B(self):
        print(self.a)

if __name__ == '__main__':
    t = test()
    t.A()
    t.B()
