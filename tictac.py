from StartScreen import show_start_screen
import pygame
import os
import sys

pygame.init()

# Gérer les fichiers dans l'exécutable
def get_path(relative_path):
    """Retourne le bon chemin, que ce soit en mode script ou exécutable .exe"""
    if getattr(sys, '_MEIPASS', False):  # Si c'est un .exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

# Chargement des sons
pygame.mixer.music.load(get_path("OST/musicCool.wav"))  # Musique de fond
pygame.mixer.music.play(-1)  # Lecture en boucle
son_victoire = pygame.mixer.Sound(get_path("OST/yay.wav"))
son_dahak = pygame.mixer.Sound(get_path("OST/BASKETpELE.wav"))
son_woo = pygame.mixer.Sound(get_path("OST/woo.wav"))

# Création de la fenêtre
T = 500
screen = pygame.display.set_mode((T, T))
pygame.display.set_caption("Tic-Tac-Toe26x")

# Chargement des images
image = pygame.image.load(get_path("IMG/sang.png"))
image = pygame.transform.scale(image, (T, T))
image.set_alpha(180)  # 70% d'opacité
img_X = pygame.image.load(get_path("IMG/xRed.png"))
img_X = pygame.transform.scale(img_X, (T//3 - 20, T//3 - 20))
img_O = pygame.image.load(get_path("IMG/circleWater.png"))
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
        text = font.render("TES UN GROS SAC DE PATATES, TES POURIE !", True, (255, 0, 0))
        screen.blit(text, (T//6, T//3))
        pygame.draw.rect(screen, (255, 0, 0), (T//4, T//2, T//2, 50))
        text_btn = font.render("Recommencer", True, (0, 0, 0))
        screen.blit(text_btn, (T//4 + 20, T//2 + 10))
    
    # Signature en bas à droite
    font_signature = pygame.font.Font(None, 30)
    signature = font_signature.render("yanis26x", True, (255, 0, 255))
    screen.blit(signature, (T - 100, T - 30))
    pygame.display.flip()

# Vérifier la victoire
def victoire(j):
    return any(all(grille[y][x] == j for x in range(3)) for y in range(3)) or \
           any(all(grille[y][x] == j for y in range(3)) for x in range(3)) or \
           all(grille[i][i] == j for i in range(3)) or \
           all(grille[i][2 - i] == j for i in range(3))

# Afficher l'écran de démarrage une première fois
show_start_screen(screen, T)

# Boucle du jeu
running = True
while running:
    dessiner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0] // (T // 3), event.pos[1] // (T // 3)
            if gagnant or all(all(cell is not None for cell in row) for row in grille):
                if T//4 < event.pos[0] < T//4 + T//2 and T//2 < event.pos[1] < T//2 + 50:
                    grille = [[None]*3 for _ in range(3)]
                    gagnant = None
                    show_start_screen(screen, T)  # 👉 Réaffiche l'écran de démarrage
            elif not grille[y][x]:
                grille[y][x] = joueur
                if victoire(joueur):
                    gagnant = f"Joueur {'1' if joueur == 'X' else '2'}"
                    pygame.mixer.Sound.play(son_victoire)
                joueur = 'O' if joueur == 'X' else 'X'
                pygame.mixer.Sound.play(son_woo)

pygame.quit()
sys.exit()
