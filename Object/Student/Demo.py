from Student import Student

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
bart.age = 18
print(bart.age)

print(lisa.getGender())
lisa.setGender(100)
print(lisa.getGender())

