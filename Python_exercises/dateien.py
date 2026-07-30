# Using with resource as name: starts a context manager and the file is always closed at the end of the block. 
# The resource is initialized and is 
# available in that block.
# In case there are anx exceptions, the resrouce is correctly finalized so you don't need a try block.
# with open (filename) as f:
    # initialize
    # for line in f:
    #    pass
        #process this line

# Example 1
def fgrep(subject: str, filename: str):
    with open(filename) as f:
        for line in f:
            if subject in line:
                print(line)

# EXample 2 where the result is printed to a new file
def fgrep2(subject: str, infile: str, outfile: str):
    with open(infile) as fin, open(outfile, "w") as fout:
        for line in fin:
            if subject in line:
                print(line, file=fout)