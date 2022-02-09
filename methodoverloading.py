class Method:
    def product(self,a,b,c=10):

        if c>10:
            print("a*b*c={}".format(a*b*c))
        else:
            print("a*b={}".format(a*b))

m=Method()
m.product(10,20,30)
m.product(10,20)
