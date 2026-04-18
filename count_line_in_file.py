def count_line(filename):
    
    with open(filename , "r") as f :
        lines = f.readlines()
        return len(lines)

print(count_line("demo.json"))    