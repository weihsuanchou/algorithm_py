#solution: Use a dictionary to store all possible sums (from all numbers with + or -)
#and ++ the sum as the way to get to each sum

class solution:
    def decode(self, code: str) -> str:
        if len(code) == 0: return ""

        stack = [ ['', 1] ] 
        numberText = ''
        
        print(code)
        for c in code:
            if c.isdigit():
                numberText += c
            elif c is '[':
                #numberText collect finished
                stack.append( ['', int(numberText)])
                numberText = ''
            elif c.isalpha():
                #append this c to current stack top
                stack[-1][0] = stack[-1][0]  + c
            elif c is ']':
                #one group is formed, resolve
                text, times = stack.pop()
                stack[-1][0] += text * times
       
        return stack[0][0]
 
    
def main():
    print( "hello Doctor! Decode String") 
    print(solution().decode("3[a]2[bc]"))
    print(solution().decode("3[a2[c]]"))
    print(solution().decode("2[abc]3[cd]ef"))


if __name__ == "__main__":
    main()