class ShoeModel:
    def __init__(self, type, view: str, color: str, price: int, manufacturer: str, size: int) -> None:
        self.type = type
        self.view = view
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size