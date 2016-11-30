import pyglet
import math

window = pyglet.window.Window()

obrazek = pyglet.image.load("had.png")
obrazek2 = pyglet.image.load("had2.png")

had = pyglet.sprite.Sprite(obrazek)

def zpracuj_text(text):
    had.x = 150

def tik(t):
    had.x = had.x + t*20


def vykresli():
    window.clear()
    had.draw()
    if had.x > window.width:
        had.x = 0

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    if tlacitko == 4:
        had.rotation += 180


window.push_handlers(
                on_text = zpracuj_text,
                on_draw = vykresli,
                on_mouse_press = klik
                    )

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 1)

pyglet.app.run()

print("hotovo")
