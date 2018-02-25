#Dictionary

my_dict = {"name": "Bayo", "age": 20, "location": "Nigeria"}

for key, val in my_dict.iteritems(): #iteritems, just like xrange is faster
    print "My {} is {}".format(key, val)



#Set
my_set = {10, 20, 30, 40}
for x in my_set:
    print x

#tuple
my_tuple = (10, 20, 30)
for x in my_tuple:
    print x

#OOP

class Person(object):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        return "My name is {}".format(self.name)

#inheritance
class Mentor(Person):
    def __init__(self,name, mentor_name): #modifying initial class
        super(Mentor, self).__init__(name)
        self.mentor_name = mentor_name

    def show_details(self):
        super(Mentor, self).show_details()
        return "{} is a mentor".format(self.mentor_name)


bayo = Person('bayo')
print bayo.show_details()

ade = Mentor("bayo", "Einstein")
print ade.show_details()