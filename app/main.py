class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[-1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[-1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step
