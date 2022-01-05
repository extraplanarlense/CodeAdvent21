def load_data(filename):
    with open(filename, mode="rt") as input:
        lines = list(map(int, input.read().split(',')))
    return lines

def calc_Fuel_cost(data, mode):
    size = max(data)
    cost = [0 for idx in range(size + 1)]
    for position in range(size + 1):
        for element in data:
            distance = abs(element - position)
            if mode == "const":
                cost[position] += abs(element - position)
            if mode == "cum":
                cost[position] += int((distance * (distance + 1)) / 2)
    return cost

if __name__ == '__main__':
    data = load_data("input.txt")
    Fuel_cost = calc_Fuel_cost(data, "const")
    cum_Fuel_cost = calc_Fuel_cost(data, "cum")
    print ("Cost of Alignemnent at every Position: ", Fuel_cost)
    print ("Minimum Fuel Cost is: ", min(Fuel_cost), "at Position:", Fuel_cost.index(min(Fuel_cost)))
    print("Cost of cumulative Alignemnent at every Position: ", cum_Fuel_cost)
    print("Minimum Fuel Cost [cumulative] is: ", min(cum_Fuel_cost), "at Position:", cum_Fuel_cost.index(min(cum_Fuel_cost)))

