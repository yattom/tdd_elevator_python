class Housing:

  def __init__(self):
    self.floors = {}
    self.car = Car(self)

  def get_floor(self, floor_number: int):
    if floor_number not in self.floors.keys():
      self.floors[floor_number] = Floor(self, floor_number)
    return self.floors[floor_number]


class Car:

  def __init__(self, housing: Housing):
    self.current_floor = housing.get_floor(1)
    self._open = False

  def is_open(self):
    return self._open

  def open(self):
    self._open = True

  def move_to_floor(self, floor: 'Floor'):
    self.current_floor = floor


class Floor:

  def __init__(self, housing: Housing, floor_number: int):
    self.housing = housing
    self.floor_number = floor_number


class Button:

  def __init__(self, floor: Floor):
    self.floor = floor

  def press(self):
    self.get_car().move_to_floor(self.floor)
    self.get_car().open()

  def get_car(self):
    return self.floor.housing.car
