# Assuming that the input string is a Unicode string
def allUniqueChars(s: str) -> bool:
    dict = {}
    s = "".join(s.split())
    for i in s:
        if i in dict:
            return False
        dict[i] = True
    return True 
    
def main():
    input = "This is my sample input"
    #input2 = "uniq "
    output = allUniqueChars(input)
    print("Are all the characters in the input string unique? " + str(output))

if __name__ == "__main__":
    main()
