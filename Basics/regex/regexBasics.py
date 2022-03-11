import re

mess = "Here are some emails test@tEster.com test@domain.com o@rest.com"
domains = re.findall(r'@(\w*\W*\w*)', mess)

print("Here are your list of Domains: \n");
for x in domains:
    print(x)


