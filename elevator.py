# TODO: 次回はリファクタリングから 
class Housing:

  def __init__(self):
    self.car = Elevator()

  def get_floor(self, floor):
    return Floor(self, floor)


class Elevator:

  def __init__(self):
    self.current_floor = 1
    self.open = False

  def is_open(self):
    return self.open


class Floor:

  def __init__(self, housing, floor):
    self.button = Button(self)
    self.housing = housing
    self.floor = floor


class Button:

  def __init__(self, floor):
    self.floor = floor

  def press(self):
    self.floor.housing.car.current_floor = self.floor.floor
    self.floor.housing.car.open = True
