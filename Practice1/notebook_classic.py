from Practice1.abstract_object import AbstractObject


class Notebook(AbstractObject):
    manufacturer: str
    model: str
    screen_size: float
    cpu: str
    memory: int
    storage: int

    def __init__(self, manufacturer, model, screen_size, cpu, memory, storage):
        self.manufacturer = manufacturer
        self.model = model
        self.screen_size = screen_size
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def get_info(self) -> str:
        return (f"Екран: {self.screen_size}\", CPU: {self.cpu}, "
                f"RAM: {self.memory}GB, Сховище: {self.storage}GB")

    def get_message(self) -> str:
        specs = self.get_info()
        is_mid_high_cpu = any(x in self.cpu for x in ["i5", "i7", "Ryzen 5", "Ryzen 7"])
        is_budget_cpu = any(x in self.cpu for x in ["i3", "Ryzen 3"])

        if self.screen_size < 15 and self.memory >= 8 and is_mid_high_cpu:
            return (f"Вас зацікавила бізнес-модель {self.manufacturer} {self.model} "
                    f"з характеристиками: {specs}")
        elif self.screen_size >= 15 and self.memory >= 8 and is_mid_high_cpu:
            return (f"Вас зацікавила ігрова модель {self.manufacturer} {self.model} "
                    f"з характеристиками: {specs}")
        elif self.screen_size >= 15 and self.memory < 8:
            return (f"Вас зацікавила мультимедійна модель {self.manufacturer} {self.model} "
                    f"з характеристиками: {specs}")
        elif is_budget_cpu:
            return (f"Вас зацікавив бюджетний ноутбук {self.manufacturer} {self.model} "
                    f"з характеристиками: {specs}")
        else:
            return (f"Вас зацікавив ноутбук {self.manufacturer} {self.model} "
                    f"з характеристиками: {specs}")


test_notebooks = [
    Notebook("Dell", "XPS 13", 13.3, "Intel i7", 16, 512),

    Notebook("ASUS", "ROG Strix", 15.6, "AMD Ryzen 7", 16, 1024),

    Notebook("Acer", "Aspire 5", 15.6, "Intel i3", 4, 256),

    Notebook("Lenovo", "IdeaPad 3", 14.0, "AMD Ryzen 3", 8, 256),

    Notebook("HP", "Pavilion", 14.0, "Intel Celeron", 4, 128),
]

for i, nb in enumerate(test_notebooks, start=1):
    print(f"--- Тест {i} ---")
    print(nb.get_message())
    print()
