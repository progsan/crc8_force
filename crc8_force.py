'''
Подбор контрольной суммы crc8 Dallas iButton перебором указанного байта в index. 
Последовательность задается без контрольной суммы в хвосте.
Перебор выполняется с текущего значения байта в позиции index до совпадения контрольной суммы в etalon_crc.
'''

__author__      = "prog_san"
__version__     = "0.2"
__date__        = "11.03.2025"

''' 
    0x01, 0x53, 0xD4, 0xFE, 0x00, 0x00, 0x00, 0x6F
    
    stream = b'\x01\x53\xD4\xFE\x00\x00\x00'  
    
    index = 3
    etalon_crc = 0x6f
''' 

stream = b'\x01\x53\xD4\x00\x00\x00\x00'

index = 3
etalon_crc = 0x6f

str_no_crc = list(stream)
count = 0

while True:
    crc = 0
    count = count + 1

    for c in str_no_crc:       
        for i in range(0, 8):
            b = (crc ^ (c >> i)) & 1
            crc = (crc ^ (b * 0x118)) >> 1

    if crc == etalon_crc:
        break

    if str_no_crc[index] + 1 == 0x100:
        str_no_crc[index] = 0
    else:
        str_no_crc[index] = str_no_crc[index] + 1

    if str_no_crc[index] == stream[index]:
        break
   
print("CRC8:", hex(crc))

def hex_zero (x: int )-> str:
   return f'0x{x:02x}'

str_no_crc.append(crc)
print(', '.join(map(hex_zero, str_no_crc)))

print("Количество попыток:", count)
print("Нужное значение {0} байта: {1}".format(index, hex(str_no_crc[index])))
