from PIL import Image
from operator import itemgetter

#im = Image.open("captcha.gif")
im = Image.open("1005_img.png")
im = im.convert("P")
his = im.histogram()

values = {}

for i in range(256):
  values[i] = his[i]

print('Цвет |'.center(8), 'кол-во пикселей'.center(18))
print(' -----|-------------------')
for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
  # print(j,k)
  print(str(j).rjust(4), ' | ', str(k).ljust(8) )
