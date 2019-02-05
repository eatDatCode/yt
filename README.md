# yt
CLI program to grab top 20 results from your favorite terminal, and use the link for use of youtube-dl or mpv or other such CLI programs.

# Things you should know about two great CLI tools before using this program:
1) youtube-dl (https://youtube-dl.org/)
2) mpv (https://mpv.io/)

youtube-dl is a tool that lets you grab videos and audios from a lot of sites, espcially from youtube from terminal

mpv is fork of mplayer2 whic features a CLI option for streaming online videos or local files from terminal. It uses youtube-dl.

So if you use "yt" to grab all the links from youtube without going to a browser and your day is all set.

Get the link from youtube using "yt" and download the video using "youtube-dl"

Or stream online using mpv

$ mpv  https://www.youtube.com/watch?v=Vxie38_sde9

$ youtube-dl  -f  18  https://www.youtube.com/watch?v=Vxie38_sde9

# Description:
  This program uses requests library to scraps first page results from youtube on any search query and gives you output
  as top 20 titles || duration || link as results.
  
# Requirements:
 1) python3 or higher

# How to setup:

Pretty simple! Clone the repository 

$ git  clone  https://www.github.com/eatDatCode/yt.git

$ cd  yt

$ sudo pip install -r requirements.txt (Please make sure your pip is configured for python3 or higher)

$ chmod  a+x  yt.py

$ mv  ./yt.py  yt

$ sudo  mv  yt  /usr/bin/

That's all.

Now open your terminal :

$ yt  (type here as you would type on the search box of youtube)

Adios.

# Some options to use: 
Use the last word of your query as an option to get customized results from youtube.
options:

  $ yt  channel name channel
  
  (This will give you option to choose channel from the list and after an option is choosen will be given at 30 playlist from that channel)

# some useful tips about mpv and youtube-dl
i) $ youtube-dl -F link
(to know the formats available for a certain video , get the format id, such m4m format has format id 140 for audios only)

ii) $ mpv --ytdl-format (format from youtube-dl) link
(This will help you to stream videos in your chosen resolution and you can even stream only audio from youtube)
e.g: $ mpv --ytdl-format 140 link
