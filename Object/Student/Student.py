class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    def getGender(self):
        return self._gender

    def setGender(self, gender):
        self._gender = gender

    def print_score(self):
        print('%s: %s' % (self._name, self._gender))

if __name__=='__main__':
    print('Student')

