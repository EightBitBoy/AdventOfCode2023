import playground

def inc(x):
  return x + 1

def test_answer():
  assert inc(4) == 5

def test_playground():
  assert playground.foo() == 2
