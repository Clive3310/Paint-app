import pygame as pg


pg.init()
font = pg.font.SysFont('roboto', 25)


class UI:

    def __init__(self) -> None:
        self.ui = pg.surface.Surface((400, 125))
        self.ui.fill((100, 100, 100))
        
        self.brush_butt = pg.draw.rect(self.ui, (151, 230, 0), (5, 35, 85, 85))
        text = font.render('BRUSH', True, (0, 0, 0))
        self.ui.blit(text, (17, 68))
        self.pencil_butt = pg.draw.rect(self.ui, (151, 230, 0), (95, 35, 85, 85))
        text = font.render('PENCIL', True, (0, 0, 0))
        self.ui.blit(text, (107, 68))

        self.butts = {"BRUSH": self.brush_butt, "PENCIL": self.pencil_butt}
        self.selected_butt = "BRUSH"

    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.ui, (5, 5))

    def handle_event(self, event):
        for key, butt in self.butts.items():
            if butt.collidepoint(event.pos):
                self.selected_butt = key


class Canvas:

    def __init__(self) -> None:
        self.c = pg.surface.Surface((400, 270))
        self.c.fill((255, 255, 255))

    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.c, (5, 135))

    def handle_event(self, event):
        pass


class Main_window:

    def __init__(self, ui: UI, canvas: Canvas) -> None:
        self.ui = ui
        self.canvas = canvas

        self.width, self.height = 410, 410
    
    def mainloop(self):
        screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Paint-app')
        icon = pg.image.load('res/icon.jpg')
        pg.display.set_icon(icon)
        clock = pg.time.Clock()

        screen.fill((30, 30, 30))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    ui.handle_event(event)
            
            clock.tick(60)

            self.ui.be_drawn(screen)
            text = font.render(f'Selected tool: {self.ui.selected_butt}', True, (0, 0, 0))
            screen.blit(text, ((self.width - text.get_width()) // 2, 12))
            self.canvas.be_drawn(screen)
            
            pg.display.flip()


if __name__ == '__main__':
    ui = UI()
    canvas = Canvas()
    main_window = Main_window(ui, canvas)
    main_window.mainloop()
