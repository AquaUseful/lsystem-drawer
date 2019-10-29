import utils
from PIL.Image import Image
from PIL.ImageDraw import Draw, ImageDraw


class Lsystem(object):
    def __init__(self, name: str, inititator: str, rules: dict) -> None:
        self.initiator = inititator
        self.rules = rules
        self.strings = []

    def set_inititator(self, inititator: str) -> None:
        self.initiator = inititator

    def set_rules(self, rules: Dict) -> None:
        self.rules = rules

    def get_initiator(self) -> str:
        return self.initiator

    def get_strings(self):
        pass

    def get_string(self, iteration):
        return self.strings[iteration]

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

    def _draw_lsystem(self) -> None:
        not_drawn_lines = 0
        x, y = self.start_coords[0], self.start_coords[1]
        angle = self.start_angle
        stack = []
        for char in lsystem:
            if char == "F":
                new_x, new_y = point_on_circle((x, y), step_length, angle)
                if check_coords((x, y), (new_x, new_y), max_coords):
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
        self._draw_lsystem()
