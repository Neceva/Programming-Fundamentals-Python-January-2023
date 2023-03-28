import re

valid_urls = []
pattern = r'((w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'

text = input()
while text:
    matches = re.search(pattern, text)
    if matches:
        valid_urls.append(matches.group(0))
    text = input()
print(*valid_urls, sep="\n")