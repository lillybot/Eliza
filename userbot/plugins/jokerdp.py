#made by @the_avengers_leader/if you erase this lines you are gay

import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRING = [

  "joker-hd-wallpapers-1080p",

  "dark-knight-joker-wallpaper",

  "joker-why-so-serious-wallpaper",

  "iron-man-wallpaper-1920x1080",

  
  
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="jokerdp ?(.*)"))

async def main(event):

    await event.edit("**Starting joker Profile Pic's...\n\nDone !!! Check Your DP.**")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60) #Edit this to your required needs
