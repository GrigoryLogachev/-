 # TODO Найдите количество книг, которое можно разместить на дискете

disc = 1.44
pages = 100
lines = 50
simbols = 25
volume = 4

one_book = volume * simbols * lines * pages

disc_bait = disc * 1024 * 1024

books = round(disc_bait / one_book)


print("Количество книг, помещающихся на дискету:", books)
