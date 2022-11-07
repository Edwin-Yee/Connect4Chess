import numpy as np
import pygame
import random
import math
import sys
import neat
import os

from Connect4Chess import global_
from global_ import *
from classes import Sprite
from classes import BoardSquare
from functions import draw_board

# Initializing Pygame
pygame.init()

# Initializing the board
draw_board()
squares_list.update()
squares_list.draw(surface)

pygame.display.flip()

num_click = 0
isButtonPressed = False
isSpriteClicked = False

# class ConnectGame:
#     def __init__(self, window, width, height):
#         self.game = Game(window, width, height)
# TODO put game into separate class with initialization

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_position, y_position = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]

            for sprite in all_sprites_list:
                if sprite.mouse_click_check(x_position, y_position):
                    current_click_sprite_list.add(sprite)
                    print("Added sprite", sprite.name, "to current_click_sprite_list")
                    isSpriteClicked = True

            print("--------")
            if len(buttons) == 3:
                button_1 = buttons.sprites()[0]  # Middle Button
                button_2 = buttons.sprites()[1]  # Left Button
                button_3 = buttons.sprites()[2]  # Right Button

                if button_1.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 1 PRESSED!")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
                elif button_2.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 2 PRESSED!")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
                elif button_3.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 3 PRESSED!")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
                elif not button_1.rect.collidepoint(x_position, y_position) \
                        and not button_2.rect.collidepoint(x_position, y_position) \
                        and not button_3.rect.collidepoint(x_position, y_position) \
                        and not isSpriteClicked and mouse_clicked and num_click % 2 == 1:
                    print("No Button has been pressed")
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
            elif len(buttons) == 2:

                button_1 = buttons.sprites()[0]  # Some Button
                button_2 = buttons.sprites()[1]  # Some Button

                if button_1.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 1 PRESSED! (EDGE CASE)")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
                elif button_2.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 2 PRESSED! (EDGE CASE)")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
                elif not button_1.rect.collidepoint(x_position, y_position) \
                        and not button_2.rect.collidepoint(x_position, y_position) \
                        and not isSpriteClicked and mouse_clicked and num_click % 2 == 1:
                    print("No Button has been pressed")
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()
            elif len(buttons) == 1:

                button_1 = buttons.sprites()[0]  # Some Button

                if button_1.rect.collidepoint(x_position, y_position) and mouse_clicked:
                    print("BUTTON 1 PRESSED! (ONLY 1 EDGE CASE)")
                    curr_sprite_color = current_click_sprite_list.sprites()[0].color
                    current_click_sprite_list.sprites()[0].move(curr_sprite_color, x_position, y_position)
                    current_click_sprite_list.empty()
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()

                elif not button_1.rect.collidepoint(x_position, y_position) \
                        and not isSpriteClicked and mouse_clicked and num_click % 2 == 1:
                    print("No Button has been pressed")
                    for button in buttons:
                        button.kill()
                        pygame.display.flip()





            # for button in buttons:
            #     if button.rect.collidepoint(x_position, y_position) and mouse_clicked:
            #         print("BUTTON PRESSED!")
            #         # current_click_sprite_list.sprites()[0].move(x_position, y_position)
            #         isButtonPressed = True
            #
            #     elif not button.rect.collidepoint(x_position, y_position) and not isSpriteClicked and mouse_clicked:
            #         print("Not button pressed!")
            #
            #     elif (not isButtonPressed) and (num_click % 2 == 1) and not \
            #             (button.rect.collidepoint(pygame.mouse.get_pos()) and not mouse_clicked):
            #         print("Removed all buttons")
            #         current_click_sprite_list.empty()
            #         for button2 in buttons:
            #             button2.kill()
            #             pygame.display.flip()
            #
            # isButtonPressed = False
            isSpriteClicked = False
            num_click = num_click + 1
            pygame.display.flip()

    # Update the board squares
    squares_list.update()
    squares_list.draw(surface)

    # Draws all sprites to the given Surface.
    buttons.update()  # Calls the update method on every sprite in the group.
    buttons.draw(surface)
    all_sprites_list.update()
    all_sprites_list.draw(surface)

    pygame.display.update()

    pygame.display.flip()



# def eval_genomes(genomes, config):
#     # Genomes is a list of tuples
#     # Every AI playing against every other AI (cut by i+1)
#     width, height = SURFACE_WIDTH, SURFACE_HEIGHT
#     window = pygame.display.set_mode((width, height))
#
#     for i, (genome_id1, genome1) in enumerate(genomes):
#
#         # Check out of bounds
#         if i + 1 == len(genomes):
#             break
#
#         genome1.fitness = 0     # initialize fitness level
#         for genome_id2, genome2 in genomes[i+1:]:
#             if genome2.fitness is None:
#                 genome2.fitness = 0     # initialize fitness if not set before
#
#             game = thegame()
#             game.train_ai(genome1, genome2, config) # TODO
# def run_neural_network(config):
#     # example usage
#     # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-2')
#     population = neat.Population(config)
#
#     # See generations, data
#     population.add_reporter(neat.StdOutReporter(True))
#     statistics = neat.StatisticsReporter()
#     population.add_reporter(statistics)
#
#     # Save a checkpoint after x generations, currently set to 1
#     population.add_reporter(neat.Checkpointer(1))
#
#     # Max gen: set to 50
#     best_winner = population.run(eval_genomes, 50)
#
#
# if __name__ == "__main__":
#     local_directory = os.path.dirname(__file__)
#     config_path = os.path.join(local_directory, "config.txt")
#
#     # load config file
#     config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_path)
#
#     run_neural_network(config)
