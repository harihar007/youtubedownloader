import webbrowser
a=input("Enter url:")
b=a.split(".")
b.insert(2,'cp')
c=(','.join(b))
c=c.replace(',','.')
d=c.replace('youtube.cp','youtubecp')
webbrowser.open(d)
