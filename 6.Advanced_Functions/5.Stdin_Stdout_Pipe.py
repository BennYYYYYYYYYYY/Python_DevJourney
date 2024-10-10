import sys

def main():
    contents = sys.stdin.read() # standard input
    new_contents = contents.replace(sys.argv[1], sys.argv[2]) 
    sys.stdout.write(new_contents) # standard output

main()