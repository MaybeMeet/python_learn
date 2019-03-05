import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ check whether any aliens arriving screen bottom """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # do the same like ship hit aliens
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ when alien hit ship, respond """
    if stats.ship_left > 0:
        # let ships_left subtract 1
        stats.ship_left -= 1

        # update the scoreboard
        sb.prep_ships()

        # clear the aliens and bullets
        aliens.empty()
        bullets.empty()

        # creat a new fleet aliens. put ship on the center of screen
        create_fleet(ai_settings, screen, ship, aliens) 
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings, aliens):
    """ when alien arrive the screen's orign, action. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ let the alien fleet move down, and change their direction. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def get_number_rows(ai_settings, ship_height, alien_height):
    """ count the screen can own how many row alien. """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """ create alien's fleet. """
    # the distance between two alien is equal the width of alien
    alien = Alien(ai_settings, screen)
    # alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # creat first cow alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """ count each line can occupy how many aliens. """
    available_space_x = ai_settings.screen_with - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #creat a alien and jion the fleet
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ respond for keydown """
    if event.key == pygame.K_RIGHT:
        # ship go right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # ship go left
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(ai_settings,screen,ship,bullets):
    # creat a bullet, and add it in bullets group
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_keyup_events(event,ship):
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ respond for mouse and keyboards events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        # go right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # go left
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,bullets, mouse_x, mouse_y):
    """ clik Play button, game start. """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
    # if play_button.rect.collidepoint(mouse_x, mouse_y):
        # reset game data
        stats.reset_stats()
        stats.game_active = True

        # reset the image of score record
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # clear aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet aliens. let the ship on center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ update the image, and show in new screen."""
    
        # blit the images
    screen.fill(ai_settings.bg_color)
    #flash all bullets after ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # show score
    sb.show_score()

    # if game be inactive, drawing Play button
    if not stats.game_active:
        play_button.draw_button()

    # show the new image in screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ update position of bullets and delete the bullet out of screen. """
    # update bullet's position
    bullets.update()
    
    # delete the bullets which don't show in screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # check whether bullets hit alien
    # if yesm delete the bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # delete exist bullets, speed up game and create new fleet and impore a level
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        # upgrade level
        stats.level += 1
        sb.prep_level()


def check_high_score(stats, sb):
    """ check if preduce the highest score. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ 
    check whether alien at screen's margin, update aliens position. 
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check the collision between ship and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # check whether alien come screen bottom
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
