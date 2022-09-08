import pyqrcode 
import png
from pyqrcode import QRCode
from pystyle import Colorate, Colors, Write, Add, Center
s = input(Colorate.Horizontal(Colors.blue_to_red,"Input the link to create QRCode > "))

url = pyqrcode.create(s)

url.svg("QRCode.svg", scale = 8)
url.png("QRCode.png", scale = 6)
