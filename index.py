""" from pytube import YouTube,Playlist
import os
import pathlib """

""" p=Playlist("https://www.youtube.com/playlist?list=PLMe25YnMPrGFdnCbTUTVxio6vjjw7erbM")
ruta=os.path.join(pathlib.Path(__file__).parent.absolute(),str(p.title))
if not os.path.exists(p.title):
      os.mkdir(p.title)
for video in p.videos:
      print(video.vid_info)
      video=video.streams.filter(only_audio=True).first()
      out_file=video.download(ruta)      
      base, ext = os.path.splitext(out_file)
      new_file = base + '.mp3'
      os.rename(out_file, new_file) """
""" yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.title=yt._title
yt=yt.streams.filter(only_audio=True).first()
out_file=yt.download()
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file) """