from car import Car, MOVE_INCREMENT
MAX_NUMBER_OF_CARS = 25

class CarManager:
    def __init__(self):
        self.cars = list()
        self.init_cars()

    
    def init_cars(self):
        for i in range( 0,  MAX_NUMBER_OF_CARS + 1):
            car = Car()
            self.cars.append(car)
            

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -300:
                car.set_cor()
    
    def collision(self, t):
        for car in self.cars:
            if car.detect_collision(t) == True:
                return True
        return False

    def increase_speed(self):
        for car in self.cars:
            car.speed += MOVE_INCREMENT
                