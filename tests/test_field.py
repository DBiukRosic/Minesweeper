from models.field import Field, Type

is_bomb = Field()
is_not_bomb = Field ()
is_bomb.is_hidden = True
is_bomb.surrounding_bombs = 3
is_bomb.type = Type.bomb
is_not_bomb.is_hidden = False
is_not_bomb.surrounding_bombs = 1
is_not_bomb.type = Type.empty
print(is_bomb.is_hidden)