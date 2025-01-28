import pygame
import time
import random

# Initialize Pygame and font
pygame.init()
pygame.font.init()

# Window dimensions
width, height = 1000, 800

# Player settings
playerPositionX, playerPositionY = 450, 700
playerWidth, playerHeight = 100, 160
playerVelocity = 7

# Star settings
starWidth, starHeight = 40, 40
starVel = 10
starInc = 2000  # Spawn interval in milliseconds
starCount = 0


# Fonts and images
font = pygame.font.SysFont("Impact", 30)
BG = pygame.transform.scale(pygame.image.load("BG.jpg"), (width, height))
starimg = pygame.transform.scale(pygame.image.load("ast.png"), (starWidth, starHeight))
player_img = pygame.transform.scale(pygame.image.load("ship.png"), (playerWidth, playerHeight))

# Create window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge the Stars")

# Load music
pygame.mixer.music.load("bgm.mp3")  
pygame.mixer.music.set_volume(0.5)  #  Set volume to 50%
pygame.mixer.music.play(-1)  # Play music in an infinite loop



def draw(player_rect, upTime, stars):
    """Draws game elements on the screen."""
    window.blit(BG, (0, 0))
    window.blit(player_img, (player_rect.x, player_rect.y))
    time_text = font.render(f"Time: {round(upTime)}s", 1, "white")
    window.blit(time_text, (10, 10))
    
    for star in stars:
        window.blit(starimg, (star.x, star.y))
    
    pygame.display.update()


def main():
    global playerPositionX, playerPositionY
    
    # Initialize game variables
    clock = pygame.time.Clock()
    start_time = time.time()
    stars = []
    starTimer = 0  # Timer for spawning stars
    
    # Player rectangle
    player_rect = pygame.Rect(playerPositionX, playerPositionY, playerWidth, playerHeight)
    
    run = True
    while run:
        clock.tick(60)
        upTime = time.time() - start_time
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_rect.x - playerVelocity > 0:
            player_rect.x -= playerVelocity
        if keys[pygame.K_d] and player_rect.x + player_rect.width + playerVelocity < width:
            player_rect.x += playerVelocity
        
        # Star spawning
        starTimer += clock.get_time()
        if starTimer > starInc:
            for _ in range(7):  # Spawn 7 stars at a time
                starX = random.randint(0, width - starWidth)
                star = pygame.Rect(starX, -starHeight, starWidth, starHeight)
                stars.append(star)
                
            starTimer = 0  # Reset the timer
        
        # Update stars
        for star in stars[:]:
            star.y += starVel
            if star.y > height:  # Remove stars that move off-screen
                stars.remove(star)
            elif star.colliderect(player_rect):  # Check collision
                run = False  # End game on collision
        
        # Draw everything
        draw(player_rect, upTime, stars)
    
    pygame.quit()

#someshit i dont understand
if __name__ == "__main__":
    main()
