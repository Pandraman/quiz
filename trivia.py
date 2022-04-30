import pygame,random


## trivia game
# get text
pygame.init()
FONT = pygame.font.SysFont('comicsans', 30)


# setup WIn
WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia")

# draw a question x on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x-textobj.get_width()/2, y-textobj.get_height()/2)
    surface.blit(textobj, (x-textobj.get_width()/2, y-textobj.get_height()/2))
tiere = ["Wie viele Tierarten hat die Jugendfarm?","wie heißen die Jugendfarmkatzen?","Wie viele Hühner leben auf der Jugendfarm?","Welche Farbe hat Maiko?","Welches Pferd hatte eine Regenbogenmähne?","Was darf man im Hasenstall machen?","Was essen Ziegen?","Was ist das Merkmal von Jerry?","Wo schlafen die Ziegen?","Welche Rasse ist Mesca?"]


questions = []
for i in tiere:
    questions.append(i)


class Button():
    def __init__(self, text, x, y, width, height, inactive_color, active_color, function=None, id=None, right=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.function = function
        self.clicked = False
        self.id = id
        self.a = 0
        self.right = right
    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(WIN, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1:
                
                if self.id == self.right:
                    self.a = 1
                    # print(self.a)
                else:
                    self.a = -1
                    # print(self.a)
        else:
            pygame.draw.rect(WIN, self.inactive_color, (self.x, self.y, self.width, self.height))
        draw_text(self.text, FONT, (255, 255, 255), WIN, self.x + self.width/2, self.y + self.height/2)
    


answers = [["6","4","5","7"],["Fips & Milo","Tom & Jerry","Charlie & Loki","Tim & Jerry"],["3","6","4","5"],["Schwarz","Weiß","Braun","Gelb"],["Casna","Maiko","Backardi","Meska"],["streicheln","füttern","Hasen verfolgen",""],["Gras","Heu","Stroh","Fleisch"]]
right = [0,1,3,0,0,0,]

q = 1
b1 = Button(answers[q][0], WIDTH/2-200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 0, right[q])
b2 = Button(answers[q][1], WIDTH/2-200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 1, right[q])
b3 = Button(answers[q][2], WIDTH/2+200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 2, right[q])
b4 = Button(answers[q][3], WIDTH/2+200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 3, right[q])


A = 0
Punkte = 0
C = pygame.time.Clock()
while True:
    C.tick(60)
    if Punkte > 0:Punkte -= .1
    A = 0
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()

    if b1.a == 1 or b2.a == 1 or b3.a == 1 or b4.a == 1:
        pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
        q += 1
        Punkte += 100
        b1 = Button(answers[q][0], WIDTH/2-200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 0, right[q])
        b2 = Button(answers[q][1], WIDTH/2-200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 1, right[q])
        b3 = Button(answers[q][2], WIDTH/2+200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 2, right[q])
        b4 = Button(answers[q][3], WIDTH/2+200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 3, right[q])
        b1.a = 0
        b2.a = 0
        b3.a = 0
        b4.a = 0
    if b1.a == -1 or b2.a == -1 or b3.a == -1 or b4.a == -1:
        pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
        q += 1
        b1 = Button(answers[q][0], WIDTH/2-200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 0, right[q])
        b2 = Button(answers[q][1], WIDTH/2-200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 1, right[q])
        b3 = Button(answers[q][2], WIDTH/2+200, HEIGHT/2+100, 200, 50, (0, 255, 0), (0, 0, 255), None, 2, right[q])
        b4 = Button(answers[q][3], WIDTH/2+200, HEIGHT/2-100, 200, 50, (0, 255, 0), (0, 0, 255), None, 3, right[q])
        b1.a = 0
        b2.a = 0
        b3.a = 0
        b4.a = 0
    draw_text("Punkte: " + str(int(Punkte)), FONT, (255, 255, 255), WIN, WIDTH/2, HEIGHT/8)
    draw_text(questions[q], FONT, (255,255,255), WIN, WIDTH/2, HEIGHT/2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
    WIN.fill((30,30,30))