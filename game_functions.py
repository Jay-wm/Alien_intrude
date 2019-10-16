import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下键盘"""

    # 右键被按下
    if  event.key == pygame.K_RIGHT:
        ship.moving_right = True

    # 左键被按下
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
    # 创建一颗新的子弹，并加入bullets组中
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    if event.key == pygame.K_q:
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


def check_aliens_edges(ai_settings, aliens):
    """限制外星人，不让其超越边界"""
    for alien in aliens.sprites():
        if  alien.check_edges():
            change_aliens_speed_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break            


def change_aliens_speed_direction(ai_settings, aliens):
    """向下移动外星人，并改变外星人移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.aliens_drop_speed
    ai_settings.aliens_speed_direction *= -1
    

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边界，并更新外星人位置"""
    check_aliens_edges(ai_settings, aliens)
    aliens.update()
    
    # 检测外星人与飞船的距离
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """添加子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    
        
def update_screen(ai_settings, screen, ship, aliens, bullets, play_button):
    """update the images on the screen and flip to the new screen"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # 非活跃状态绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
            
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置，并删除已消失子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

            
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹与外星人碰撞"""
    # 删除发生碰撞的子弹与外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # 删除现有的子弹并新建一群外星人
    if len(aliens) == 0:
        bullets.empty()
        creat_aliens(ai_settings, screen, ship, aliens)
    

def get_number_aliens_x(ai_settings, alien_width):
    """计算一行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    """计算一列可容纳多少外星人"""
    available_space_y = ai_settings.screen_height-3 * alien_height - ship_height
    number_aliens_y = int(available_space_y / (2*alien_height))
    return number_aliens_y


def create_alien(ai_settings, screen, aliens, alien_x_number, alien_y_number):
    """创建外星人""" 
    alien = Alien(ai_settings, screen)
    
    # 外星人间距等于外星人宽度
    alien_width = alien.rect.width
    
    # 将新的外星人加入当前行或列
    alien.x = alien_width + 2 * alien_width * alien_x_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_y_number
    aliens.add(alien)
    
    
def create_aliens(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算该行或列最大容下多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)
    
    for alien_y_number in range(number_aliens_y):
        for alien_x_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_x_number, alien_y_number)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    # 将ships_left减1
    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
    
    
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    
    # 创建一群新的外星人，并将飞船放到屏幕底端中央
    create_aliens(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    # 暂停
    sleep(0.5)


    
   

    
    





    
