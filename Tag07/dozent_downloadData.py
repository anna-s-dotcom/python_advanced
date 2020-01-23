# https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png

import requests

img = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')

# print(img.content)
# file = open('goog.png', 'wb')
# file.write(img.content)
# file.close()

open('goog1.png', 'wb').write(img.content)
