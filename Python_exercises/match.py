from dataclasses import dataclass
from enum import Enum

@dataclass
class hammer:
    size = int

@dataclass
class bohrer:
    size = int

@dataclass
class werkzeug:
    kind = hammer | bohrer
    size = int


def was_bist_du(werkzeug1: werkzeug) -> str :
    match werkzeug1.kind:
        case werkzeug(hammer):
            return "Du hast einen Hammer der Größe: "+ str(werkzeug.size)
        case werkzeug(bohrer):
            return "Du hast einen Bohrer der Größe: " + str(werkzeug.size) + " vom Hersteller: "+ str(werkzeug.hersteller)