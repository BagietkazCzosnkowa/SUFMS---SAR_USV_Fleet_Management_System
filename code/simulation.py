from dataclasses import dataclass, field
from enum import Enum
import random


class CastawayState(Enum):
    LEEWAY = 'leeway'
    SWIMMING = 'swimming'
    UNCONSCIOUS = 'unconscious'
    DEAD = 'dead'


@dataclass()
class CastawaysHistory:
    history: dict[int, list[CastawaySnapchot]] = field(default_factory=dict)

    def update_castaway(self, current_id: int, castaway_snapshot: CastawaySnapchot):
        if current_id not in self.history:
            self.history[current_id] = []

        self.history[current_id].append(castaway_snapshot)


@dataclass()
class CastawaySnapchot:
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
        self.movement_x = random.uniform(-1, 1)
        self.movement_y = random.uniform(-1, 1)


random.seed()
castaway_dict: dict[int, Castaway] = {}
number = 10
for i in range(int(input('Ilu rozbitków: '))):
    castaway_dict[i] = Castaway(castaway_id=i,
                                name='Jan',
                                position_x=0.0,
                                position_y=0.0,
                                movement_x=random.uniform(-1, 1),
                                movement_y=random.uniform(-1, 1),
                                have_life_jacket=random.choice([True, False]),
                                can_swim=random.choice([True, False]),
                                state=random.choice(list(CastawayState)))
CastawaysHistory = CastawaysHistory()
for i in range(number):
    for castaway_id in castaway_dict:
        current_castaway = castaway_dict[castaway_id]
        snapshot = CastawaySnapchot(castaway_id=current_castaway.castaway_id,
                                    name=current_castaway.name,
                                    position_x=current_castaway.position_x,
                                    position_y=current_castaway.position_y,
                                    movement_x=current_castaway.movement_x,
                                    movement_y=current_castaway.movement_y,
                                    have_life_jacket=current_castaway.have_life_jacket,
                                    can_swim=current_castaway.can_swim,
                                    state=current_castaway.state)
        CastawaysHistory.update_castaway(castaway_id, snapshot)
        castaway_dict[castaway_id].move()

print(CastawaysHistory.history)
