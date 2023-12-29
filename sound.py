import pygame as pg


class Sound:
    def __init__(self):
        pg.mixer.init()

    def load_music(self, path):
        self.path = path
        self.theme = pg.mixer.music.load(self.path)

    def set_volume(self, volume):
        pg.mixer.music.set_volume(volume)

    def play_theme(self):
        pg.mixer.music.play(-1)  # -1 means the music loops indefinitely
