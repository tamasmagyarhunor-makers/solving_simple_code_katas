# Build a small program that turns a fullname into its initials
# eg. make_initials("Will Smith") #=> 'W.S'
# note: we don't deal with edge cases now, such as more than 
# one first and last name

# Parameters
#    - fullname, a string (eg. "Xiao Chan")
# Returns
#    - string (eg. 'X.C')
# Side effects
#    - None
def make_initials(fullname):
    # return (fullname.split()[0][0] + "." + fullname.split()[1][0]).upper()

    names = fullname.split(" ")
    
    first = names[0]
    last = names[1]

    first_first_letter = first[0]
    last_first_letter = last[0]

    return (first_first_letter + "." + last_first_letter).upper()

# Tasks
# 1. split the fullname #DONE
# 2. identify/pick the different names (first, last) #DONE
# 3. extract first letters of the names #DONE
# 4. # - concatenate the final letters with 
# a dot '.' in between #DONE
# 5. upcase the entire string and return it. #DONE

print(make_initials('Will Smith'))
print(make_initials("hunor coach"))