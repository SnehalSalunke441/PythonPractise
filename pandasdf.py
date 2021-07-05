import pandas as pd

names = ['UN', 'India', 'Germany']
dr = [ True, False, True]
cpc = [100, 23, 45]

my_dict = {'country': names , 'drives_right': dr, 'cars_per_cap' : cpc}
cars = pd.DataFrame(my_dict)
print(cars)