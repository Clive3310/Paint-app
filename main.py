import pygame as pg


pg.init()
font = pg.font.SysFont('roboto', 22)
WIDTH, HEIGHT = 410, 505

class UI:

    def __init__(self) -> None:
        self.ui = pg.surface.Surface((400, 90))
        self.ui.fill((100, 100, 100))
        
        self.bt = pg.draw.rect(self.ui, (151, 230, 0), (5, 25, 60, 60))
        text = font.render('BRUSH', True, (0, 0, 0))
        self.ui.blit(text, (8, 49))
        self.pt = pg.draw.rect(self.ui, (151, 230, 0), (70, 25, 60, 60))
        text = font.render('PENCIL', True, (0, 0, 0))
        self.ui.blit(text, (72, 49))

        self.brush_butt = pg.rect.Rect(self.bt.x + 5, self.bt.y + 5, self.bt.width, self.bt.height)
        self.pencil_butt = pg.rect.Rect(self.pt.x + 5, self.pt.y + 5, self.pt.width, self.pt.height)

        self.butts = {"BRUSH": self.brush_butt, "PENCIL": self.pencil_butt}
        self.selected_butt = "BRUSH"

        self.s4 = pg.draw.rect(self.ui, (151, 230, 0), (140, 21, 20, 20))
        self.size_butt_4 = pg.rect.Rect(self.s4.x + 5, self.s4.y + 5, self.s4.width, self.s4.height)
        text = font.render('4', True, (0, 0, 0))
        self.ui.blit(text, (146, 25))
        self.s6 = pg.draw.rect(self.ui, (151, 230, 0), (140, 46, 20, 20))
        self.size_butt_6 = pg.rect.Rect(self.s6.x + 5, self.s6.y + 5, self.s6.width, self.s6.height)
        text = font.render('6', True, (0, 0, 0))
        self.ui.blit(text, (146, 50))
        self.s8 = pg.draw.rect(self.ui, (151, 230, 0), (140, 71, 20, 20))
        self.size_butt_8 = pg.rect.Rect(self.s8.x + 5, self.s8.y + 5, self.s8.width, self.s8.height)
        text = font.render('8', True, (0, 0, 0))
        self.ui.blit(text, (146, 75))

        self.size_butts = {4: self.size_butt_4, 6: self.size_butt_6, 8: self.size_butt_8}
        self.selected_size = 6

    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.ui, (5, 5))
        text = font.render(f'Selected tool ({self.selected_size}): {self.selected_butt}', True, (0, 0, 0))
        screen.blit(text, (120, 11))

    def handle_event(self, event):
        for key, butt in self.butts.items():
            if butt.collidepoint(event.pos):
                self.selected_butt = key
            
        for key, butt in self.size_butts.items():
            if butt.collidepoint(event.pos):
                self.selected_size = key
        
        return self.selected_butt, self.selected_size


class Canvas:

    def __init__(self) -> None:
        self.c = pg.surface.Surface((400, 400))
        self.c.fill((255, 255, 255))

        self.selected_tool = "BRUSH"
        self.radius = 4

        self.pos = pg.rect.Rect(5, 100, 400, 400)
    
    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.c, (5, 100))

    def handle_event(self, event, tool, size):
        pos = event.pos
        self.selected_tool = tool
        self.radius = size

        if self.pos.collidepoint(pos):
            self.draw((pos[0] - 5, pos[1] - 100))

    def draw(self, pos):
        if self.selected_tool == "BRUSH":
            pg.draw.rect(self.c, (255, 0, 0), (pos[0] - self.radius // 2, pos[1] - self.radius // 2, self.radius, self.radius), 0)
        elif self.selected_tool == "PENCIL":
            pg.draw.rect(self.c, (0, 0, 0), (pos[0] - self.radius // 2, pos[1] - self.radius // 2, self.radius, self.radius), 0)


class Main_window:

    def __init__(self, ui: UI, canvas: Canvas) -> None:
        self.ui = ui
        self.canvas = canvas
    
    def mainloop(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
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
                    tool, size = ui.handle_event(event)
                    canvas.handle_event(event, tool, size)
            
            clock.tick(60)

            self.ui.be_drawn(screen)
            self.canvas.be_drawn(screen)

            pg.display.flip()


if __name__ == '__main__':
    ui = UI()
    canvas = Canvas()
    main_window = Main_window(ui, canvas)
    main_window.mainloop()


# TODO : Make color board. Make color changing. ?Make undo and redo?