from car import Car
from road_lane import RoadLane


def main():
    print(Car())

    n_cars = 10
    cars = [Car(i) for i in range(0, 2*n_cars, 2)]
    roadLane = RoadLane(30, cars)
    roadLane.show()
    print(roadLane)

    return 0


if __name__ == '__main__':
    main()
else:
    print("Fatal Error: no entering point!")
    exit(-1)
