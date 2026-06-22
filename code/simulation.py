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
    history: dict[int, list[CastawaySnapshot]] = field(default_factory=dict)

    def update_castaway(self, current_frame: int, castaway_snapshot: CastawaySnapshot):
        if current_frame not in self.history:
            self.history[current_frame] = []

        self.history[current_frame].append(castaway_snapshot)


@dataclass()
class CastawaySnapshot:
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
number = 1
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
castaways_history = CastawaysHistory()
for frame in range(number):
    for castaway_id in castaway_dict:
        current_castaway = castaway_dict[castaway_id]
        snapshot = CastawaySnapshot(castaway_id=current_castaway.castaway_id,
                                    name=current_castaway.name,
                                    position_x=current_castaway.position_x,
                                    position_y=current_castaway.position_y,
                                    movement_x=current_castaway.movement_x,
                                    movement_y=current_castaway.movement_y,
                                    have_life_jacket=current_castaway.have_life_jacket,
                                    can_swim=current_castaway.can_swim,
                                    state=current_castaway.state,
                                    temperature=current_castaway.temperature,
                                    time_in_water=current_castaway.time_in_water)
        castaways_history.update_castaway(frame, snapshot)
        castaway_dict[castaway_id].move()

print(castaways_history.history)
