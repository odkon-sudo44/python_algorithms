import random
from datetime import date
from Practice1.notebook_dataclass import Notebook

class Generator:
    manufacturers = ("Dell", "ASUS", "Acer", "Lenovo", "HP", "Apple")
    models = ("XPS 13", "ROG Strix", "Aspire 5", "IdeaPad 3", "Pavilion", "MacBook Air")
    cpus = ("Intel i3", "Intel i5", "Intel i7", "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "Intel Celeron")
    screen_sizes = (13.3, 14.0, 15.6, 17.3)
    memories = (4, 8, 16, 32)
    storages = (128, 256, 512, 1024)

    def __create_date(self) -> date:
        cur_year = date.today().year
        year = random.randint(1930, cur_year)
        month = random.randint(1, 12)

        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)
        return date(year, month, day)

    def generate_single(self) -> Notebook:
        manufacturer = random.choice(self.manufacturers)
        model = random.choice(self.models)
        screen_size = random.choice(self.screen_sizes)
        memory = random.choice(self.memories)
        cpu = random.choice(self.cpus)
        storage = random.choice(self.storages)
        birthday = self.__create_date()
        return Notebook(manufacturer, model, screen_size, memory, cpu, storage, birthday)

    def generate_1000(self) -> list:
        plist = list()
        for i in range(1000):
            plist.append(self.generate_single())
        return plist

    def generate_10_000(self) -> list:
        plist = [self.generate_single() for i in range(10000)]
        return plist

