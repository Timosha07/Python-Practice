import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    tool = 'brush'
    color = (0, 0, 255) 
    
    # Список для хранения всех нарисованных объектов
    elements = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                
                # Выбор цвета
                if event.key == pygame.K_r: color = (255, 0, 0)
                elif event.key == pygame.K_g: color = (0, 255, 0)
                elif event.key == pygame.K_b: color = (0, 0, 255)
                elif event.key == pygame.K_y: color = (255, 255, 0)
                
                # Выбор инструментов (добавлены новые пункты 5, 6, 7)
                if event.key == pygame.K_1: tool = 'brush'
                elif event.key == pygame.K_2: tool = 'square'
                elif event.key == pygame.K_3: tool = 'circle'
                elif event.key == pygame.K_4: tool = 'eraser'
                elif event.key == pygame.K_5: tool = 'right_triangle'
                elif event.key == pygame.K_6: tool = 'equilateral_triangle'
                elif event.key == pygame.K_7: tool = 'rhombus'

            # Изменение размера фигуры кнопками мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 2)
                elif event.button == 3: 
                    radius = max(2, radius - 2)
            
            # Рисование при зажатой кнопке
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    position = event.pos
                    current_draw_color = (0, 0, 0) if tool == 'eraser' else color
                    
                    elements.append([position, current_draw_color, radius, tool])
                    
                    if len(elements) > 2000:
                        elements.pop(0)
                
        screen.fill((0, 0, 0))
        
        # Отрисовка всех элементов
        for ent in elements:
            pos, col, rad, shape = ent
            x, y = pos
            
            if shape == 'brush' or shape == 'eraser':
                pygame.draw.circle(screen, col, pos, rad)
            
            elif shape == 'square':
                # Квадрат: рисуем rect с одинаковой шириной и высотой
                pygame.draw.rect(screen, col, (x - rad, y - rad, rad * 2, rad * 2))
            
            elif shape == 'circle':
                pygame.draw.circle(screen, col, pos, rad, 2)

            elif shape == 'right_triangle':
                # Прямоугольный треугольник (вершины: центр, вправо, вверх)
                points = [
                    (x, y), 
                    (x + rad * 2, y), 
                    (x, y - rad * 2)
                ]
                pygame.draw.polygon(screen, col, points)

            elif shape == 'equilateral_triangle':
                # Равносторонний треугольник (используем тригонометрию для равных сторон)
                # Вершина 1 (верх), вершины 2 и 3 (низ под углом 120 градусов)
                points = [
                    (x, y - rad),
                    (x - rad * math.sin(math.radians(60)), y + rad * math.cos(math.radians(60))),
                    (x + rad * math.sin(math.radians(60)), y + rad * math.cos(math.radians(60)))
                ]
                pygame.draw.polygon(screen, col, points)

            elif shape == 'rhombus':
                # Ромб (четыре точки: верх, право, низ, лево)
                points = [
                    (x, y - rad),      # Верх
                    (x + rad * 1.5, y), # Право (сделаем чуть шире)
                    (x, y + rad),      # Низ
                    (x - rad * 1.5, y)  # Лево
                ]
                pygame.draw.polygon(screen, col, points)
        
        # Панель управления
        info = f"Tool: {tool} | Color: {color} | Size: {radius}"
        font = pygame.font.SysFont("Arial", 18)
        text = font.render(info, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()