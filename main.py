import pygame as pg


pg.init()
font = pg.font.SysFont('roboto', 22)
WIDTH, HEIGHT = 410, 505

class UI:

    def __init__(self) -> None:
        self.ui = pg.surface.Surface((400, 90))
        self.ui.fill((100, 100, 100))

        self.clear = False

        self.ct = pg.draw.rect(self.ui, (151, 230, 0), (5, 4, 60, 18))
        self.clear_butt = pg.rect.Rect(self.ct.x + 5, self.ct.y + 5, self.ct.width, self.ct.height)
        text = font.render('CLEAR', True, (0, 0, 0))
        self.ui.blit(text, (8, 7))
        
        self.bt = pg.draw.rect(self.ui, (151, 230, 0), (5, 25, 60, 60))
        self.brush_butt = pg.rect.Rect(self.bt.x + 5, self.bt.y + 5, self.bt.width, self.bt.height)
        text = font.render('BRUSH', True, (0, 0, 0))
        self.ui.blit(text, (8, 49))
        self.pt = pg.draw.rect(self.ui, (151, 230, 0), (70, 25, 60, 60))
        self.pencil_butt = pg.rect.Rect(self.pt.x + 5, self.pt.y + 5, self.pt.width, self.pt.height)
        text = font.render('PENCIL', True, (0, 0, 0))
        self.ui.blit(text, (72, 49))

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

        self.red_b = pg.draw.rect(self.ui, (255, 0, 0), (190, 21, 20, 20))
        self.red_b = pg.rect.Rect(self.red_b.x + 5, self.red_b.y + 5, self.red_b.width, self.red_b.height)
        self.green_b = pg.draw.rect(self.ui, (0, 255, 0), (190, 46, 20, 20))
        self.green_b = pg.rect.Rect(self.green_b.x + 5, self.green_b.y + 5, self.green_b.width, self.green_b.height)
        self.blue_b = pg.draw.rect(self.ui, (0, 0, 255), (190, 71, 20, 20))
        self.blue_b = pg.rect.Rect(self.blue_b.x + 5, self.blue_b.y + 5, self.blue_b.width, self.blue_b.height)
        self.lightsalmon_b = pg.draw.rect(self.ui, (255, 160, 122), (215, 21, 20, 20))
        self.lightsalmon_b = pg.rect.Rect(self.lightsalmon_b.x + 5, self.lightsalmon_b.y + 5, self.lightsalmon_b.width, self.lightsalmon_b.height)
        self.hotpink_b = pg.draw.rect(self.ui, (255, 105, 180), (215, 46, 20, 20))
        self.hotpink_b = pg.rect.Rect(self.hotpink_b.x + 5, self.hotpink_b.y + 5, self.hotpink_b.width, self.hotpink_b.height)
        self.orange_b = pg.draw.rect(self.ui, (255, 165, 0), (215, 71, 20, 20))
        self.orange_b = pg.rect.Rect(self.orange_b.x + 5, self.orange_b.y + 5, self.orange_b.width, self.orange_b.height)
        self.yellow_b = pg.draw.rect(self.ui, (255, 255, 0), (240, 21, 20, 20))
        self.yellow_b = pg.rect.Rect(self.yellow_b.x + 5, self.yellow_b.y + 5, self.yellow_b.width, self.yellow_b.height)
        self.indigo_b = pg.draw.rect(self.ui, (75, 0, 130), (240, 46, 20, 20))
        self.indigo_b = pg.rect.Rect(self.indigo_b.x + 5, self.indigo_b.y + 5, self.indigo_b.width, self.indigo_b.height)
        self.cyan_b = pg.draw.rect(self.ui, (0, 255, 255), (240, 71, 20, 20))
        self.black_b = pg.draw.rect(self.ui, (0, 0, 0), (265, 46, 20, 20))
        self.black_b = pg.rect.Rect(self.black_b.x + 5, self.black_b.y + 5, self.black_b.width, self.black_b.height)
        self.cyan_b = pg.rect.Rect(self.cyan_b.x + 5, self.cyan_b.y + 5, self.cyan_b.width, self.cyan_b.height)
        self.white_b = pg.draw.rect(self.ui, (255, 255, 255), (265, 71, 20, 20))
        self.white_b = pg.rect.Rect(self.white_b.x + 5, self.white_b.y + 5, self.white_b.width, self.white_b.height)
        
        self.color_butts = {(255, 0, 0): self.red_b, (0, 255, 0): self.green_b, (0, 0, 255): self.blue_b, 
                            (255, 160, 122): self.lightsalmon_b, (255, 105, 180): self.hotpink_b, (255, 165, 0): self.orange_b,
                            (255, 255, 0): self.yellow_b, (75, 0, 130): self.indigo_b, (0, 255, 255): self.cyan_b,
                            (0, 0, 0): self.black_b, (255, 255, 255): self.white_b}
        self.color_map = {(255, 0, 0): 'RED', (0, 255, 0): 'GREEN', (0, 0, 255): 'BLUE', 
                            (255, 160, 122): 'LIGHT SALMON', (255, 105, 180): 'HOT PINK', (255, 165, 0): 'ORANGE',
                            (255, 255, 0): 'YELLOW', (75, 0, 130): 'INDIGO', (0, 255, 255): 'CYAN',
                            (0, 0, 0): 'BLACK', (255, 255, 255): 'WHITE'}
        self.selected_color = (255, 0, 0)
    
    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.ui, (5, 5))
        text = font.render(f'Selected tool ({self.selected_size}): {self.selected_butt}', True, (0, 0, 0))
        screen.blit(text, (120, 11))
        text1 = font.render(f'Selected color: ', True, (0, 0, 0))
        screen.blit(text1, (290, 30))
        text = font.render(self.color_map[self.selected_color], True, (0, 0, 0))
        screen.blit(text, (290 + text1.get_width() // 2 - text.get_width() // 2, 50))

    def handle_event(self, event):
        for key, butt in self.butts.items():
            if butt.collidepoint(event.pos):
                self.selected_butt = key
            
        for key, butt in self.size_butts.items():
            if butt.collidepoint(event.pos):
                self.selected_size = key
        
        if self.clear_butt.collidepoint(event.pos):
            self.clear = True
        
        for key, color_b in self.color_butts.items():
            if color_b.collidepoint(event.pos):
                self.selected_color = key
        
        return self.selected_butt, self.selected_size, self.selected_color


class Canvas:

    def __init__(self) -> None:
        self.c = pg.surface.Surface((400, 400))
        self.c.fill((255, 255, 255))

        self.selected_tool = "BRUSH"
        self.selected_color = "red"
        self.radius = 4

        self.pos = pg.rect.Rect(5, 100, 400, 400)
    
    def be_drawn(self, screen: pg.surface.Surface):
        screen.blit(self.c, (5, 100))

    def handle_event(self, event, tool, size, color):
        pos = event.pos
        self.selected_tool = tool
        self.radius = size
        self.selected_color = color

        if self.pos.collidepoint(pos):
            self.draw((pos[0] - 5, pos[1] - 100))

    def draw(self, pos):
        if self.selected_tool == "BRUSH":
            pg.draw.circle(self.c, self.selected_color, pos, self.radius, 0)
        elif self.selected_tool == "PENCIL":
            pg.draw.circle(self.c, (0, 0, 0), pos, self.radius // 2, 0)

    def clear(self):
        self.c.fill((255, 255, 255))


class Main_window:

    def __init__(self, ui: UI, canvas: Canvas) -> None:
        self.ui = ui
        self.canvas = canvas
    
    def mainloop(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Paint-app')
        icon = pg.image.load('res/icon.jpg')
        pg.display.set_icon(icon)

        screen.fill((30, 30, 30))

        tool, size = self.ui.selected_butt, self.ui.selected_size

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            
            if pg.mouse.get_pressed()[0]:
                tool, size, color = self.ui.handle_event(pg.event.EventType(pg.MOUSEBUTTONDOWN, {'pos': pg.mouse.get_pos()}))
                canvas.handle_event(pg.event.EventType(pg.MOUSEBUTTONDOWN, {'pos': pg.mouse.get_pos()}), tool, size, color)
                if self.ui.clear:
                    self.canvas.clear()
                    self.ui.clear = False
            
            self.ui.be_drawn(screen)
            self.canvas.be_drawn(screen)

            pg.display.flip()


if __name__ == '__main__':
    ui = UI()
    canvas = Canvas()
    main_window = Main_window(ui, canvas)
    main_window.mainloop()


# TODO : Make color board. Make color changing. ?Make undo and redo?