# Python summary

- Python was developed by Guido Van Rossum 1991, python combines features of c and Java.
- Feature: Simple, Easy to learn, Open Source, High-Level Language, Platform independent, Procedure and object oriented.
- A class is a blueprint for declaring and creating objects. An object is a class instance that allows programmers to use variables and methods from inside the class.
- A class does not exist physically, A class is only an abstract idea that represent the common behavior of several objects, this imaginary picture is called a class. ex-dog class(variable: height, age,color. method: barking, eating,  running)
- A scripting language is a programming language that does not use a compiler for execution of the source code. it uses an interpreter to translate the source code into machine code on the fly(while running)
- source code ->(compiler)-> byte code(set of instruction) ->(PVM/interpeter)-> machine code(binary) -> computer
- JIT just in time, PVM python virtual machine, JIT is faster than the interpreter(line by line).
- Everything is considered an object in Python. even modules are also objects.
- memory allocation and deallocation are done during runtime automatically, all these objects are stored on a separate memory called heap.
- a variable is seen as a tag or name that is tied to some value,(a=1) which means the value '1' is created first in memory and then a tag by the name 'a'.
- DataType: None type, boolean, Numeric(int, float, complex), Sequences(str, bytes,list, tuple, range), Sets(set, frozen set), Mapping(dict).
- None type object does not contain any value, 'None' is used inside the function as the default value.
- the list[] can store diff types of elements and can grow dynamically in memory.
- tuple () elements can not be modified and the set {} is an unordered collection of elements and does not allow duplicate values.
- Operators: Arithmetic(+ _ * / % **), Assignment(= += -= *= /= %= **= //=), unary(-), Relational(> >= < <= == !=), Logical(and or not), Boolean(true and true = true, False or false = false), Bitwise, Membership(in not in), Identity(Is is not).
- an operator is a symbol that performs an operation and acts on some variables called operands.
- math function: sqrt, ceil, floor factorial, pow, gcd
- a,b = [int (x) for x in input ("enter two number").split(',')
- control statement: if, if else, if elif else, while loop, for loop, else suite, break, continue,pass, assert, return.
- the group of statement in python is called suite.
- synatx: assert expression, message 
- array use less memory than lists and they offer faster execution than list.
- import array, a = array.array('i',[5,6,7])
- array methods: append,count, extend, index, pop, remove.
- numpy is package that contains serveral classes, functions, variable etc to deal with scientific calculation in python.
- vectorized operation: dividing or adding of 2 arrays called vectorized operation, these are fast, syntactically clear, compact code.
- math operation on arrays: sum, prod,min,max,mean,sort.
- any () function can be used to determine if any one element of the array is true.
- all() function can be used to determine whether all elements in the array are true.
- c = where (a>b , a , b)
- ndim attribute represent number of dimensions in an array ex: arre.ndim
- shape attribute , size attribute, dtype
- reshape method is use full to change the shape of an array.ex: arr.reshape(2,5)
- flatten () method is useful to return a copy of array collapsed into one dimension.
- a 2d array is also considered as a Matrix.
- onces() ex: a=onces((3,4), float), zeroes () ex: b=zeros ((3,4), int)
- eyes() function create 2d array and fills elements in the diagonal with 1s ex: a=eye(3)
- reshape: b = reshape (a, (2,3))
- Matrix represent a rectangular array of elements arranged in a row and column ex: a=Matrix([[1,2,3][4,5,6]]) or b= Matrix ("1 2; 3 4; 5 6")
- m = Matrix( arange (12).reshape(3,4)
- diagonal Matrix d=diagonal(mat),m = sort(mat), mat.max(), mat.min(), mat.sum(), mat.min()
- number, string,tuples are immutable. list, set, dictionary are mutable object.
- functions represent reusable code
- a function that calls itself is known as recursive function, it is useful solve complex program
- a function without a name is called anonymous or lamda function
- lambda function generally used with filter, map, reduce
- filter function is useful to extract elements from a sequence depending on the result of functions
- map function is useful to perform some operations on each element of sequence depending on function
- reduce function reduce a sequence of elements to a single value by processing the elements according to function supplied 
- a decorators is function that accept a function as parameter and return a function. decorator are useful to perform some additional processing required by function
- a generator is a function that return a sequence of value or elements to return elements from a generator we have to use yield statement
- "__name__" indicate whether the program is run as an individual program or as a module
- list is similar to an array, but it can store different types of elements
- lst = list(range(4,9,2)
- lists are mutable, means we can modify the content of list.
- 