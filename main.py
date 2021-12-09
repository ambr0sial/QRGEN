# by CColdFox / waw
# https://github.com/CColdFox/QRGEN
# big thanks to billythegoat356 for his Pystyle project, check him out: https://github.com/billythegoat356

import qrcode
import time
from os import listdir, remove, mkdir
from os.path import isdir, isfile
from pystyle import Anime, Colors, Colorate, System, Center, Write

banner = r"""
█▀▀▀▀▀█ ███ ▀▄▀▀█ █▀▀▀▀▀█
█ ███ █ █▄▀█ ▄▀ ▄ █ ███ █
█ ▀▀▀ █ ▄  ▄▄ ▀▀█ █ ▀▀▀ █
▀▀▀▀▀▀▀ ▀▄▀ █ █ █ ▀▀▀▀▀▀▀
▀█  ██▀  ▄▄▀██▄▄▄  ▀▄█▀█▀
 ▄███ ▀██ ▄█ ▀▄▀▀▀▀█▀▀█▄ 
█▀█▄▄▄▀▄▀▄▀█ █▄█ █▀▀▄▀▀█▀
  ▄▄▀▀▀▀▄ █▀█▀▄▀█▄ ██▀█▄ 
▀▀▀▀ ▀▀▀█▄ █▀ ▄ █▀▀▀█▀▀  
█▀▀▀▀▀█ ▄ █▀▄▀█ █ ▀ █▄▄ ▄
█ ███ █ ▀ █ ▀ ▄▄▀███▀▀█▄▄
█ ▀▀▀ █ ▄▀▄█▄ ▀ ▀██▄▄█▄█ 
▀▀▀▀▀▀▀ ▀   ▀  ▀  ▀   ▀▀▀"""

ascii_art = r"""

 ___________   _____                           _             
|  _  | ___ \ |  __ \                         | |            
| | | | |_/ / | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | |    /  | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
\ \/' / |\ \  | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \_/\_\_| \_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|"""[1:]              

def init():
    if not isdir('codes'):
        mkdir('codes')
    System.Clear()
    System.Size(160, 50)
    System.Title("QR Generator")
    Anime.Fade(text=Center.Center(banner), color=Colors.white_to_green, mode=Colorate.Vertical, enter=True)

def main():
    global qr_url
    global qr_name
    System.Clear()
    print('\n'*2)
    print(Colorate.Diagonal(color=Colors.white_to_green, text=Center.XCenter(ascii_art)))
    print('\n'*3)
    qr_url = Write.Input(text="Enter the link that will be opened when the QR Code will be scanned > ", color=Colors.white_to_green, interval=0.005)
    print()
    qr_name = Write.Input(text="Enter the name so the program can save the code with a custom name > ", color=Colors.white_to_green, interval=0.005)
    print()
    img = qrcode.make(qr_url)
    img.save('codes/{}.jpg'.format(qr_name))
    Write.Print(text="QR Code successfully generated & saved in [./codes]!", color=Colors.white_to_green, interval=0.005)
    print()
    time.sleep(3)

if __name__ == '__main__':
    init()
    while True:
        main()