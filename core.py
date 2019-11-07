from utils import point_on_circle, check_coords
from PIL import Image
from PIL.ImageDraw import Draw, ImageDraw
from math import pi
from itertools import chain


class Lsystem(object):
    def __init__(self, name: str, inititator: str, rules: dict) -> None:
        self.name = name
        self.initiator = inititator
        self.rules = rules
        self.string = inititator
        self.last_req = 0

    def set_inititator(self, inititator: str) -> None:
        if inititator == self.initiator:
            return
        self.initiator = inititator
        self._param_changed()

    def set_rules(self, rules: dict) -> None:
        if rules == self.rules:
            return
        self.rules = rules
        self._param_changed()

    def get_initiator(self) -> str:
        return self.initiator

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def generate_string(self, iteration: int) -> str:
        if iteration == self.last_req:
            return self.string
        self.last_req = iteration
        string = self.initiator
        for _ in range(iteration):
            string = chain(
                *map(lambda char: self.rules[char] if char in self.rules else char, string))
        self.string = "".join(string)
        return self.string

    def _param_changed(self) -> None:
        self.last_req = 0


class LsystemImage(object):
    def __init__(self, lsystem: Lsystem,
                 size: tuple = (0, 0),
                 start_coords: tuple = (0, 0),
                 start_angle: float = 0,
                 rot_angle: float = 0,
                 step_length: int = 1,
                 bg_color="#000000",
                 line_color="#FFFFFF") -> None:
        self.lsystem = lsystem
        self.size = size
        self.start_coords = start_coords
        self.start_angle = start_angle
        self.rot_angle = rot_angle
        self.step_length = step_length
        self.bg_color = bg_color
        self.line_color = line_color

    def _make_empty_image(self) -> None:
        self.image = Image.new("RGBA", self.size, self.bg_color)

    def _make_draw(self) -> None:
        self.draw = Draw(self.image)

    def _draw_lsystem(self) -> None:
        not_drawn_lines = 0
        x, y = self.start_coords[0], self.start_coords[1]
        angle = self.start_angle
        stack = []
        for char in self.string:
            if char == "F":
                new_x, new_y = point_on_circle((x, y), self.step_length, angle)
                if check_coords((x, y), (new_x, new_y), self.size):
                    self.draw.line(((x, y), (new_x, new_y)),
                                   fill=self.line_color, width=1)
                    not_drawn_lines = 0
                else:
                    not_drawn_lines += 1
                x, y = new_x, new_y
            elif char == "f":
                x, y = point_on_circle((x, y), self.step_length, angle)
            elif char == "+":
                angle -= self.rot_angle
            elif char == "-":
                angle += self.rot_angle
            elif char == "|":
                angle += pi
            elif char == "[":
                stack.append((x, y, angle))
            elif char == "]":
                x, y, angle = stack.pop()
            if not_drawn_lines >= 30000:
                break

    def get_image(self) -> Image:
        return self.image

    def update_image(self, iteration: int) -> None:
        self.string = self.lsystem.generate_string(iteration)
        self._make_empty_image()
        self._make_draw()
        self._draw_lsystem()

    def set_size(self, size: tuple) -> None:
        self.size = size

    def set_size(self, heigth: int, width: int) -> None:
        self.size = (heigth, width)

    def set_start_coords(self, coords: tuple) -> None:
        self.start_coords = coords

    def set_start_coords(self, x: int, y: int) -> None:
        self.start_coords = (x, y)

    def set_start_angle(self, angle: float) -> None:
        self.start_angle = angle

    def set_rot_angle(self, angle: float) -> None:
        self.rot_angle = angle

    def set_step_length(self, length: int) -> None:
        self.step_length = length

    def set_bg_color(self, color) -> None:
        self.bg_color = color

    def set_line_color(self, color) -> None:
        self.line_color = color

    def get_size(self) -> tuple:
        return self.size
