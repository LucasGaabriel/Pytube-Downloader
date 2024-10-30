from pytubefix import YouTube

url = 'http://youtube.com/watch?v=2lAe1cqCOXo'

yt = YouTube(url)

print(yt.title)

# ys = yt.streams.get_highest_resolution()
# ys.download()