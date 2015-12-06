from PIL import Image, ImageChops

IMAGE = 'img_best/amazon.jpg'

INAME = IMAGE.split('.')[0]
IEXT = IMAGE.split('.')[1]

## load image
im = Image.open(IMAGE)

### box cut
width, height = im.size


print im.load()
print im.format
print im.mode
print im.size
print im.palette
print im.info





print "done"