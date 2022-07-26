import pytube

link = 'https://youtu.be/eChpPgJxeIg'
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print('downloaded', link)