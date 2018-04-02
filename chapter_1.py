def URLify (string):
    string = list (string)
    j = None
    for i in xrange (len (string) - 1, 0, -1):
        if (string[i] != ' '):
            if (not j):
                j = len (string) - 1
            string [j] = string [i]
            j -= 1
        else:
            if (j):
                string [j - 2:j + 1] = '%20'
                j -= 3
    return ''.join (string)

def one_away(s1,s2):
    assert (abs(len(s1) - len(s2)) <= 1)
    count = 0
    if (len(s1) > len(s2)):
        count += len(s1) - len(s2)
        for i in xrange(len(s1) - len(s2)):
            if(s1[i] != s2[i]):
                count += 1
            if(count > 1):
                return False
    elif (len(s1) < len(s2)):
        count += len(s2) - len(s1)
        for i in xrange(len(s1)):
            if(s1[i] != s2[i]):
                count += 1
            if(count > 1):
                return False
    else:
        for i in xrange(len(s1)):
            if(s1[i] != s2[i]):
                count += 1
            if(count > 1):
                return False
    return True

def string_compression (string):
    # aabcccccaaa - a2b1c5a3
    # abc - a1b1c1 - abc
    max_length = len(string)
    prev = None
    suffix_count = 0
    result = ''
    for i in string:
        if (i == prev):
            suffix_count += 1
        else:
            if (prev):
                temp = prev + str(suffix_count)
                if (len(result) + len(temp) > max_length):
                    return string
                else:
                    result += temp
                    suffix_count = 0
            suffix_count += 1
            prev = i
    return result + prev + str(suffix_count) if len(result) + len(str(suffix_count)) + 1 < max_length else string

# matrix is a NXN matrix representing pixels of an image.
# Each pixel is 4 bytes. Rotate image by 90 degrees clock wise in place.
def rotate_matrix_clock_wise (matrix):
    result_matrix = []
    for row in reversed(matrix):
        i = 0
        for col in row:
            if (len(result_matrix) == len(matrix)): # all rows of result matrix has been already initialized
                result_matrix[i].append(col)
                i += 1
            else:
                result_matrix.append([col])
    return result_matrix

# matrix is a NXN matrix representing pixels of an image.
# Each pixel is 4 bytes. Rotate image by 90 degrees counter clock wise in place.
def rotate_matrix_counter_clock_wise (matrix):
    result_matrix = []
    for row in matrix:
        i = 0
        for col in reversed(row):
            if (len(result_matrix) == len(matrix)): # all rows of result matrix has been already initialized
                result_matrix[i].append(col)
                i += 1
            else:
                result_matrix.append([col])
    return result_matrix

def zero_matrix_default (matrix):
    r,c = None,None
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[row])):
            if(matrix[row][col] == 0):
                r,c = row, col
                break
            else:
                continue
        else:
            continue
        break
    if(r and c):
        matrix[r] = [0] * len(matrix[r]) #set all elements in the row to zeros
        for row in matrix: # set all elements in col to zeros
            row[c] = 0
    return matrix

def string_rotation(s1,s2):
    assert (len(s1) == len(s2))
    start_index = None
    start_char = s1[0]
    for i in xrange (len(s2)):
        if (s2[i] == start_char):
            start_index = i
            break
    s2 = s2[start_index:] + s2[:start_index]
    return (s2 in s1) #in keyword is equivalent to substring

