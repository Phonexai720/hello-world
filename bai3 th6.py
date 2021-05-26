class nguoi(object):

    def getGender(self):

        return " Unknown"

class Nam(nguoi):

    def getGender(self):

        return"Nam"

class Nu(nguoi):

    def getGender(self):

        return "Nu"

aNam = Nam()

aNu = Nu()

print (aNam.getGender())

print (aNu.getGender())
