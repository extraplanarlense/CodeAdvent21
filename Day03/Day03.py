def load_data(filename):
    with open(filename) as f:
       numbers_string = f.read().splitlines()
    return numbers_string

def bin2dec(bin):
    dec = 0
    number_digits = len(bin)
    print(number_digits)
    for base, value in enumerate(bin):
        dec += value * (pow(2, (number_digits-base) - 1))
    return dec

# def bin2dec(bin):
#     dec = 0
#     number_digits = len(bin)
#     print(number_digits)
#     for base, value in enumerate(bin):
#         dec += value * (pow(2, (number_digits-base) - 1))
#     return dec

def calc_epsilon_rate(bin):
    epsilon_rate = []
    for digit in bin:
        if digit == 0:
            epsilon_rate.append(1)
        else:
            epsilon_rate.append(0)
    return epsilon_rate

def calc_gamma_rate(input):
    result = []
    for i in range(len(input[0])):
        ones = 0
        zeroes = 0
        for j in range(len(input)):
            if input[j][i] == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            result.append(0)
        else:
            result.append(1)
    return result

def calc_power_consumption(gamma_rate_dec, epsilon_rate_dec):
    return gamma_rate_dec * epsilon_rate_dec

def calc_oxygen_generator_rating(input):
    o_g_r = input
    counter = 0
    while len(o_g_r) > 1:
        ones = []
        zeroes = []
        for current_number in o_g_r:
            if current_number[counter] == "0":
               zeroes.append(current_number)
            else:
                ones.append(current_number)
        if (len(ones) > len(zeroes)) or (len(ones) == len(zeroes)):
            o_g_r = ones
        else:
            o_g_r = zeroes
        counter += 1
    return [int(i) for i in str(o_g_r[0])]

def calc_co2_scrubbing_rating(input):
    c_s_r = input
    counter = 0
    while len(c_s_r) > 1:
        ones = []
        zeroes = []
        for current_number in c_s_r:
            if current_number[counter] == "0":
               zeroes.append(current_number)
            else:
                ones.append(current_number)
        if (len(ones) > len(zeroes)) or (len(ones) == len(zeroes)):
            c_s_r = zeroes
        else:
            c_s_r = ones
        counter += 1
    return [int(i) for i in str(c_s_r[0])]

def calc_life_support_rating(o_g_r, c_s_r):
    return bin2dec(o_g_r) * bin2dec(c_s_r)

if __name__ == '__main__':
   numbers = load_data("input.txt")
   gamma_rate_bin = calc_gamma_rate(numbers)
   gamma_rate_dec = bin2dec(gamma_rate_bin)
   epsilon_rate_bin = calc_epsilon_rate(gamma_rate_bin)
   epsilon_rate_dec = bin2dec(epsilon_rate_bin)
   oxygen_generator_rating = calc_oxygen_generator_rating(numbers)
   co2_scrubbing_rating = calc_co2_scrubbing_rating(numbers)
   life_support_rating = calc_life_support_rating(oxygen_generator_rating, co2_scrubbing_rating)

   print("Gamma-rate bin: ", gamma_rate_bin)
   print("Gamma-rate dec: ", gamma_rate_dec)
   print("Epsilon-rate bin: ", epsilon_rate_bin)
   print("Epsilon-rate dec: ", epsilon_rate_dec)
   print("Power Consumption: ", calc_power_consumption(gamma_rate_dec, epsilon_rate_dec))
   print("oxygen generator rating: ", oxygen_generator_rating)
   print("CO2 scrubber rating: ", co2_scrubbing_rating)
   print("life support rating: ", life_support_rating)