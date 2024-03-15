def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return '0'
    hexadecimal = ''
    hex_map = '0123456789ABCDEF'
    while decimal > 0:
        hexadecimal = hex_map[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal

if __name__ == "__main__":
    decimal_input = int(input("請輸入一個介於0到255之間的十進位數字："))
    if decimal_input < 0 or decimal_input > 255:
        print("輸入數字範圍為0-255")
    else:
        binary_result = decimal_to_binary(decimal_input)
        hexadecimal_result = decimal_to_hexadecimal(decimal_input)
        print(f"十進位 {decimal_input} 對應的二進位為: {binary_result}")
        print(f"十進位 {decimal_input} 對應的十六進位為: {hexadecimal_result}")
