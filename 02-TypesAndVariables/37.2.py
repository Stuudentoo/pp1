personal_data='Mr. John May, born on 1998-02-16'
Description=f'{personal_data}'
Name=personal_data[4:8]
Surname=personal_data[9:12]
Initials=Name[0]+Surname[0]
Born=personal_data[22:33]
print(Description)
print(Name)
print(Surname)
print(Initials)
print(Born)