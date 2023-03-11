from  pytest import fixture

@fixture()
def answer():
    return 42

@fixture()
def new_answer(answer):
    return 42 + 1
