import my_module

my_module.greet('Danny')

my_module.calc_sqCube(3)

x , y =my_module.calc_sqCube(3)
print("the square of number is {} and cube of it is {}".format(x,y))

dir(my_module)

# aliasing a module
import num_module as nm

dir(num_module)

nm.tbl(5)

from my_module2 import func2

func2(10)

func1()
