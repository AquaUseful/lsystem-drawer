from utils import point_on_circle, check_coords
from PIL.Image import Image
from PIL.ImageDraw import Draw, ImageDraw
from math import pi


class Lsystem(object):
    def __init__(self, name: str, inititator: str, rules: dict) -> None:
        self.name = name
        self.initiator = inititator
        self.rules = rules
        self.strings = []

    def set_inititator(self, inititator: str) -> None:
        self.initiator = inititator

    def set_rules(self, rules: dict) -> None:
        self.rules = rules

    def get_initiator(self) -> str:
        return self.initiator

    def get_strings(self):
        pass

    def get_string(self, iteration):
        return self.strings[iteration]

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def update_strings(self, iterations: int) -> None:
        strings = [self.initiator]
        for it in range(iterations):
            strings.append(str(
                map(lambda char: self.rules[char] if char in self.rules else char, strings[it])))


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

    def _draw_lsystem(self, iteration: int) -> None:
        not_drawn_lines = 0
        x, y = self.start_coords[0], self.start_coords[1]
        angle = self.start_angle
        stack = []
        string = self.lsystem.get_string(iteration)
        for char in string:
            if char == "F":
                new_x, new_y = point_on_circle((x, y), step_length, angle)
                if check_coords((x, y), (new_x, new_y), self.size):
                    self.draw.line(((x, y), (new_x, new_y)),
                                   fill=line_color, width=1)
                    not_drawn_lines = 0
                else:
                    not_drawn_lines += 1
                x, y = new_x, new_y
            elif char == "f":
                x, y = point_on_circle((x, y), step_length, angle)
            elif char == "+":
                angle += self.rotation_angle
            elif char == "-":
                angle -= self.rotation_angle
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
        self._make_empty_image()
        self._make_draw()
        self._draw_lsystem(iteration)

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
