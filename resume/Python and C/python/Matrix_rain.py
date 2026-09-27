import pygame
import random

# Initialize Pygame
pygame.init()

# Setup display (Set to full screen or a large window)
# For a true wallpaper, you'll want your monitor's exact resolution
WIDTH, HEIGHT = 1920, 1080 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Digital Rain")

# Clock to control frame rate
clock = pygame.time.Clock()

# Fonts and Characters (Matrix uses Katakana, numbers, and symbols)
FONT_SIZE = 18

# 1. Try a list of known fonts that support Katakana/Japanese characters
possible_fonts = ["msmincho", "msgothic", "meiryo", "arial", "couriernew"]
font = None

for font_name in possible_fonts:
    # False, False disables bold/italic to keep it crisp
    font = pygame.font.SysFont(font_name, FONT_SIZE, False, False)
    # Test if the font actually loaded something valid instead of None
    if font:
        break

# 2. Complete fallback if no specific system fonts are found
if not font:
    font = pygame.font.Font(None, FONT_SIZE)

# 3. Dynamic Character List
# If we ended up using a basic font like Arial/Default, Katakana might look like empty boxes.
# To be safe, we check if we got a Japanese font. If not, we fall back to matrix-style alphanumeric/binary text.
if font.name in ["msmincho", "msgothic", "meiryo"]:
    chars = [chr(int(i)) for i in range(12448, 12543)] + [str(i) for i in range(10)] + ['!', '#', '$', '%', '*', '+', '-', '<', '>']
else:
    # High-tech cyberpunk alphanumeric/binary mix if Japanese symbols aren't supported
    chars = [chr(int(i)) for i in range(33, 126)] # Standard ASCII matrix characters
FONT_CHARS = [font.render(char, True, (0, 255, 0)) for char in chars]
WHITE_CHARS = [font.render(char, True, (255, 255, 255)) for char in chars]

# Column setup
column_width = FONT_SIZE
num_columns = WIDTH // column_width
# Tracks the current Y position of each falling column
drops = [random.randint(-100, 0) for _ in range(num_columns)]
# Tracks the speed of each individual column
speeds = [random.randint(2, 5) for _ in range(num_columns)]

running = True
while running:
    # Handle exiting the preview
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # 1. Trick for trailing effect: Draw a semi-transparent black surface over the old frame
    # This creates the fading green "tail" behind the bright leading characters
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.set_alpha(15) # Lower alpha = longer trails
    fade_surface.fill((0, 0, 0))
    screen.blit(fade_surface, (0, 0))

    # 2. Draw the falling code
    for i in range(num_columns):
        # Pick a random character
        char_index = random.randint(0, len(chars) - 1)
        
        # Calculate screen coordinates
        x = i * column_width
        y = drops[i] * FONT_SIZE

        if 0 <= y < HEIGHT:
            # Randomly make the leading head of the stream white for realism
            if random.random() > 0.95:
                screen.blit(WHITE_CHARS[char_index], (x, y))
            else:
                screen.blit(FONT_CHARS[char_index], (x, y))

        # Move the drop down by its unique speed
        drops[i] += speeds[i]

        # Reset drop to the top with a random delay once it goes off-screen
        if y > HEIGHT and random.random() > 0.975:
            drops[i] = random.randint(-20, 0)
            speeds[i] = random.randint(2, 5)

    pygame.display.flip()
    clock.tick(30) # 30 FPS keeps CPU usage lower for a background task

pygame.quit()