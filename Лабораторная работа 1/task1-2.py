# TODO Найдите количество книг, которое можно разместить на дискете
storage=(1.44*1024)*1024
pages=100
lines=50
symbols=25
needed_space=round(storage/(((symbols*4)*lines)*pages),0)
needed_space = int(needed_space)
print("Количество книг, помещающихся на дискету:",needed_space )