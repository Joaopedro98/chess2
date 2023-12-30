

#Chess comum

import pygame as p

import ChessEngine

width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15 #para animação
imagens = {}

def loadimages():
    pieces = ["wp","wR","wN","wB", "wQ", "wK", "wB", "wN" ,"wR","bR","bN","bB", "bQ", "bK", "bB", "bN" ,"bR", "bp"]
    for piece in pieces:
        imagens[piece]=p.transform.scale(p.image.load("image/" + piece + ".png"),(sq_size,sq_size))
        #Podemos acessar um elemento do conjunto imagens como "imagens[nome]"

def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.game_state()
    loadimages()
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGamestate(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawGamestate(screen, gs):
    drawBoard(screen) #draw squares on the board    
    drawPieces(screen, gs.board) #draw the pieces on the top of display

def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray"), p.Color("red")]
    for i in range(dimension):
        for j in range(dimension):
            color = colors[(j+i)%3]
            p.draw.rect(screen, color, p.Rect(j*sq_size,i*sq_size,sq_size,sq_size))
        
            
    

def drawPieces(screen,gs):
    pass


#if __name__ == "__chess2__":
main()

