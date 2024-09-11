class Housing:

  def __init__(self):
    self.car = Elevator()

  def get_floor(self, floor):
    return Floor(self)


class Elevator:

  def __init__(self):
    self.current_floor = 1
    self.open = False

  def is_open(self):
    return self.open


class Floor:

  def __init__(self, housing):
    self.button = Button(self)
    self.housing = housing


class Button:

  def __init__(self, floor):
    self.floor = floor

  def press(self):
    self.floor.housing.car.current_floor = 1
    self.floor.housing.car.open = True
