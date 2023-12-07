import numpy as np

day3_file = open('day3.txt', 'r')
day3_text = day3_file.read()

def set_matrix(text):
    # Split the string into rows based on newline characters
    rows = text.split('\n')

    global n_rows, n_cols, shape
    n_rows = len(rows)
    n_cols = len(rows[0])
    shape = (n_rows,n_cols)
    
    # Create a n x m matrix from the string
    matrix = []
    for row in rows:
        matrix.append(list(row))

    # transform the list into a matrix
    x = np.array(matrix)
    x.reshape(shape)
    
    return x

def create_proximitry_matrix(x):
    # defining the symbols by the inverse logic
    not_symbols = ['1','2','3','4','5','6','7','8','9','0','.']

    # creating the proximitry matrix
    proximitry_matrix = np.empty(shape = shape)
    #loop through rows
    for i in np.arange(x.shape[0]):
        # loop through columns
        for j in np.arange(x.shape[1]):
            if x[i][j] in not_symbols:
                proximitry_matrix[i][j] = 0
            else:
                proximitry_matrix[i][j] = 1
    return proximitry_matrix

def look_neighbours(matrix,row,col):
    include_in_sum = False
    neighbours = []
    n_rows = matrix.shape[0]
    n_cols = matrix.shape[1]
    
    for i in range(max(0, row - 1), min(n_rows, row + 2)):
        for j in range(max(0, col - 1), min(n_cols, col + 2)):
            # check if the cell is not itsef
            if i != row or j != col:
                neighbours.append(matrix[i][j])
    if 1 in neighbours:
        include_in_sum = True
        
    return include_in_sum

def find_number_at_position(string, position):
    number = ''
    
    # Forward check from the specified position
    i = position
    while i < len(string) and string[i].isdigit():
        number += string[i]
        i += 1
    
    # Backward check before the specified position
    i = position - 1
    while i >= 0 and string[i].isdigit():
        number = string[i] + number
        i -= 1
    
    return number

def list_cleaner(x):
    clean_list = []
    for i, item in enumerate(x):
        clean_list.append(item)
        if item == x[i+1]:
            x.remove(x[i+1])
    return clean_list


engine_schematic = []
#
x = set_matrix(day3_text)
proximitry_matrix = create_proximitry_matrix(x)

#loop through rows
for i in np.arange(x.shape[0]):
    # loop through columns
    for j in np.arange(x.shape[1]):
        if x[i][j].isnumeric():
            if look_neighbours(proximitry_matrix,i,j) == True:
                engine_schematic.append(find_number_at_position(x[i],j))
                
engine_schematic = list_cleaner(engine_schematic)
p1_result = sum(map(int, engine_schematic))
print(p1_result)
