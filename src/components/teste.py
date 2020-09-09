L = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

B, C = split_list(L)

print (B)
print (C)