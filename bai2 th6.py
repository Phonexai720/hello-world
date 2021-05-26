class Hinhchunhat(object):

    def _init_(sell,l,w):

        self.dai = l

        self.rong = w

    def area(self):

        return self.dai*self.rong

aHinhchunhat = Hinhchunhat(5,4)

print(aHinhchunhat.area())
