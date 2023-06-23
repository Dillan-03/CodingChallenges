def print_formatted(number):
    pad = number.bit_length()
    for i in range(1, n+1):
        decimal = i
        octal = oct(i)[2:]#excluding the prefixes
        hexadecimal = hex(i)[2:] 
        binary = bin(i)[2:]
        print(str(decimal).rjust(pad),
              str(octal).rjust(pad),
              str(hexadecimal).upper().rjust(pad),
              str(binary))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)