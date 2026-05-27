import datetime
from dataclasses import dataclass
from Practice1.abstract_object import AbstractObject


@dataclass(order=True)
class Notebook(AbstractObject):
    manufacturer: str
    model: str

    screen_size: float
    memory: int
    cpu: str
    storage: int
    birthday: datetime.date = datetime.date(2024, 1, 1)

    # internal storage for validated properties — do not make these dataclass fields

    def __post_init__(self):
        """Validate and move annotated values into internal attributes using setters.

        This avoids declaring private attributes as dataclass fields (which can
        cause field ordering issues)."""
        # Use setters to validate and store values in private attributes
        self.screen_size = self.screen_size
        self.memory = self.memory

    def get_info(self) -> str:
        return f"{self.manufacturer} {self.model} ({self.screen_size}\", {self.cpu}, {self.memory}GB RAM, {self.storage}GB SSD)"

    def __repr__(self) -> str:
        return self.get_info()

    def get_message(self) -> str:
        cpu_lower = self.cpu.lower()

        specs = f"{self.screen_size}\", RAM {self.memory}GB, CPU {self.cpu}, Storage {self.storage}GB"

        if "i3" in cpu_lower or "ryzen 3" in cpu_lower:
            model_type = "бюджетний ноутбук"

        elif self.screen_size < 15.0 and self.memory >= 8 and (
                "i5" in cpu_lower or "i7" in cpu_lower or "ryzen 5" in cpu_lower or "ryzen 7" in cpu_lower
        ):
            model_type = f"бізнес-модель {self.manufacturer} {self.model}"
            return f"Вас зацікавила {model_type} з характеристиками: {specs}"

        elif self.screen_size >= 15.0 and self.memory >= 8 and (
                "i5" in cpu_lower or "i7" in cpu_lower or "ryzen 5" in cpu_lower or "ryzen 7" in cpu_lower
        ):
            model_type = f"ігрова модель {self.manufacturer} {self.model}"
            return f"Вас зацікавила {model_type} з характеристиками: {specs}"

        elif self.screen_size >= 15.0 and self.memory < 8:
            model_type = f"мультимедійна модель {self.manufacturer} {self.model}"
            return f"Вас зацікавила {model_type} з характеристиками: {specs}"

        else:
            return f"Вас зацікавив ноутбук {self.manufacturer} {self.model} з характеристиками: {specs}"

        return f"Вас зацікавив {model_type} {self.manufacturer} {self.model} з характеристиками: {specs}"

    def _get_screen_size(self) -> float:
        return self.__screen_size

    def _set_screen_size(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Розмір екрану має бути числом (float або int)!")
        if value <= 0:
            raise ValueError("Розмір екрану не може бути нульовим або від'ємним!")
        self.__screen_size = float(value)

    def _get_memory(self) -> int:
        return self.__memory

    def _set_memory(self, value: int):
        if type(value) != int:
            raise TypeError("Об'єм оперативної пам'яті має бути цілим числом (int)!")
        if value <= 0:
            raise ValueError("Об'єм пам'яті має бути більшим за 0!")
        self.__memory = value

# Attach properties after the dataclass has been processed to avoid
# dataclass interpreting these as default values (which would break
# field ordering validation).
Notebook.screen_size = property(Notebook._get_screen_size, Notebook._set_screen_size)
Notebook.memory = property(Notebook._get_memory, Notebook._set_memory)
