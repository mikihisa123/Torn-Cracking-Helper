# Torn Cracking Helper

This is simple script to help you with cracking crime
just run it in your console (using ./search.py) and
you will be prompted with simple instructions:

1.  Provide word length you want to crack in torn
2.  Provide letter by letter password using this semantic:
    - type letter for letter known/cracked/guessed
    - type . if there is empty space
    - type !! if you want to provide letter that should not
      be seen
3.  You will be provided with matching words + letters statistics
4.  Pick a letter that has the highest statistic for the place

Good luck!

## Example:

You want to crack password: J \_ _ G _ E;

1. run script
2. provide amount of letters: 6
3. Start typing letter by letter:

   - J
   - .
   - .
   - G
   - .
   - E

4. you will be provided statistics.

If you tried to guess for the second place I and in TORN
it shows that it's incorrect, you should re-run the script
and provide such input (also, letter by letter)

- J
- !! (to start typing letters to not be counted for search)
- I
- !! (to exit this mode)
- .
- G
- .
- E

## DISCLAIMER:

This script is using Ignis - 1M list of passwords
That can be found here:
https://github.com/ignis-sec/Pwdb-Public/blob/master/wordlists/ignis-1M.txt

There is no proof which list TORN is using, but having the script work faster
than searching within 10M records can be bneneficial for you
