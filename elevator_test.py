from elevator import Housing, Floor


def test_1Fにエレベーターがいて1Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car
  first_floor = housing.get_floor(1)

  # act 実行
  first_floor.button.press()

  # assert 検証
  assert car.is_open() == True


def test_1Fにエレベーターがいてドアが閉まっている():
  # arrange 準備
  housing = Housing()
  car = housing.car

  # act 実行

  # assert 検証
  assert car.is_open() == False
  assert car.current_floor == housing.get_floor(1)


def test_2Fにエレベーターがいて1Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car
  car.current_floor = 2
  first_floor = housing.get_floor(1)

  # act 実行
  first_floor.button.press()

  # assert 検証
  assert_呼んだ階でドアが開いている(呼んだ階=first_floor, car=car)


def assert_呼んだ階でドアが開いている(呼んだ階: Floor, car):
  assert car.current_floor == 呼んだ階
  assert car.is_open() == True


def test_1Fにエレベーターがいて2Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  car = housing.car
  car.current_floor = 1
  second_floor = housing.get_floor(2)

  # act 実行
  second_floor.button.press()

  # assert 検証
  assert_呼んだ階でドアが開いている(呼んだ階=second_floor, car=car)
