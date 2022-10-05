# check Pillow version number

import PIL

standard = PIL.open('../standard.pnd')

print(standard.format)

print(standard.size)

print(standard.mode)

# show the image

standard.show()