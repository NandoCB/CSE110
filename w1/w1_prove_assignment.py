import random

print('Favorite Color')

color = input('Please type your favorite color: ')

print(f'Your favorite color is: \n {color}')

print('Wait! Do you want to know curious facts about some colors?')
fact = input('Please type [yes] or [no]: ')

if fact == ('yes'):
  colors = (['Orange', 'Blue', 'Red', 'Green'])
  colorsrandomizer = random.choice(colors)
  print (f'Did you know! \n {colorsrandomizer}')

else: fact == ('no')
exit('OK, thank you!')

orange = """One of the greatest curiosities of this color is its name... And it is that orange was known in Europe\n
as reddish yellow until the 16th century. This changed with the arrival of orange trees from Asia, 300 years after\n
their arrival, this hue adopted the name of the fruit."""

blue =  """In many parts of the world, the color blue represents freedom, loyalty, harmony, truth and seriousness.\n
Likewise, it is associated with physical energy and sport. Also to masculinity, modernism and technological\n
development."""

red = """Red is the color attributed to different emotions. We associate it with love and passion,\n
for example, but also with shyness or anger. It makes sense if we realize that any of the above emotions\n
can cause the blood to rise to the head and our face to adopt this hue."""

green = """The color of the fresh, the immature and the jovial\n
Green is the symbol of nature. It represents all its extensive and varied vegetation and is a very primitive\n
universal association, alien to cultures and religions. Green is also associated with life, health, hope and the\n
environment."""

if colorsrandomizer == ('Orange'):
  print(orange)

if colorsrandomizer == ('Blue'):
  print(blue)

if colorsrandomizer == ('Red'):
  print(red)

if colorsrandomizer == ('Green'):
  print(green)