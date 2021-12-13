from models.field import Field, Type

bomb_field = Field(True, 6, Type.bomb)
empty_field = Field (False, 3, Type.empty)

print(bomb_field.__repr__)
print(empty_field.__repr__)