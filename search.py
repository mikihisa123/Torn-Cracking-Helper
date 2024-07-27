import re
from collections import defaultdict
with open(r'ignis-1M.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    word_length = int(input("Provide word length: "))
    pattern = r"^"
    print(71 * "=")
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
                        print("Please provide only one letter or if you want to negate, use '!!'")
                    elif(negate_letter == "!!"):
                        print("moving on...")
                        break
                    else:
                        pattern += f"(?!{negate_letter})"
                pattern += "."
                break
            else:
                pattern += letter
                break
    pattern += "$"
    print(f"Your pattern: {pattern}")
    print(70 * "#")


    pattern_compile = re.compile(pattern, re.IGNORECASE)
    # Match 'J', any character, 'N', any character, with word boundaries

    # Counter for matching lines
    match_count = 0
    hit_list = []
    letters_combined = [[] for _ in range(word_length)]
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
# Step 2: Count occurrences of each letter in each column
for col in range(len(letters_combined)):
    for letter in letters_combined[col]:
        column_counts[col][letter] += 1

# Step 3: Calculate percentages
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