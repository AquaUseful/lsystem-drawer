import utils
from PIL.Image import Image


class Lsystem(object):
    def __init__(self, inititator: str, rules: dict = {}) -> None:
        self.initiator = inititator
        self.rules = rules
        self.strings = None

    def set_inititator(self, inititator: str) -> None:
        self.initiator = inititator

    def set_rules(self, rules: Dict) -> None:
        self.rules = rules

    def get_initiator(self) -> str:
        return self.initiator

    async def generate_strings(self, iterations: int) -> None:
        strings = [self.initiator]
        for it in range(iterations):
            strings.append(
                map(lambda char: self.rules[char] if char in self.rules else char, strings[it]))


class LsystemImage(object):
    def __init__(self, lsystem: Lsystem,
                 size: tuple = (0, 0),
                 start_coords: tuple = (0, 0),
                 start_angle: int = 0,
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

    def gen_lsystem_image(lsystem, size, bg_color, draw_params):
        img = Image.new("RGBA", size, bg_color)
        dr = Draw(img)
        draw_lsystem(dr, lsystem, *draw_params, size)
        del dr
        return img

    def generate_image(self, iteration: int) -> Image:
        pass
