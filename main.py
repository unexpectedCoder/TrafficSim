import random

from road_net import RoadNet


def main():
    edges = init_nodes(20)
    rn = RoadNet(edges)
    rn.show()

    return 0


def init_nodes(n: int):
    return [(i, i+1, {'weight': random.randint(1, 10)})
            for i in range(n)]


if __name__ == '__main__':
    main()
else:
    print("Fatal Error: no entering point!")
    exit(-1)
