import sys
from collections import deque

def load_data(filename):
    with open(filename, mode="rt") as input:
        lines = list(map(int, input.read().split(',')))
    return lines

def start_simulation(data, time):
    fish_list = data
    generation_bins = [0 for i in range(9)]
    for initial_fish in fish_list:
        generation_bins[initial_fish] += 1
    for step in range(time):
        buffer = generation_bins[0]
        generation_bins = deque(generation_bins)
        generation_bins.rotate(-1)
        generation_bins = list(generation_bins)
        generation_bins[6] += buffer
        print("Day: ", step+1, ": ",generation_bins, "Fishcount: ", sum(generation_bins))
    return generation_bins



def generate_result(final_list):
    return len(data)

if __name__ == '__main__':
    data = load_data('input.txt')
    final_list = start_simulation(data, 256)
    #print(final_list)
