
with open('Names/invited_names.txt', 'r') as f:
    # readlines with \n at the end
    names = f.readlines()

# print(mails)

with open('Letters/mail.txt', 'r') as f:
    letter = f.read()

for name in names:
    name = name.strip()  
    new_letter = letter.replace('[name]', name)
    
    with open(f'Ready/{name}.txt', 'w') as f:
        f.write(new_letter)
