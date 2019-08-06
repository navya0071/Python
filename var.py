#ex4.py


cars = 100
spaceincar = 5
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
car_driven = drivers
carpool_capacity =  car_driven * spaceincar
average_passengers_per_car = passengers/car_driven

print("there are",cars,"cars available")
print("there are only",drivers,"drivers available")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have",passengers,"to carpool today")
print("we need to put about",average_passengers_per_car,"in each car.")
