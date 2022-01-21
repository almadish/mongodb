file = open("data/listings.csv", "r", encoding='utf_8')
csv_file = open("data/listings_clean.csv", "w", encoding='utf_8')

s = file.readline()
list_s = s.split(",")

while list_s[0] not in s:
    s = file.readline()

clean_s = ",".join(s.split()) + "\n"
csv_file.write(clean_s)

s = file.readline()
a = file.readline()

while True:
    if s != "":
        if s.split(",")[0].isnumeric() and a.split(",")[0].isnumeric():
            not_clean_lst = s.split()
            clean_s = " ".join(not_clean_lst) + "\n"
            csv_file.write(clean_s)
            s = file.readline()
            a = file.readline()
        else:
            s = file.readline()
            a = file.readline()
            continue
    else:
        break

csv_file.close()

