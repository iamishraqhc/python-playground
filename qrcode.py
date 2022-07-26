import pyqrcode
import png
from pyqrcode import QRCode

# String representing QRCode
s = "https://instagram.com/codewithishraq"

# Generate QRCode
url = pyqrcode.create(s)

# Create and save svg file named 'qr.svg'
url.svg("qr.svg", scale = 8)

# Create and save the png file named 'qr.png'
url.png("qr.png", scale = 6)

url = pyqrcode.create(s)

s2 = "https://tiktok.com/@codewithishraq"
s3 = "https://youtube.com/codewithishraq"

url2 = pyqrcode.create(s2)
url3 = pyqrcode.create(s3)

url2.svg("qr2.svg", scale=8)
url3.svg("qr3.svg", scale=8)
         
url2.png("qr2.png", scale=6)
url3.png("qr3.png", scale=6)
