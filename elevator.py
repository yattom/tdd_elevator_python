# TODO: 次回はリファクタリングから
class Housing:

  def __init__(self):
    self.floors = {}
    self.car = Elevator(self)

  def get_floor(self, floor_number: int):
    if floor_number not in self.floors.keys():
      self.floors[floor_number] = Floor(self, floor_number)
    return self.floors[floor_number]


class Elevator:

  def __init__(self, housing):
    self.current_floor = housing.get_floor(1)
    self._open = False

  def is_open(self):
    return self._open

  def open(self):
    self._open = True

  def move_to_floor(self, floor):
    self.current_floor = floor


class Floor:

  def __init__(self, housing, floor):
    self.button = Button(self)
    self.housing = housing
    self.floor_number = floor


class Button:

  def __init__(self, floor):
    self.floor = floor

  def press(self):
    self.get_car().move_to_floor(self.floor)
    self.get_car().open()

  def get_car(self):
    return self.floor.housing.car
