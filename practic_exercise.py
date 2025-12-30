#Access the data

#isolate each title

#Generate the code

#Display the result

#Pattern Recognition
#"Harry Potter" --> H(index 0) + 12(Total Lenght)
#Title[0] + Length(Title)

file = open("testing.txt", "r")
for line in file:
    title = line.strip()
    first_letter = title[0]
    length = len(title)
    print(f"{first_letter}{length}")

file.close()