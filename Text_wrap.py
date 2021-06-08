import textwrap

def wrap(string, max_width):
    new_string = ""
    while len(string):
        new_string += string[:max_width] +"\n"
        string = string[max_width:]
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
	
	
	

#second solution by me
	
import textwrap

def wrap(string, max_width):
    
    k = textwrap.fill(string,max_width)
    
    return k

if __name__ == '__main__':




#textwrap will always take the max width as long as there is sufficient characters to take the next group in the next word. Or within
#same word until we reach the end.