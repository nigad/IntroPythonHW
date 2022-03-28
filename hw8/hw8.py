## Ayush Nigade
## nigad001

#Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    try:
        file = open(fname)
    except FileNotFoundError:
        return -1

    lines = file.readlines()
    file.close()
    return lines



#Part 2: hw8_index
#==========================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#==========================================
def hw8_index(row1_str):
    try:
        list = row1_str.split(",")
        index = list.index('hw8 Grade')
    except ValueError:
        return -1

    return index

#Part 3: alter_grade
#==========================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#==========================================
def alter_grade(row_str,idx):
    data = row_str.split(",")
    data[idx] = '40'
    return ",".join(data)


#Part 4: haxx
#==========================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):
        rows = get_data_list(fname)
        if rows != -1:
            row = -1
            col = -1

            indx_tmp = hw8_index(rows[0])
            if indx_tmp != -1:
                col = indx_tmp
            else:
                return False

            for i in range(len(rows)):
                row_tmp = rows[i].split(",")
                try:
                    row_tmp.index('Ayush Nigade')
                    row = i
                except ValueError:
                    pass

            rows[row] = alter_grade(rows[row], col)

            file = open(fname, "w")
            for row in rows:
                file.write(row)
            file.close()
            return True

        else:
            return False
