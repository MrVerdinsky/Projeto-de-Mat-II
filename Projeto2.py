import math
import pygame
import pygame.freetype
import time

grid_base = (80, 560)
grid_center = (645,356)
grid_divs = 10
def main():
    pygame.init()

    #Defines window resolution
    res = (1290, 712)

    # Load a font
    axis_labels_font = pygame.freetype.Font("NotoSans-Regular.ttf", 12)

    #Draws the window with previous parameters
    screen = pygame.display.set_mode(res)

   
    while(True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()
        # Draw grid
        draw_grid(screen, grid_base[0], grid_base[1], grid_divs,20,20, 1, (64, 128, 64, 255), axis_labels_font, [str(i) for i in range(1, 11)], [str(i) for i in range(1, 11)])
        draw_function(screen, (255, 0, 255, 255), lambda x : x*math.tan(30)-9.8*math.pow(x, 2)/2*math.pow((math.cos(30)*30),2) * math.pow(math.cos(30), 2))

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
        

def trajectory(velocity, angle,viscosity,gravity):
    Vx = math.cos(angle)*velocity
    Vy = math.sin(angle)*velocity
    V0 = [Vx, Vy]
    
    t1 = 2 * V0[0]* math.sin(angle) / gravity
    t2 = 2 * V0[1]* math.sin(angle) / gravity

    return(t1,t2)

def draw_grid(screen, x, y, grid_division, x_count, y_count, div_size, color, font, labels_x = None, labels_y = None):
    for yy in range(0, y_count + 1):
        pygame.draw.aaline(screen, color, (x, y - yy * grid_division), (x + x_count * grid_division, y - yy * grid_division))
    for xx in range(0, x_count + 1):
        pygame.draw.aaline(screen, color, (x + xx * grid_division, y), (x + xx * grid_division, y - y_count * grid_division))

    lx = [str(i) for i in range(0, x_count + 1)]
    if (labels_x != None):
        lx = labels_x
    ly = [str(i) for i in range(0, y_count + 1)]
    if (labels_y != None):
        ly = labels_y
    
    draw_graph_axis_x(screen, x, y, grid_division, x_count, div_size, color, font, lx)
    draw_graph_axis_y(screen, x, y, grid_division, y_count, div_size, color, font, ly)





def convert_coord(x,y):
    global grid_center 
    global grid_divs 

    return (grid_center[0] + x * grid_divs, grid_center[1] - y * grid_divs)

def draw_graph_axis_x(screen, x, y, x_inc, x_count, div_size, color, font = None, values = None):
    current_x = x
    for i in range(0, x_count + 1):
        pygame.draw.aaline(screen, color, (current_x, y - div_size), (current_x, y + div_size))

        if (font != None):
            width = font.get_rect(values[i]).width
            font.render_to(screen, (current_x - width, y + div_size + 4), values[i], color)

        current_x = current_x + x_inc

    pygame.draw.aaline(screen, color, (x,y), (x + x_count * x_inc, y))

def draw_graph_axis_y(screen, x, y, y_inc, y_count, div_size, color, font = None, values = None):
    current_y = y
    for i in range(0, y_count + 1):
        pygame.draw.aaline(screen, color, (x - div_size, current_y), (x + div_size, current_y))

        if (font != None):
            height = font.get_rect(values[i]).height
            font.render_to(screen, (current_y + height, x + div_size + 4), values[i], color)

        current_y = current_y - y_inc

    pygame.draw.aaline(screen, color, (x,y), (x, y - y_count * y_inc))

def draw_function(screen, color, func, domain = None):
    if (domain == None):
        x = prev_x = -3
        prev_y = func(prev_x)
    else:
        x = prev_x = domain[0]
        prev_y = func(prev_x)
    while (x < 3):
        x = x + 0.025
        if (domain != None):
            if ((x < domain[0]) or (x > domain[1])):
                continue
        pygame.draw.aaline(screen, color, convert_coord(prev_x, prev_y), convert_coord(x, func(x)))
        prev_x = x
        prev_y = func(x)
main()