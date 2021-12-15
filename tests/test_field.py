from models.field import Field, Type

def test_field():
    bomb_field = Field(True, 6, Type.bomb)
    empty_field = Field (False, 3, Type.empty)

    print(bomb_field)
    print(empty_field)