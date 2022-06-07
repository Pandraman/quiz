
import pygame,random
def AddLB(LB,Name,P):
    v = len(LB)-1
    while P > LB[v][1] and v > 0:
        v -= 1
    if P < LB[v][1]:
        LB.insert(v+1,[Name,P])
    
    if P > LB[v][1]:
        LB.insert(v,[Name,P])
        LB.pop(len(LB)-1)
    while len(Scoreboard)-1>10:
        Scoreboard.pop()
    return LB
## trivia game
# get text
pygame.init()
FONT = pygame.font.Font('font.ttf', 20)


# setup WIn
WIDTH, HEIGHT = 1600,900
WIN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Trivia")

# draw a question x on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x-textobj.get_width()/2, y-textobj.get_height()/2)
    surface.blit(textobj, (x-textobj.get_width()/2, y-textobj.get_height()/2))

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
        self.b = 0
    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(WIN, self.active_color, (self.x, self.y, self.width, self.height),1,30)
            if click[0] == 1:
                
                if self.id == self.right:
                    self.a = 1
                    self.b = 1
                    # print(self.a)
                else:
                    self.a = -1
                    # print(self.a)
        else:
            pygame.draw.rect(WIN, self.inactive_color, (self.x, self.y, self.width, self.height),1,30)
        draw_text(self.text, FONT, (255, 255, 255), WIN, self.x + self.width/2, self.y + self.height/2)
    
import json
from q import A as QUESTIONS
n = []
r = random.randint(0,len(QUESTIONS)-1)




Scoreboard = [["",0],["",-1],["",-1],["",-1],["",-1],["",-1],["",-1],["",-1],["",-1],["",-1]]
q = 0
Name = ""
n = True
A = 0
Punkte = 0
C = pygame.time.Clock()
Played = False
L = False
PL = True
LGCHARS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"," ","-","_",".",",","?","!",":",";","(",")","[","]","{","}","/","\\","|","@","#","$","%","^","&","*","+","=","<",">","~","`","'"," ","ß"]
N = 8
TOA = 8

def gen_q(i,QUESTIONSS,j=None):
    i = random.randint(0,len(QUESTIONS)-1)
    b1 = Button(QUESTIONS[i][1][0], WIDTH/2-200, HEIGHT/2+100, 200, 50, (255, 208, 0), (0, 0, 255), None, 0, QUESTIONS[i][2])
    b2 = Button(QUESTIONS[i][1][1], WIDTH/2-200, HEIGHT/2-100, 200, 50, (255, 16, 0), (0, 0, 255), None, 1, QUESTIONS[i][2])
    b3 = Button(QUESTIONS[i][1][2],WIDTH/2+200, HEIGHT/2+100, 200, 50, (0, 157, 255), (0, 0, 255), None, 2, QUESTIONS[i][2])
    b4 = Button(QUESTIONS[i][1][3], WIDTH/2+200, HEIGHT/2-100, 200, 50, (0, 255, 46), (0, 0, 255), None, 3, QUESTIONS[i][2])
    q = QUESTIONS[i][0]
    a = QUESTIONS[i][1]
    r = QUESTIONS[i][2]
    
    
    return b1,b2,b3,b4,q,a,r,QUESTIONSS
b1,b2,b3,b4,question,answer,right,QUESTIONSS = gen_q(0,[],True)



while True:
    C.tick(60)
    
    A = 0
    if N < TOA:
        if PL:
            Punkte = 0
            print("")
        PL = False
        L = False
        if Punkte > 0:Punkte -= .1
        if Punkte < 0:Punkte = 0
        b1.draw()
        b2.draw()
        b3.draw()
        b4.draw()
        try:
            draw_text(question, FONT, (255,255,255), WIN, WIDTH/2, HEIGHT/2)
            draw_text("Punkte: " + str(int(Punkte)), FONT, (255, 255, 255), WIN, WIDTH/2, HEIGHT/8)
            n = True
        except:
            n = False
            draw_text("Punkte: " + str(int(Punkte)), FONT, (255, 255, 255), WIN, WIDTH/2, HEIGHT/10)
        if b1.a == 1 or b2.a == 1 or b3.a == 1 or b4.a == 1:
            if n:
                try:
                    r = random.randint(0,len(QUESTIONS)-1)
                    N += 1
                    pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
                    Punkte += 100
                    b1,b2,b3,b4,question,answer,right,QUESTIONSS = gen_q(0,QUESTIONSS,True)                   
                    q += 1
                    b1.a = 0
                    b2.a = 0
                    b3.a = 0
                    b4.a = 0
                except:
                    pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
        if b1.a == -1 or b2.a == -1 or b3.a == -1 or b4.a == -1:
            if n:

                try:
                    r = random.randint(0,len(QUESTIONS)-1)
                    N += 1
                    pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
                    b1,b2,b3,b4,question,answer,right,QUESTIONSS = gen_q(0,QUESTIONSS,True)    
                    q += 1
                    b1.a = 0
                    b2.a = 0
                    b3.a = 0
                    b4.a = 0
                except:
                    pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)
            else:
                WIN.fill((25,25,30))
                draw_text("Punkte: " + str(int(Punkte)), FONT, (255, 255, 255), WIN, WIDTH/2, HEIGHT/10)
        
    else:


        for i in range(5):
            r = random.randint(0,len(QUESTIONS)-1)
        if not L:
            Scoreboard = AddLB(Scoreboard,Name,int(Punkte))
            Name = ""
            
        L = True
        pygame.draw.rect(WIN,(20,20,20),(0,0,WIDTH//3,HEIGHT))
        pygame.draw.rect(WIN,(50,255,50),(-1,-1,WIDTH//3,HEIGHT+2),1)
        Punkte = -100
        for i in range(10):#
            if not Scoreboard[i][0] == "":
                #draw_text(str(i+1) + ". " + Scoreboard[i][0] + " - " + str(Scoreboard[i][1]), FONT, (255, 255, 255), WIN, 20, 50+i*50)
                WIN.blit(FONT.render((str(i+1) + ". " + Scoreboard[i][0] + " - " + str(Scoreboard[i][1])), False, (255, 255, 255)), (10, 50+i*50))
            else:
                WIN.blit(FONT.render((str(i+1) + ". "), False, (255, 255, 255)), (10, 50+i*50))
        m = FONT.render(Name+"|",False,(255,255,255))
        M = FONT.render("______________________________",False,(255,255,255))
        WIN.blit(M,(WIDTH//2-M.get_width()//2,HEIGHT//3-M.get_height()//2))
        WIN.blit(m,(WIDTH//2-M.get_width()//2,HEIGHT//3-M.get_height()//2))
        BT = Button("Starten",WIDTH//2,HEIGHT//2,200,50,(255,255,255),(200,200,200),None,0,0)
        Punkte = 0
        BT.draw()
        PL = True
        if BT.b == 1:
            BT.b = 0
            
        
        if BT.a == 1 and len(Name) >= 1:
            N = 0
            while QUESTIONS != QUESTIONSS: QUESTIONSS = QUESTIONS
            q = 0
            BT.a = 0
            Played = True
            b = 9
            b1,b2,b3,b4,question,answer,right,QUESTIONSS = gen_q(0,[],True)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if not N < TOA:
                if event.key == pygame.K_BACKSPACE:
                    Name = Name[:-1]
                else:
                    
                    if event.unicode in LGCHARS and len(Name) < 30:
                        Name += event.unicode
            
    pygame.display.update()
    WIN.fill((30,30,30))