import pygame as pg


pg.init()


class Main_window:

    def __init__(self, ui, canvas) -> None:
        self.ui = ui
        self.canvas = canvas
    
    def mainloop(self):
        screen = pg.display.set_mode((400, 400))
        pg.display.set_caption('Paint-app')
        icon = pg.image.load('res/icon.jpg')
        pg.display.set_icon(icon)
        clock = pg.time.Clock()

        screen.fill((30, 30, 30))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            clock.tick(60)

            self.ui.draw(screen)
            self.canvas.draw(screen)
            pg.display.update()
    

class UI:

    def __init__(self) -> None:
        self.ui = pg.surface.Surface((400, 100))
        self.ui.fill((0, 255, 0))
        pg.draw.rect(self.ui, (255, 255, 255), (10, 10, 80, 80))

    def draw(self, screen: pg.surface.Surface):
        screen.blit(self.ui, (0, 0))


class Canvas:

    def __init__(self) -> None:
        self.c = pg.surface.Surface((400, 300))
        self.c.fill((255, 255, 255))

    def draw(self, screen: pg.surface.Surface):
        screen.blit(self.c, (0, 100))


if __name__ == '__main__':
    ui = UI()
    canvas = Canvas()
    main_window = Main_window(ui, canvas)
    main_window.mainloop()
