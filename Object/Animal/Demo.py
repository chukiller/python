import Dog, Cat

dog = Dog.Dog()
dog.run()

cat = Cat.Cat()
cat.run()

def run_twice(func):
    func.run()

run_twice(dog)
run_twice(cat)
