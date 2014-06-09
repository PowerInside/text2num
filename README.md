Replaces numbers in a string to their corresponding numerical format. The [Western decimal numeral system](http://en.wikipedia.org/wiki/English-language_numerals) is used by default.

Examples
========

### Basic Usage

    from text2num import text2num
    print text2num("It costs thousand FIVE hundred dollars") # "It costs 1500 dollars"
    
### Custom number systems

Populate the `numwords` object as shown below. (The below example is for Indian number system)

    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "lakh", "crore"]

    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):    numwords[word] = (1, idx)
    for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
    
    numwords["hundred"] = (10**2,0)
    numwords["thousand"] = (10**3,0)
    numwords["lakh"] = (10**5,0)
    numwords["crore"] = (10**7,0)
    
Pass the `numwords` object into the second argument of text2num function.

    from textnum import text2num
    print text2num("one lakh prize money", numwords) # 100000 prize money

TODO
====

  * Support fractional decimal numericals.

Credits
=======
This is a derivative work from a [code snippet](http://stackoverflow.com/a/493788/679829) on stackoverflow by the user "[recursive](http://stackoverflow.com/users/44743/recursive)".
