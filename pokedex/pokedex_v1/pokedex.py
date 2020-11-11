#! /usr/bin/env python3.9
import csv
import os
import logging
import traceback

try: 
    os.chdir('./pokedex/pokedex_v1')

    if not os.path.exists('./logs'):
        os.mkdir('./logs')

    logging.basicConfig(filename='./logs/pokedex_logs.txt',level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

    file_object = open('./../data/pokemon-data.csv', newline='')
    csv_reader = csv.reader(file_object)

    pokemonlistall = []

    for row in csv_reader:
        pokemonlistall.append(row)

    file_object.close()
    logging.info('Step 1: accessed .csv file was successful!')

    pokemonlistSubSet = []
    # filter out all the pokemon that have Mega in their name since we only want the first original 151 pokemon
    pokemonlistSubSet = filter(lambda pokemon: 'mega' not in pokemon[1].lower(), pokemonlistall)
    pokemonlistSubSet = list(pokemonlistSubSet)[1:152]
    logging.info('Step 2: filtered out non 151 original pokemon was successful!')

    logging.debug('logging first 151 original pokemon for debugging')
    for pokemon_data in pokemonlistSubSet:
        logging.debug(pokemon_data)

    def sortPokemonByPower(listOfPokemon):
        sorted_pokemon = []
        listOfPokemon.sort(key=lambda pokemon: int(pokemon[6]))
        for pokemon_data in listOfPokemon:
            sorted_pokemon.append([pokemon_data[6], pokemon_data[1]])
        return sorted_pokemon 

    sorted_pokemon = sortPokemonByPower(pokemonlistSubSet)
    logging.info('Step 3: sorted first 151 original by pokemon attack power was successful!')

    # write sorted output to csv file
    if not os.path.exists('./output'):
        os.mkdir('./output')

    results_file = open('./output/pokedex-output.csv', 'w', newline='')
    csv_writter_object = csv.writer(results_file)

    csv_writter_object.writerow(['attack power','name'])
    csv_writter_object.writerows(sorted_pokemon)
    results_file.close()

    logging.info('Step 4: outputed csv with sorted pokemon by attack power was successful!\n')
    print('SUCCESS: sorted pokemon by attack power, please see ./output/pokedex-output.csv')
except:
    print('CRITICAL FAILURE: see logs for more details')
    logging.critical(traceback.format_exc())
