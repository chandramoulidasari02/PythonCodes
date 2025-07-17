if __name__ == '__main__':
    # Read from input file
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    
    # Open output file for writing
    with open('output.txt', 'w') as output_file:
        N = int(lines[0])
        result = []
        for i in range(1, N + 1):
            cmd = lines[i].split()
            if cmd[0] == "insert":
                result.insert(int(cmd[1]), int(cmd[2]))
            elif cmd[0] == "print":
                output_file.write(str(result) + '\n')
            elif cmd[0] == "remove":
                result.remove(int(cmd[1]))
            elif cmd[0] == "append":
                result.append(int(cmd[1]))
            elif cmd[0] == "sort":
                result.sort()
            elif cmd[0] == "pop":
                result.pop()
            elif cmd[0] == "reverse":
                result.reverse()
            
            # Write current command to output for debugging
            #output_file.write(f"Executed: {' '.join(result)}\n") #Original requested. Commenting out since it's not part of the problem spec.