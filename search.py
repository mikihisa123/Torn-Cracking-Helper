import re
from collections import defaultdict
from time import sleep

def openFile():
    with open(r'ignis-1M.txt', 'r', encoding='utf-8') as file:
        ln = file.readlines()
        w_ln = -1
        while(True):
            try:
                w_ln = int(input("Provide word length: "))
                break
            except ValueError:
                print("Please provide valid length as integer")
                continue
        ptrn = r"^"
    return ln,w_ln,ptrn

def runProgram(ptrn, wr_lngth):
    pattern_compile = re.compile(ptrn, re.IGNORECASE)

    # Counter for matching lines
    match_count = 0
    hit_list = []
    letters_combined = [[] for _ in range(wr_lngth)]
    for i, line in enumerate(lines, 1):
        if pattern_compile.search(line):
            found_word = line.strip().upper()
            if found_word not in hit_list:
                hit_list.append(found_word)
                print(f"Line {i}: {found_word}")
                match_count += 1
    for i in hit_list:
        temp_string_list = list(i)
        indexer = 0
        for j in temp_string_list:
            letters_combined[indexer].append(j)
            indexer += 1
                

    for i in range(0, len(letters_combined)):
        output_string = ''
        for j in range(0, len(letters_combined[i])):
            output_string += letters_combined[i][j]
            

    # Display the total number of matching lines
    print(f"Total matching lines: {match_count}")

    column_counts = [defaultdict(int) for _ in range(len(letters_combined))]

    print(70 * "#")
    # Count occurrences of each letter in each column
    for col in range(len(letters_combined)):
        for letter in letters_combined[col]:
            column_counts[col][letter] += 1

    # Calculate percentages
    column_percentages = []
    for col_count in column_counts:
        total_count = sum(col_count.values())
        percentages = {letter: (count / total_count) * 100 for letter, count in col_count.items()}
        sorted_percentages = dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))
        formatted_percentages = {letter: f"{percentage:.2f}%" for letter, percentage in sorted_percentages.items()}
        column_percentages.append(formatted_percentages)

    # Display the results
    for i, percentages in enumerate(column_percentages):
        print(f"Column {i+1}: {percentages}")
        print(70 * "#")
        
def preparePattern(ptrn: list[str]):
    result = r"^"
    result += "".join(ptrn)
    result += "$"
    return result
    
    
lines,word_length,pattern = openFile()
pattern_table = ["" for _ in range(word_length)]

print(70 * "=")
print("Now program will ask you to provide password letter by letter. You can:")
print("Type a letter/number/sign - to provide a valid input from game")
print("Type '.' (dot) - to provide empty input" )
print("Type '!!' - to enter negating mode" )
print(71 * "=")
for i in range(1, word_length+1):
    while(True):  
        letter = input(f"Provide letter for {i} position: ")
        if (len(letter) > 1 and letter != "!!" ):
            print("Please provide only one letter or if you want to negate, use '!!'")
        elif(letter == "!!"):
            while(True):
                negate_letter = input(f"What letters SHOULD NOT BE in position {i}? (to exit type again '!!'): ")
                if (len(negate_letter) > 1 and negate_letter != "!!" ):
                    print("Please provide letter one by one or if you want to exit, use '!!'")
                elif(negate_letter == "!!"):
                    print("moving on...")
                    break
                else:
                    pattern += f"(?!{negate_letter})"
                    pattern_table[i-1] += f"(?!{negate_letter})"
            pattern += "."
            pattern_table[i-1] += "."
            break
        else:
            pattern += letter
            pattern_table[i-1] = letter
            break
pattern += "$"
# print(f"Your pattern: {pattern}")
print(70 * "#")
runProgram(pattern, word_length)
        
while(True):
    print("Do you want to continue checking? type following letter")
    print(">>>> 'q' to quit script")
    print(">>>> 'c' to continue")
    option = input("Provide letter: ")
    if(option.lower() == "c"):
        while(True):
            hit = input(f"which place (range: 1-{word_length}) you typed a letter?:  ")
            try:
                hit_num = int(hit)
                if(hit_num > word_length):
                    raise ValueError
                hit_num -= 1 # getting an index
                while(True):
                    letter_next = input("Provide letter you typed in game:  ")
                    if(len(letter_next) != 1):
                        print("Please provide only one letter!")
                        continue
                    else:
                        while(True):
                            hit_or_nah = input("Was it successful? type 'Y' for Yes and 'N' for No:  ")
                            if(hit_or_nah .lower()== "y"):
                                pattern_table[hit_num] = letter_next
                                break
                            elif(hit_or_nah.lower()=="n"):
                                pattern_table[hit_num] = pattern_table[hit_num].replace(".", f"(?!{letter_next}).", 1)
                                break
                            else:
                                print("Please provide valid input!")
                                continue
                        break
                break
                
            except ValueError:
                print(f"Invalid input! Please provide a number from 1 to {word_length}!")
                continue
        runProgram(preparePattern(pattern_table), word_length)
        continue
    elif(option.lower() == "q"):
        print("Thank you for using the script and have a good day!")
        print("Script created by Mikihisa123")
        print("Have a good day!")
        sleep(2)
        break
    else:
        print("Please provide valid input!!")
        