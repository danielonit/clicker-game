# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Window caption
pygame.display.set_caption('Clicker Game')

# Font
text_font = pygame.font.SysFont("Courier", 30)

# Function to draw text on screen
def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

# Score count variable
score_count = 0

# Game Over Boolean
game_over = False

# Hit Left Wall Boolean
left_hit = True

# Hit Right Wall Boolean
right_hit = False

# Rectangle border width variable
rect_border = 1

# Rectangle movement speed
rect_xSpeed = 0

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if rect.collidepoint(mouse_position):
               score_count += 1
               rect_border=0
            else:
                game_over = True
        if event.type == pygame.MOUSEBUTTONUP:
            rect_border=1
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Rectangle Variables
    rect_x = 200+rect_xSpeed
    rect_y = 200
    rect_width = 100
    rect_height = 100

    # Rectangle variable created
    rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Draw score on screen
    if (score_count <= 20 and game_over == False):
        draw_text(f"Score: {score_count}", text_font, (255, 255, 255), 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), rect, rect_border)

        if (rect_x + rect_width >= 500):
            right_hit = True
            left_hit = False

        if (rect_x <= 0):
            right_hit = False
            left_hit = True

        if (score_count < 5):
            draw_text(f"Level 1", text_font, (255, 255, 255), 200, 100)

        if (score_count >= 5 and score_count < 10):
            draw_text(f"Level 2", text_font, (255, 255, 255), 200, 100)
            
            if (right_hit == True and left_hit == False):                
                rect_xSpeed -= 0.05
            
            if (right_hit == False and left_hit == True):
                rect_xSpeed += 0.05


        if (score_count >= 10 and score_count < 15):
            draw_text(f"Level 3", text_font, (255, 255, 255), 200, 100)

            if (right_hit == True and left_hit == False):                
                rect_xSpeed -= 0.1
            
            if (right_hit == False and left_hit == True):
                rect_xSpeed += 0.1

        if (score_count >= 15):
            draw_text(f"Level 4", text_font, (255, 255, 255), 200, 100)

            if (right_hit == True and left_hit == False):                
                rect_xSpeed -= 0.2
            
            if (right_hit == False and left_hit == True):
                rect_xSpeed += 0.2

    if (game_over == True and score_count <= 20):
        draw_text(f"You Lost!", text_font, (255, 255, 255), 200, 50)

    if (score_count > 20):
        draw_text(f"You Won!", text_font, (255, 255, 255), 200, 50)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
