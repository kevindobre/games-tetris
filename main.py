from setting import *
from tetris import Tetris, text
from sound import *
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)
        self.text = text(self)
        self.sound = Sound()  # Initialize the Sound class here
        self.sound.load_music('(Korobeiniki).mp3')  # Load the music file
        self.sound.set_volume(0.3)  # Set the volume

    # ... (other methods remain the same)

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BG_COLOR)  # Removed color= from fill
        self.screen.fill(FIELD_COLOR, rect=(0, 0, *FIELD_RES))  # Removed color= from fill
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()

    def check_event(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):  # Changed pg.KEY_ESCAPE to pg.K_ESCAPE
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True

    def run(self):
        self.sound.play_theme()  # Play the theme music
        while True:
            self.check_event()
            self.update()
            self.draw()

    # ... (rest of your App class remains the same)


if __name__ == '__main__':
    app = App()  # Create an instance of the App class
    app.run()
