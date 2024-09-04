from elevator import Housing


def test_1Fにエレベーターがいて1Fホールの上ボタンを押す():
  # arrange 準備
  housing = Housing()
  elevator = housing.elevator
  first_floor = housing.get_floor(1)

  # act 実行
  first_floor.button.press()

  # assert 検証
  assert elevator.door.is_open() == True


def test_1Fにエレベーターがいてドアが閉まっている():
  # arrange 準備
  housing = Housing()
  elevator = housing.elevator

  # act 実行

  # assert 検証
  assert elevator.door.is_open() == False
