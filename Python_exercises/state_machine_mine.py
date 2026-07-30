from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class State:
    def next(self, input: int) -> "State":
        return self
    def ouput(self) -> str:
        return ""

@dataclass
class MyState(Enum):
    INIT = auto()
    LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_LIGHT_ON = auto()

@dataclass
class S_Init(State):
    def next(self, input: int) -> State:
        match input:
            case "SENSE_ACC":
                return ***
        return self

S = MyState


def next_state(state: "MyState", input: str) -> "MyState":
    match state:
        case S.INIT:
            if input == ("SENSE_ACC") * 2:
                return state.LIGHT_ON
                
            if input == ("SENS_TAP") * 2:
                return state.SCREEN_ON
        
        case S.LIGHT_ON:
            if input == ("SENS_ACC") * 2:
                return state.INIT

            if input == ("SENS_TAP") * 2:
                return state.SCREEN_LIGHT_ON
            
        case S.SCREEN_ON:
            if input == ("SENS_TAP") * 2:
                return state.INIT
                
            if input == ("SENS_ACC") * 2:
                return state.SCREEN_LIGHT_ON
    return S.INIT


@dataclass
class S_after(State):
    prefix: list[str]
    def next(self, input: str) -> State:
        self.prefix = self.prefix + [input]
        match self.prefix:
            case
