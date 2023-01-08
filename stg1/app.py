import utils
import random
# import ecomm.shipping
# ecomm.shipping.calc_ship

# from ecomm import shipping
# becomes shipping.calc_ship

from ecomm.shipping import calc_ship


for i in range(3):
    print(random.randint(23, 857))

utils.time_stamp("3:25")
numbers = [1, 31, 5, 1, 24, 46, 7, 68, 24, 46, 62, 46, 35, 57, 53, 35, 46, 35, 57, 24, 35, 24, 52, 24, 24, 75, 124, 87]
print(utils.find_max(numbers))
print(calc_ship(100))

utils.roll_dice()
utils.roll_dice()
utils.roll_dice()
utils.roll_dice()
