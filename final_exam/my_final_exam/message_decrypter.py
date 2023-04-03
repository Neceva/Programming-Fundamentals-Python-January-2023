import re
pattern = r'^(\$([A-Z][a-z]{2,})\$|\%([A-Z][a-z]{2,})\%): (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
n = int(input())
for i in range(n):
    message = input()

    match = re.match(pattern, message)
    if not match:
        print("Valid message not found!")
        continue

    decrypted_groups = []
    for group in match.group(4).split('|'):
        decrypted_group = ''.join(chr(int(num[1:-1])) for num in re.findall(r'\[\d+\]', group))
        decrypted_groups.append(decrypted_group)


    decrypted_message = ''.join(decrypted_groups)
    tag = match.group(2) or match.group(3)
    print(f"{tag}: {decrypted_message}")