from typing import Iterable
from crossroad import Crossroad
from road_net import RoadNet


def main():
    rng_crossr = range(0, 20)

    crossroads = init_crossroads(rng_crossr)
    rn = RoadNet(crossroads)

    return 0


def init_crossroads(rng: Iterable) -> Iterable:
    return [Crossroad(uuid=i) for i in rng]


if __name__ == '__main__':
    main()
else:
    print("Fatal Error: no entering point!")
    exit(-1)
