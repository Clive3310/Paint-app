import pygame as pg


pg.init()
font = pg.font.SysFont('roboto', 22)
WIDTH, HEIGHT = 410, 505

class UI:

    def __init__(self) -> None:
        self.ui = pg.surface.Surface((400, 90))
        self.ui.fill((100, 100, 100))
        
        self.brush_butt = pg.draw.rect(self.ui, (151, 230, 0), (5, 25, 60, 60))
        text = font.render('BRUSH', True, (0, 0, 0))
        self.ui.blit(text, (8, 49))
        self.pencil_butt = pg.draw.rect(self.ui, (151, 230, 0), (70, 25, 60, 60))
        text = font.render('PENCIL', True, (0, 0, 0))
        self.ui.blit(text, (72, 49))

        self.butts = {"BRUSH": self.brush_butt, "PENCIL": self.pencil_butt}
        self.selected_butt = "BRUSH"

    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.ui, (5, 5))
        text = font.render(f'Selected tool: {self.selected_butt}', True, (0, 0, 0))
        screen.blit(text, (120, 11))

    def handle_event(self, event):
        for key, butt in self.butts.items():
            if butt.collidepoint(event.pos):
                self.selected_butt = key
        
        return self.selected_butt


class Canvas:

    def __init__(self) -> None:
        self.c = pg.surface.Surface((400, 400))
        self.c.fill((255, 255, 255))

        self.selected_tool = "BRUSH"

        self.pos = pg.rect.Rect(5, 100, 400, 400)
    
    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.c, (5, 100))

    def handle_event(self, event, tool):
        pos = event.pos
        self.selected_tool = tool

        if self.pos.collidepoint(pos):
            self.draw((pos[0] - 5, pos[1] - 100), self.selected_tool)

    def draw(self, pos, tool):
        if tool == "BRUSH":
            pg.draw.rect(self.c, (0, 0, 0), (pos[0] - 3, pos[1] - 3, 6, 6), 0)
        elif tool == "PENCIL":
            pg.draw.rect(self.c, (255, 0, 0), (pos[0] - 3, pos[1] - 3, 6, 6), 0)


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
                    tool = ui.handle_event(event)
                    canvas.handle_event(event, tool)
            
            clock.tick(60)

            self.ui.be_drawn(screen)
            self.canvas.be_drawn(screen)

            pg.display.flip()


if __name__ == '__main__':
    ui = UI()
    canvas = Canvas()
    main_window = Main_window(ui, canvas)
    main_window.mainloop()
