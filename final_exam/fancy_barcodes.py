import re

count_barcodes = int(input())
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
digit = ""
for i in range(count_barcodes):
    barcode = input()

    match = re.search(pattern, barcode)
    if match:
        product = match.group(1)
        for el in product:
            if el.isdigit():
                digit += el
        if digit == "":
            digit = "00"

        print(f'Product group: {digit}')
        digit = ""
    else:
        print("Invalid barcode")
