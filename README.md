# modded-darkreader

a modified dark reader extension to match with wallpaper colours

the extension is unpacked from firefox but it'll work on chromium browsers 

## what is modded:

background/index.js (CTRL + F and MOD1)

inject/index.js (CTRL + F and MOD2 MOD3 MOD4 MOD5)

basically i edited the colour filter matrix (used for speia and grayscale filters) per every wallpaper colour change

## how 2 install - browsers

chrome ppl:

https://github.com/web-scrobbler/web-scrobbler/wiki/Install-an-unpacked-extension

firefox ppl:

you need to install the developer edition of firefox first

when you're done, make your way over to the `about:addons` page, click that gear icon and press load addon from file (zip darkreader folder!)

## how 2 install - server

the server is located in the "server" folder

you need to:

- get python & pip
- pip install simple-websocket-server 
- pip install pywal
- pip install haishoku
- python main.py (you might want to make it run on startup)
- smile that your browser is pretty

ports that are used:

9483 - websocket

9484 - tcp port for the server to receive the wallpaper location

idk how you guys configure your wallpapers so i've decided that you'd need to manually implement it

-> get wallpaper location 

-> connect to tcp socket 9484 on 127.0.0.1 

-> send both color index & wallpaper location on disk

   - color indexs start at 0 to 15
   
   - an example of what to send to the tcp socket:

        color index ; wallpaper location

        0;/home/me/wallpaper.png

        
-> **close socket**

-> server gets the wallpaper location and inputs it in pywal

-> pywal outputs hex colour and brodcasts to connected browsers


**actually just use wraper.py to do it all for you**

wraper.py positional arguments:

{color index} {wallpapr location}
