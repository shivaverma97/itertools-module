import itertools
import operator


# COUNT function

counter = itertools.count(start=3, step=2)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


data = [100,200,300,400]
data_combo = zip(itertools.count(start=4, step=4),data)      #for 0,1,2,3 use count() only
                                                             # step can be negative also
# for item in data_combo:
#     print(item)

data_combo = list(zip(itertools.count(start=4, step=4),data))  # this will generate a list of zip
# print(data_combo)

data_combo = list(zip(itertools.zip_longest(range(10), data)))  #this will run till range and allocate none after data set get exhausted
# print(data_combo)



# CYCLE function

counter = itertools.cycle(data)           # it will restart after getting exhausting, loops will lead to infinte loop
counter_2 = itertools.cycle(['on','off'])
# print(next(counter_2))
# print(next(counter_2))
# print(next(counter_2))
# print(next(counter_2))
# print(next(counter_2))



# REPEAT function

counter = itertools.repeat(2, times=3)   #if times is not mentioned it will lead to infinity

# for item in counter:
#     print(item)

squares = map(pow, range(10), itertools.repeat(2))    #map will return the result of pow fucntion with passed args
# for item in squares:
#     print(item)
# print(list(squares))




# STAR MAP

squares = itertools.starmap(operator.add, [(0,1),(1,2),(3,4)])  # works same as map function, istead of pow example of corey, we used operator.add() func 
# print(list(squares))




# COMBINATION and PERMUTAION

numbers = [1,2,3,4,5]
alphabets = ['a','b','c','d']
names = ['shiva','ayushi','rajesh','lalita']

# for combined result of above 3 lists, there are 2 methods, first is we make a new list by adding all and second is using CHAIN
combined = numbers + alphabets + names
# print(combined)

combined = itertools.chain(numbers,alphabets,names)           # this will combine all three lists in a single list
# for item in combined:
#     print(item)


combination = itertools.combinations(alphabets,3)     # alphabet data set will be used and 3 is used for pair of 3 combination for each result
combination = itertools.combinations_with_replacement(numbers,4)   # this will generate result for taking same values also, for example '1' is printed multiple times
# for item in combination:
#     print(item)



permutation = itertools.permutations(names,2)         # here same as combination but uniqueness wont be here for orders, 
                                                      #here order matters and thats why result will show 2 same values for diff orders
# for item in permutation:
#     print(item)



# PRODUCT

product = itertools.product(alphabets, repeat=3)     # this will generate result for taking same values also, for example 'a' is printed multiple times
# for item in product:
#     print(item)



# ISLICE
slice_example = [0,1,2,3,4,5,6,7,8,9]
slice_list = itertools.islice(slice_example,3,8,2)         # it will slice the list according to the given args, first is iterable item, then start index point, stop point and skip value

# for element in slice_list:
#     print(element)



# COMPRESS
selectors = [True, False, True, True]
values = ['a','b','c','d']

True_values = itertools.compress(values, selectors)      # it will combine values with selectors and return those values only that are true

# for true in True_values:
#     print(true)



#FILTER

def less_than_2(n):
    if n<2:
        return True
    return False

numbers = [1,2,3,4,5,6,7]

result = filter(less_than_2, numbers)                            # returns true value only
# result = itertools.filterfalse(less_than_2, numbers)             # returns false values
# result = itertools.dropwhile(less_than_2, numbers)               # return values untill hit a particular value and then returns all after hitting
# result = itertools.takewhile(less_than_2, numbers)               # returns value untill hit a particular value

# for ans in result:
#     print(ans)




# ACCUMULATE

result = itertools.accumulate(numbers)                    # gives addition by default
result = itertools.accumulate(numbers, operator.mul)      # now the operator is also passed, so it will now give the multiplication of all

# for ans in result:
#     print(ans)




# GROUP BY


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get_state(person):
    return person['state']

person_group = itertools.groupby(people, get_state)

# for key, value in person_group:
#     print(key)
#     for person in value:
#         print(person)




 
# TEE- if we want to make two iterables for one item then we can use this

copy_1, copy_2 = itertools.tee(person_group)        #this will replicate two iterables of one that is person_group