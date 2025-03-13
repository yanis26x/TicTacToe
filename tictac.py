import pygame

pygame.init()

# Chargement des sons
pygame.mixer.music.load("./OST/musicCool.wav")  # Musique de fond
pygame.mixer.music.play(-1)  # Lecture en boucle
son_victoire = pygame.mixer.Sound("./OST/yay.wav")

# Création de la fenêtre
T = 500
screen = pygame.display.set_mode((T, T))
pygame.display.set_caption("Tic-Tac-Toe26x")

# Chargement des images
image = pygame.image.load("sang.png")
image = pygame.transform.scale(image, (T, T))
image.set_alpha(180)  # 70% d'opacité
img_X = pygame.image.load("./IMG/xRed.png")
img_X = pygame.transform.scale(img_X, (T//3 - 20, T//3 - 20))
img_O = pygame.image.load("./IMG/circleRed.png")
img_O = pygame.transform.scale(img_O, (T//3 - 20, T//3 - 20))

# Grille
grille = [[None]*3 for _ in range(3)]
joueur = 'X'
gagnant = None

# Dessiner la grille
def dessiner():
    screen.fill((0, 0, 0))  # Fond noir
    screen.blit(image, (0, 0))
    for i in range(1, 3):
        pygame.draw.line(screen, (255, 0, 0), (0, i * T//3), (T, i * T//3), 3)
        pygame.draw.line(screen, (255, 0, 0), (i * T//3, 0), (i * T//3, T), 3)
    for y in range(3):
        for x in range(3):
            if grille[y][x]:
                pos = (x * T//3 + 10, y * T//3 + 10)
                screen.blit(img_O if grille[y][x] == 'O' else img_X, pos)
    font = pygame.font.Font(None, 50)
    if gagnant:
        text = font.render(f"{gagnant} a gagné !", True, (255, 0, 0))
        screen.blit(text, (T//6, T//3))
        pygame.draw.rect(screen, (255, 0, 0), (T//4, T//2, T//2, 50))
        text_btn = font.render("Recommencer", True, (0, 0, 0))
        screen.blit(text_btn, (T//4 + 20, T//2 + 10))
    elif all(all(cell is not None for cell in row) for row in grille):
        text = font.render("Vous êtes trop cons !", True, (255, 0, 0))
        screen.blit(text, (T//6, T//3))
        pygame.draw.rect(screen, (255, 0, 0), (T//4, T//2, T//2, 50))
        text_btn = font.render("Recommencer", True, (0, 0, 0))
        screen.blit(text_btn, (T//4 + 20, T//2 + 10))
    pygame.display.flip()

# Vérifier la victoire
def victoire(j):
    return any(all(grille[y][x] == j for x in range(3)) for y in range(3)) or any(all(grille[y][x] == j for y in range(3)) for x in range(3)) or all(grille[i][i] == j for i in range(3)) or all(grille[i][2-i] == j for i in range(3))

# Boucle du jeu
while True:
    dessiner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0] // (T//3), event.pos[1] // (T//3)
            if gagnant or all(all(cell is not None for cell in row) for row in grille):
                if T//4 < event.pos[0] < T//4 + T//2 and T//2 < event.pos[1] < T//2 + 50:
                    grille = [[None]*3 for _ in range(3)]
                    gagnant = None
            elif not grille[y][x]:
                grille[y][x] = joueur
                if victoire(joueur):
                    gagnant = f"Joueur {'1' if joueur == 'X' else '2'}"
                    pygame.mixer.Sound.play(son_victoire)
                joueur = 'O' if joueur == 'X' else 'X'
