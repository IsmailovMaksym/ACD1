from dataclasses import dataclass


@dataclass
class Bag:
    brand: str
    color: str
    material: str
    type: str
    category: str
    price: float

    def validate(self) -> str:
        valid_combinations = {
            "Косметички": {"Жінкам": "поліестер", "Дівчаткам": "поліестер"},
            "Несесери": {"Жінкам": "поліестер", "Дівчаткам": "поліестер"},
            "Портмоне": {"Чоловікам": ["шкіра", "екошкіра"]},
            "Валізи": {"Жінкам": ["шкіра", "екошкіра"], "Чоловікам": ["шкіра", "екошкіра"],
                       "Хлопчикам": ["шкіра", "екошкіра"], "Дівчаткам": ["шкіра", "екошкіра"]},
            "Сумки": {"Жінкам": None, "Чоловікам": None, "Хлопчикам": None, "Дівчаткам": None},
            "Рюкзаки": {"Жінкам": "поліестер", "Чоловікам": "поліестер", "Хлопчикам": "поліестер",
                        "Дівчаткам": "поліестер"}
        }

        if self.type in valid_combinations:
            if self.category in valid_combinations[self.type]:
                allowed_materials = valid_combinations[self.type][self.category]
                if allowed_materials is None or self.material in allowed_materials:
                    return f"Вами обрано {self.type} від {self.brand} з матеріалу {self.material} по ціні {self.price}"

        return f"Нажаль {self.type} бренду {self.brand} по ціні {self.price} немає в наявності"


# Example usage:

if __name__ == '__main__':
    bag1 = Bag(brand="Gucci", color="Black", material="шкіра", type="Портмоне", category="Чоловікам", price=2000)
    print(bag1.validate())

    bag2 = Bag(brand="Adidas", color="Red", material="поліестер", type="Рюкзаки", category="Жінкам", price=100)
    print(bag2.validate())

    bag3 = Bag(brand="Prada", color="Blue", material="екошкіра", type="Косметички", category="Жінкам", price=150)
    print(bag3.validate())
