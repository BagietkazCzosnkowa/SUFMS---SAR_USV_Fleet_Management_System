from dataclasses import dataclass
from enum import Enum
import random


class CastawayState(Enum):
    LEEWAY = 'leeway'
    SWIMMING = 'swimming'
    UNCONSCIOUS = 'unconscious'
    DEAD = 'dead'


@dataclass
class Castaway:
    castaway_id: int
    name: str
    position_x: float
    position_y: float
    movement_x: float
    movement_y: float
    have_life_jacket: bool
    can_swim: bool
    state: CastawayState

    temperature: float = 36.6
    time_in_water: int = 0

    def move(self):
        self.position_x += self.movement_x
        self.position_y += self.movement_y
        self.movement_x = round(random.uniform(-1, 1), 5)
        self.movement_y = round(random.uniform(-1, 1), 5)


random.seed()
castaway_dict = {}
for i in range(int(input('Ilu rozbitków: '))):
    castaway_dict[f'castaway_{i}'] = Castaway(castaway_id=i,
                                              name='Jan',
                                              position_x=0.0,
                                              position_y=0.0,
                                              movement_x=round(random.uniform(-1, 1), 5),
                                              movement_y=round(random.uniform(-1, 1), 5),
                                              have_life_jacket=random.choice([True, False]),
                                              can_swim=random.choice([True, False]),
                                              state=random.choice(list(CastawayState)))

for _ in range(1000):
    for castaway_id in castaway_dict:
        castaway_dict[castaway_id].move()
