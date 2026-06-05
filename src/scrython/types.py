from enum import Enum
from typing import Union, Literal

MotionTarget = Union['Sprite', Literal['random', 'mouse-pointer']]
PointTarget = Union['Sprite', Literal['mouse-pointer']]
CollisionTarget = Union['Sprite', Literal['mouse-pointer', 'edge']]
DistanceTarget = Union['Sprite', Literal['mouse-pointer']]
CloneTarget = Union['Sprite']

def when_started(func): pass
def when_key_pressed(key: str): pass
def when_backdrop_switches(backdrop: str): pass
def when_loudness_is_over(volume: float): pass
def when_timer_is_over(time: float): pass
def when_i_recieve(message: str): pass
def when_this_sprite_clicked(func): pass
def when_cloned(func): pass
def when_stage_clicked(func): pass


# This is an especially ugly way to do this, but it at least gives auto-complete
Key = Literal['space', 'up arrow', 'down arrow', 'right arrow', 'left arrow', 'any', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Costumes is a decorator that takes an array of strings (names)
class Assets():
    pass

class RotationStyle(Enum):
    LEFT_RIGHT = 0
    RIGHT_LEFT = 1

class Effect(Enum):
    COLOR = 0
    FISHEYE = 1
    WHIRL = 2
    PIXELATE = 3
    MOSAIC = 4
    BRIGHTNESS = 5
    GHOST = 6

class AudioEffects(Enum):
    PITCH = 0
    PAN_LEFT_OR_RIGHT = 1

class __common():
    def set_backdrop(backdrop: str) -> None: pass
    def next_backdrop() -> None: pass

    def change_effect(effect: Effect, increase: float) -> None: pass
    def set_effect(effect: Effect, value: float) -> None: pass
    def clear_graphic_effects() -> None: pass

    def get_backdrop_number(self) -> int: pass
    def get_backdrop_name(self) -> str: pass

    def play_sound_until_done(self, name: str) -> None: pass
    def start_sound(self, name: str) -> None: pass
    def stop_all_sounds(self) -> None: pass

    def change_audio_effect(effect: AudioEffects) -> None: pass
    def set_audio_effect(effect: AudioEffects) -> None: pass
    def clear_audio_effects() -> None: pass
    def change_volume(percentage: float) -> None: pass
    def set_volume(percentage: float) -> None: pass
    def get_volume() -> float: pass

    def broadcast(message: str) -> None: pass
    def broadcast_and_wait(message: str) -> None: pass
    def wait(seconds: float): pass
    def wait_until(condition: bool) -> None: pass
    def stop_all() -> None: pass
    def stop_this_script() -> None: pass
    def stop_other_scripts() -> None: pass
    def create_clone_of(target: CloneTarget) -> None: pass

    def ask(question: str) -> None: pass
    def get_answer() -> str: pass
    def is_key_pressed(key: Key) -> bool: pass
    def is_mouse_down() -> bool: pass
    def get_mouse_x() -> int: pass
    def get_mouse_y() -> int: pass
    def set_draggable(draggable: bool) -> None: pass
    def get_loudness() -> int: pass
    def get_timer() -> float: pass
    def reset_timer() -> None: pass
    def get_attribute(attribute: str, target: Sprite) -> any: pass
    def get_year() -> int: pass
    def get_month() -> int: pass
    def get_date() -> int: pass
    def get_day_of_week() -> int: pass
    def get_hour() -> int: pass
    def get_minute() -> int: pass
    def get_second() -> int: pass
    def is_online() -> bool: pass
    def get_username() -> str: pass
    def get_random(min: int | float, max: int | float) -> int | float: pass
    def show_variable(variable: str) -> None: pass
    def hide_variable(variable: str) -> None: pass

class Sprite(__common):
    def move_steps(self, steps: float | int) -> None: pass
    def turn_degrees_right(self, degrees: float) -> None: pass
    def turn_degrees_left(self, degrees: float) -> None: pass
    def goto_target(self, target: MotionTarget) -> None: pass
    def goto(self, x: float | int, y: float | int) -> None: pass
    def glide_to_target(self, seconds: float, target: MotionTarget) -> None: pass
    def glide(self, seconds: float, x: float | int, y: float | int) -> None: pass
    def point(self, direction: float) -> None: pass
    def point_at(self, target: PointTarget) -> None: pass
    def change_x(self, x: float) -> None: pass
    def set_x(self, x: float) -> None: pass
    def change_y(self, y: float) -> None: pass
    def set_y(self, y: float) -> None: pass
    def if_on_edge_bounce(self) -> None: pass
    def set_rotation_style(self, rotation_style: RotationStyle) -> None: pass
    def get_x(self) -> float: pass
    def get_y(self) -> float: pass
    def get_direction(self) -> float: pass
    def say(self, message: str, seconds: float | None) -> None: pass
    def think(self, message: str, seconds: float | None) -> None: pass
    def set_costume(costume: str) -> None: pass
    def next_costume() -> None: pass
    def change_size(size: float) -> None: pass
    def set_size(size: float) -> None: pass
    def show(self) -> None: pass
    def hide(self) -> None: pass
    def go_to_front(self) -> None: pass
    def go_to_back(self) -> None: pass
    def go_forward_layers(self, layers: int) -> None: pass
    def go_backward_layers(self, layers: int) -> None: pass
    def get_costume_number(self) -> int: pass
    def get_costume_name(self) -> str: pass
    def get_size(self) -> float: pass
    def delete_this_clone() -> None: pass
    def is_touching(target: CollisionTarget) -> bool: pass
    def is_color_touching_color(color1: str, color2: str) -> bool: pass
    def distance_to(target: CollisionTarget) -> float: pass
    

class Stage(__common):
    pass