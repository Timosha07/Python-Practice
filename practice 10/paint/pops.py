import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    
    tool = 'brush'
    color = (0, 0, 255) 
    
    
    elements = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE: return
                
               
                if event.key == pygame.K_r: color = (255, 0, 0)
                elif event.key == pygame.K_g: color = (0, 255, 0)
                elif event.key == pygame.K_b: color = (0, 0, 255)
                elif event.key == pygame.K_y: color = (255, 255, 0)
                
               
                if event.key == pygame.K_1: tool = 'brush'
                elif event.key == pygame.K_2: tool = 'rect'
                elif event.key == pygame.K_3: tool = 'circle'
                elif event.key == pygame.K_4: tool = 'eraser'

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 2)
                elif event.button == 3: 
                    radius = max(2, radius - 2)
            
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    position = event.pos
                    
                    
                    current_draw_color = (0, 0, 0) if tool == 'eraser' else color
                    
                    
                    elements.append([position, current_draw_color, radius, tool])
                    
                    if len(elements) > 2000:
                        elements.pop(0)
                
        screen.fill((0, 0, 0))
        
        
        for ent in elements:
            pos, col, rad, shape = ent
            
            if shape == 'brush' or shape == 'eraser':
                pygame.draw.circle(screen, col, pos, rad)
            
            elif shape == 'rect':
                
                pygame.draw.rect(screen, col, (pos[0] - rad, pos[1] - rad, rad * 2, rad * 2))
            
            elif shape == 'circle':
                
                pygame.draw.circle(screen, col, pos, rad, 2)
        
        
        info = f"Tool: {tool} | Color: {color} | Size: {radius}"
        font = pygame.font.SysFont("Arial", 18)
        text = font.render(info, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()