def Text_To_Binary(text):
    binary = ''.join(format(ord(i), 'b') for i in text)
    return binary

def Binary_To_Text(binary):
    str_data = ""


    for i in range(0, len(binary), 7): 
        temp_data = int(binary[i:i + 7]) 
        decimal, i, n = 0, 0, 0
        while(temp_data != 0): 
            dec = temp_data % 10
            decimal = decimal + dec * pow(2, i) 
            temp_data = temp_data//10
            i += 1
        decimal_data = decimal
        str_data = str_data + chr(decimal_data)
    return str_data
