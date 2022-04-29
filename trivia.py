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
def Button(x,y,w,h,text,color,action=None):
    # pygame.font.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    X = 0
    WIN.blit(FONT.render(text,False,(255,255,255)),(x-FONT.render(text,False,(255,255,255)).get_width()//2,y-FONT.render(text,False,(255,255,255)).get_height()//2))
    pygame.draw.rect(WIN, color, (x-w/2,y-h/2,w,h),1,50)
    if x+w/2 > mouse[0] > x-w/2 and y+h/2 > mouse[1] > y-h/2:   
        pygame.draw.rect(WIN, (color[0]-20,color[1]-20,color[2]-20), (x-w/2,y-h/2,w,h),3,50)
        if click[0] == 1 and action != None:
            action()
        

answers = [["6","4","5","7"],["Fips & Milo","Tom & Jerry","Charlie & Loki","Tim & Jerry"],["3","6","4","5"],["Schwarz","Weiß","Braun","Gelb"],["Casna","Maiko","Backardi","Meska"],["streicheln","füttern","Hasen verfolgen",""]]



q = 0
def pr():
    print("Ji")
while True:
    draw_text(questions[q], FONT, (255,255,255), WIN, WIDTH/2, HEIGHT/2)
    Button(WIDTH/6*2,HEIGHT/8*6,WIDTH/4,HEIGHT/8,answers[q][0],(20,255,20),pr)
    Button(WIDTH/6*4,HEIGHT/8*6,WIDTH/4,HEIGHT/8,answers[q][1],(20,255,20),pr)
    Button(WIDTH/6*2,HEIGHT/8*7.2,WIDTH/4,HEIGHT/8,answers[q][2],(20,255,20),pr)
    Button(WIDTH/6*4,HEIGHT/8*7.2,WIDTH/4,HEIGHT/8,answers[q][3],(20,255,20),pr)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
    WIN.fill((30,30,30))