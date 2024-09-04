# TODO:次はリファクタリング
class Housing:

  def __init__(self):
    self.elevator = Elevator()

  def get_floor(self, floor):
    return Floor(self)


class Elevator:

  def __init__(self):
    self.door = Door()


class Floor:

  def __init__(self, housing):
    self.button = Button(self)
    self.housing = housing


class Button:

  def __init__(self, floor):
    self.floor = floor

  def press(self):
    self.floor.housing.elevator.door.open = True


class Door:

  def __init__(self):
    self.open = False

  def is_open(self):
    return self.open
