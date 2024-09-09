from Controller.controller import ShoeController

class ShoeView:
    def shoe_details(self, shoe):
        print(f"Тип обуви {shoe.type}")
        print(f"Вип обуви {shoe.view}")
        print(f"Цвет {shoe.color}")
        print(f"Цена {shoe.price}")
        print(f"Производитель {shoe.manufacturer}")
        print(f"Размер {shoe.size}")