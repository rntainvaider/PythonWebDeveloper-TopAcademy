from Model.model import ShoeModel

class ShoeController(ShoeModel):
    def __init__(self, type: str, view: str, color: str, price: int, manufacturer: str, size: int) -> None:
        super().__init__(type, view, color, price, manufacturer, size)


    def create_shoe(self):
        return (self.type, self.view, self.color, self.price, self.manufacturer, self.size)
    