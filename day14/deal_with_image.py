
from PIL import Image, ImageFilter
image = Image.open('./code.png')
image.format, image.size, image.mode
('PNG', (500, 750), 'RGB')
image.filter(ImageFilter.CONTOUR).show()