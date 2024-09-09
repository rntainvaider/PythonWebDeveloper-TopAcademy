from Controller.controller import ShoeController
from View.view import ShoeView

controller = ShoeController("asd", "asd", "asd", 123123, "asd", 32)
view = ShoeView()

print(view.shoe_details(controller))