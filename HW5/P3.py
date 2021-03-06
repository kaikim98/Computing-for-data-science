"""
**Instruction**
Write P3 function that reads a file and return a list of lines except header(any line starts with '//').
Also exclude new lne character('\n') and any commented part.(marked as '#')
If any line starts with comment mark('#'), ignore the line.

For example, if the input file has below lines, 

//Header: description
//metals no weight
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078 #Good for your health
strontium 38 87.62
barium 56 137.327
# This is comment line and  ignore
radium 88 226


P3 should return below list.
['beryllium 4 9.012', 'magnesium 12 24.305', 'calcium 20 20.078 ', 'strontium 38 87.62', 'barium 56 137.327', 'radium 88 226']

"""
def P3(filename: str) -> list:
    L1 = []
    L2 = []
    L3 = []
    with open(filename, 'r') as lines:
        for line in lines:
            if line[0] == '/' and line[1] == '/' :
                continue
            elif line[0] == '#':
                continue
            else:
                L1.append(line)
    for lines in L1:
        if '#'not in lines:
            L2.append(lines)
        elif '#' in lines:
            a = lines.find('#')
            L2.append(lines[:a])
    for lines in L2:
        a = lines.strip()
        L3.append(a)
    return list(L3)