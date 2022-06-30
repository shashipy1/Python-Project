import pyglet

vidPath = 'E:\\vid.go\\1.Valuable Resources.mp4'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()
 
 
@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(100, 100)
 
pyglet.app.run()