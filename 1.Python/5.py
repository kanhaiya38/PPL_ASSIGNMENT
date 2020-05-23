"""
    5. Find a missing page number from given page number list of a 25-page book
"""

input_str = input("Enter page numbers present in the book ")

# input_str = "2,4-6,7-9,12,16,17,20,21"

input_list = input_str.split(",")
final_list = []
for i in input_list:
    if '-' in i:
        start, end = i.split('-')[0], i.split('-')[1]
        print(start, end)
        final_list += [int(i) for i in range(int(start), int(end) + 1)]
    else:
        final_list.append(int(i))

print("Missing numbers are:")
for i in range(1, 26):
    if i not in final_list:
        print(i, end=", ")
