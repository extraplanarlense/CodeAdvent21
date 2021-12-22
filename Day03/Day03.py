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

def power_consumption(gamma_rate_dec, epsilon_rate_dec):
    return gamma_rate_dec * epsilon_rate_dec

if __name__ == '__main__':
   numbers = load_data("input.txt")
   gamma_rate_bin = calc_gamma_rate(numbers)
   gamma_rate_dec = bin2dec(gamma_rate_bin)
   epsilon_rate_bin = calc_epsilon_rate(gamma_rate_bin)
   epsilon_rate_dec = bin2dec(epsilon_rate_bin)
   print("Gamma-rate bin: ", gamma_rate_bin)
   print("Gamma-rate dec: ", gamma_rate_dec)
   print("Epsilon-rate bin: ", epsilon_rate_bin)
   print("Epsilon-rate dec: ", epsilon_rate_dec)
   print("Power Consumption: ", power_consumption(gamma_rate_dec, epsilon_rate_dec))
