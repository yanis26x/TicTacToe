import pygame
import os
import sys

def get_path(relative_path):
    """Gère les chemins pour compatibilité avec les .exe PyInstaller"""
    if getattr(sys, '_MEIPASS', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

def show_start_screen(screen, T):
    # Charger le son d'intro
    intro_sound = pygame.mixer.Sound(get_path("OST/swamp-ah-ah.wav"))
    intro_sound.set_volume(1.0)  # 🔊 Volume max
    intro_sound.play()

    # Charger l'image de fond sang
    image = pygame.image.load(get_path("IMG/sang.png"))
    image = pygame.transform.scale(image, (T, T))
    image.set_alpha(180)  # 70% d'opacité

    # Afficher l'image de fond
    screen.fill((0, 0, 0))  # Fond noir par sécurité
    screen.blit(image, (0, 0))

    # Afficher le texte
    font_intro = pygame.font.Font(None, 30)
    message = font_intro.render("FOLLOW ME EVERYWHERE @yanis26x", True, (255, 255, 255))
    rect = message.get_rect(center=(T//2, T//2))
    screen.blit(message, rect)

    pygame.display.flip()
    
    # Attendre 5 secondes pendant que le son joue
    pygame.time.delay(5000)
