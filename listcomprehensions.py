# squares of numbers
lst=[i**2 for i in range(1,6)] 
print(lst)

# even numbers
evens=[i for i in range(1,11) if i%2==0]
print(evens)

# odd numbers
odds=[i for i in range(1,11) if i%2!=0]
print(odds)

# square even numbers
result=[i**2 for i in range(1,11) if i%2==0]
print(result)

# even or odd labeling
lables=['even' if i%2==0 else 'odd' for i in range(1,20)]
print(lables)

# uppercase characters 
result=[ch.upper() for ch in "yaswanthi"]
print(result)

# extract vowels
vowels=[ch for ch in "mississippi" if ch in "aeiou"]
print(vowels)

# flatten matrix
matrix=[[1,2],[3,4],[5,6]]
flat=[num for row in matrix for num in row]
print(flat)

# length of words
words=["pthon", "is","awesome"]
lengths=[len(word) for word in words]
print(lengths)