myList = [x + 10 for x in [3, 2, 6, 7, 1, 4]];
print(myList);

aList = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]));
print(aList);

someList = [*enumerate([42, 3, 4, 18, 3, 10])];
print(someList);
