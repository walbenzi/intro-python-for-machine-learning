from pprint import pprint
# Part 1: Lists, Loops, and aggregating

# * Create a list with 5 numbers in it and assign it to a variable.
a_list = [5, 12, 0, 54, -1]
# * Create a variable called `list_sum` and assign it the value `0`
list_sum = 0
# * Using a for loop, the `list_sum` variable and the `+=` operator, compute
# the sum of the values in your list.
for item in a_list:
    list_sum += item
# * Using the `len` function, `list_sum`, and the `/` operator, compute the
# average of the values in your list and store it into a variable.
list_average = list_sum / len(a_list)
# * Using another loop and an if statement inside the loop print all the
# values in your list that are less than the average.
for item in a_list:
    if item < list_average:
        print(item)

# Part 2: Nested Data
# Often times data is provided in strange, and sometimes deeply nested formats.
# Lists inside of lists, lists inside of dictionaries,
# dictionaries inside of dictionaries... and so on. Examining and understanding
# this kind of data is a skill programmers have to use
# frequently... Lets practice. Copy this python code into a new script:

dictionary_challenge = {
    'key': 'value',
    'hello': 'world',
    'target': [
        {
            'this_is': 'getting',
            'sort': 'of',
            'tricky': [
                'Hello Earth',
                'Hello Detroit',
                'Hello World!'
            ]
        },
        {
            'too': 'far'
        }
    ]
}

# * Using bracket notation to select each of the follow values from the above
# data structure and then print them to check your work:
#     * `'world'`
print(dictionary_challenge.get("hello"))
#     * `'far'`
print(dictionary_challenge["target"][1]["too"])
#     * `'Hello World!'`
print(dictionary_challenge["target"][0]["tricky"][2])


# * Now, instead of simply printing the values, modify them!
#     * Replace `'world'` with `'friends'`
dictionary_challenge["hello"] = "friends"
#     * Replace `'far'` with `'cool'`
dictionary_challenge["target"][1]["too"] = "cool"
#     * Replace `'Hello World!'` with `'So long and thanks for all the fish'`
dictionary_challenge["target"][0]["tricky"][2] = \
    'So long and thanks for all the fish'


#     * Then, print the entire data structure to check your work.
print(dictionary_challenge)
# Pro-tip, use the following code to "pretty print" the dictionary instead of
# the standard print:
pprint(dictionary_challenge)
