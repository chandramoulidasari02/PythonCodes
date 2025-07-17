if __name__ == '__main__':
    # Read from input file
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    
    # Open output file for writing
    with open('output.txt', 'w') as output_file:
        N = int(lines[0].strip())
        requiredList = []
        
        for i in range(1, N + 1):
            command = lines[i].strip().split()
            
            if command[0] == "insert":
                pos = int(command[1])
                val = int(command[2])
                requiredList.insert(pos, val)
            elif command[0] == "print":
                output_file.write(str(requiredList) + '\n')
            elif command[0] == "remove":
                val = int(command[1])
                requiredList.remove(val)
            elif command[0] == "append":
                val = int(command[1])
                requiredList.append(val)
            elif command[0] == "sort":
                requiredList.sort()
            elif command[0] == "pop":
                if len(command) > 1:
                    pos = int(command[1])
                    requiredList.pop(pos)
                else:
                    requiredList.pop()
            elif command[0] == "reverse":
                requiredList.reverse()
            
            # Write current command to output for debugging
            output_file.write(f"Executed: {' '.join(command)}\n")