import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下键盘"""

    # 右键被按下
    if  event.key == pygame.K_RIGHT:
        ship.moving_right = True

    # 左键被按下
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # 创建一颗新的子弹，并加入bullets组中
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开键盘"""
    if  event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """监控键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

            
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) <= ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    
        
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the images on the screen and flip to the new screen"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后面绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
            
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置，并删除已消失子弹"""

    # 更新子弹位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """计算一行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x / alien_width)
    return number_aliens_x


def creat_aliens(ai_settings, screen, aliens, alien_number):
    """创建外星人""" 
    alien = Alien(ai_settings, screen)
    
    # 外星人间距等于外星人宽度
    alien_width = alien.rect.width
    
    # 将新的外星人加入当前行
    alien_x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien_x
    aliens.add(alien)
    
    
def creat_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算该行最大容下多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    
    # number_aliens_x为奇数时
    if (number_aliens_x % 2) != 0:
        for alien_number in range(int(number_aliens_x / 2 + 1)):
            creat_aliens(ai_settings, screen, aliens, alien_number)
            
    # number_aliens_x为偶数时
    elif (number_aliens_x % 2) == 0:
         for alien_number in range(int(number_aliens_x / 2)):
             creat_aliens(ai_settings, screen, aliens, alien_number)
            
    
   

    
    





    
