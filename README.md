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
- python main.py (you might want to make it run on startup)
- smile that your browser is pretty

ports that are used:

9483 - websocket

9484 - tcp port for the server to update the colour 

only connecting to the socket is enough to trigger an colour update to the browser, you don't need to send anything to the tcp socket

the return_color.py script currently works on linux systems w pywal installed

you can freely modify the script for your operating system as long it returns a hex string!
