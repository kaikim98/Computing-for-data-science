"""
**Instruction**
Write P5 function that reads a file and write another file as following
- Ignore header(starts with '//').
- If there is any comment mark('#'), remove '#' and move commented parts to the next line
- If there is another comment mark in the commented part, 
  move any parts that follows the second comment to the next line. 
  (i.e. A # B # C becomes three lines)
- If any line starts with comment mark('#'), remove '#' only.
- Assume there is no consecutive '#' in the input file 
  (i.e. '##', '###', ... does not appear in the input file)
- Filenames of input and ouput file are entered as input of P5 function
- There is no return value of P5 function

For example, if the input file has below lines, 

//Header: description
//metals no weight
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078 #Good for your health #Comment in comment
strontium 38 87.62
barium 56 137.327
# This is comment line and  ignore 
radium 88 226


Output file should look as below
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078 
Good for your health 
Comment in comment
strontium 38 87.62
barium 56 137.327
 This is comment line and  ignore
radium 88 226

"""

def P5(input_filename: str, out_filename: str):        
    ##### Write your Code Here ##### 


    ##### End of your code #####
    