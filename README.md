# learn-python
practice stups

# Reducing the number of times the function is called meoization
# high order functions take other functions as arguments, or return them as a results
#pure functions have no side effects, and return a value that depends only on their arguments

#The function map takes a function and an iterable as an arguments, and returns a new iterable with the function applied to each argument

#the function filters an iterable by removing items that don't match a predicate

# sets are similar to list or dictionaraies
# to create empty set use set(), as {} creates an empty dictionaries
# sets are unordered, which means that they can't indexed
#they can not contain duplicate elements
# instead of using appennd to add to a set, use add
#the method remove removes a specific elemnet from a set: pop removes an arbitary element
# The union operator | combines two sets to from a new one containing items in either
# the intersection operator & get items only in both
#the differences operator - gets items in the first set but not in the scond
#the symmetric difference operator ^ gets items in either set, but not both

            ######## when to use a dictionary  #######
    -- when you need a logical association between a key:value pair
    -- when you need fast look up for your data, based on custom key
    -- when your data is being constantly modified. Remember dictionaries are mutable

            ######## When to use the other types  #######
    -- use list if you have a collection of data that does not need random access. 
    -- try to choose list when you need a simple, iterable collection that is modified frequently

    -- use a set if you need uniqueness for the elements

    -- use the tuples when your data cannot change

    #-- many times, a tuples is used in combination with a dictionary, for example
     --, a tuple migth represnt a key, beacuse it's immutable

