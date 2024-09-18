from elevator import Housing, Floor, Button, Car


def test_1Fにエレベーターがいて1Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car

  # act 実行
  button = Button(housing.get_floor(1))
  button.press()

  # assert 検証
  assert car.is_open() == True


def test_1Fにエレベーターがいてドアが閉まっている():
  # arrange 準備
  housing = Housing()
  car = housing.car

  # act 実行

  # assert 検証
  assert_指定した階でドアが閉まっている(floor=housing.get_floor(1), car=car)


def test_2Fにエレベーターがいて1Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car
  car.move_to_floor(housing.get_floor(2))
  first_floor = housing.get_floor(1)

  # act 実行
  button = Button(first_floor)
  button.press()

  # assert 検証
  assert_指定した階でドアが開いている(floor=first_floor, car=car)


def test_1Fにエレベーターがいて2Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car
  second_floor = housing.get_floor(2)

  # act 実行
  button = Button(second_floor)
  button.press()

  # assert 検証
  assert_指定した階でドアが開いている(floor=second_floor, car=car)
  # assert_エレベーターの状態("2-開-停止", car)


def assert_指定した階でドアが開いている(floor: Floor, car):
  assert car.current_floor == floor
  assert car.is_open() == True


def assert_指定した階でドアが閉まっている(floor: Floor, car: Car):
  assert car.current_floor == floor
  assert car.is_open() == False
