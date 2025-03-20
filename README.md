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
- lst.remove(11), lst.reverse(), lst = lst*2, a in lst
- n = x.count(y) number of occurrences in list
- common elements in 2 list
set1.interaection(set2)
- list comprehension:
even_squares = [x**2 for x in range (1,11) if x%2==0]
- a tuple is similar to list but immutable
- dictionary represent a group of elements arranged in the form of key value pair
- to delete key value from dict
del dict[`id`]
- x.update({k:v}), x.items()
- two list to dict.  z=zip(x,y)
- procedure oriented programming: the main task is divided into several sub task and each sub task represent as procedure or function.
- object oriented programming: use of class and object in program is oops, A class is a module which itself contains data and methods to achieve the task, main task is divided into several sub task and these are represented as classes 
- features of oops: class and object, encapsulation, abstraction, inheritance, polymorphism
- entire oops methodology has been derived from a single root concept called object, and object is anything that really exist in the world
- behaviour of object represented by attributes and action
- some object may have similar behaviour such object belongs to same category called class
- we can use class as models to creating object
- encapsulation is a mechanism where data (variable) and code (method) that act on the data will bind together.ex class
- both variable and methods are public by default
- abstraction: we can hide the unnecessary data from the user and expose only that data that is interested to the user called abstraction ex car
- variable with double score is private variable ex __y
- to access this, instance.__classname__y
- inheritance: creating new class from existing classes so that the new class will aquire all the features of existing class ex: class B(A):
- polymorphism: polymorphism represent the ability to assume several different forms , in program method exhibiting diff behaviour in different context
- class is a model of blueprint for creating object, class contains variable and methods
- classsname.methodname(),instancename.methodname()
- self refers to current class instance
- constructor is special method that is used to initialize instance variable of a class
- constructor does not create an instant. the duty of the construction is to initialize or Store the beginning value into the instance variables. a constructor called only once.
- types of method: instance method( access method, mutator method), class method, static method
- concept of deriving new classes from the existing class such that the new classes inherit all the members of the existing classes is called inheritance
- already existing class is called super class or base class and newly created class is sub class or derived class
- class subclass(baseclass):
- all the members of the super class are available to the sub class,(variables and methods too)
- writing methods in the sub class with the same name as that of super class methods is called method overloading
- in this case super class methods is not available. only sub class methods is executed always 
- super () is a method that is useful to refer to all members of the super class from a sub class. super().__init__(), super().methods()
- python support single inheritance and multiple inheritance.
- one or more sub class from single base class is called single inheritance.
- deriving sub class from multiple base class is called multiple inheritance
- MRO: starting from current class, searching in parents class in depth first,left to right fashion without searching the same class twice is called method resolution order
- if a variable, object or method exhibits different behaviour in different contexts is called polymorphism.
- python follow duck typing where the type of the object is not checked while invoking the method on the object. any object is accepted as long as that method is found in object
- if any operator perform additional action Other than what it is meant for, it is called operator overloading (more parameters) 
- an abstract method is a method whose actions is redefined in the sub class as per the requirement of the object
- generally an abstract method is written without any body, it is possible to write with body too 
- abstract method with body called concrete method 
- not possible to create an object or instance to an abstract class/ interface 
- every abstract method of abstract class should be derived from ABC class ie available in abc module 
- an abstract class will become an interface when it contains only abstract methods and no concrete method 
- the built in function global()[str] convert the string 'str' into a classname and return the class name
- both abstract classes and interfaces are examples for polymorphism
- error in python: compile time error, runtime error, logical error
- an exception is an error that can be handled by a programmer. if the programmer cannot handle it, then it will not be an exception it will become an error.
- exception occur only at runtime 
- error that occurs at compilation time are not called exceptions. also logical errors cannot come into exception category
- all exception are sub class of base exception class
- all user defined exception should be derived from exception class
- exception handling is done using try except finally else block
- raise statement is use full to raise user defined exception 
- logging module is useful to store exception or error message into log file
- data stored in storage media like hhd cd called file
- python support text file, binary file
- open() method open a file for some operations like writing, reading appending. close () method close the file
- we need not close the file of we open the file using with statement
- encode() method convert the string into byte so that it can be written into a binary file 
- binary string can be converted into ordinary string using decode() method 
- zipping and unzipping of files can be done using zipfile class of zipfile module 
- the os module is useful to perform several operation on directories like finding the currently working directory, changing directory, renaming deleting.
- system() method of os module is useful to run command or execution program from our python program
- regular expression is a string that contains special symbol and character to find and extract the information needed by us from given data
- a data structure represent logical arrangement of elements in memory in a particular model. data structure are also known as abstract data type(ADTs)
- stack, linkedlist, queue are important data structure which are used in most software
- a linked list is a setbof nodes such that each node contains a data field to store data and two link field to refer to the previous node and next node
- insertion, deletion, replacing elements are more important operation in case of linked list
- a stack represent a group of elements arranged in memory in lifo manner 
- push, pop, peep or peek operation in case of stack 
- a queue is a data structure where the first element which enter the queue will come out first called fifo
- in queues elements are added in rear and poped in front 
- deque or double ended queue is a queue where elements can be inserted deleted from both end
- deque is More efficient than normal queue in term of memory and speed 
- a thread represent a separate path of execution of a group of Statements. a thread can be imagined as a light weight process that execute a group of Statements.
- statement of every python program are executed by default thread called Main thread 
- current_thread_().getName() method return the name of the currently running thread 
- executing the task only one at a time is called single tasking. single tasking cannot use the processor time in efficient manner
- executing more than one task at a time is called multitasking. multitasking utilizes the process time in an optimum manner
- two types of multitasking, process-based multitasking and thread-baeed multitasking
- we can create a thread by creating an object to thread class as 
t = Thread(target=functionname, [args=(arg1,args2...)])
- we can create a thread as an instance of sub class to thread class. in this case we have to override the run() method of thread class in the sub class
- when thread is already acting on an object, preventing any other threads from acting on the same object is called thread synchronous or thread safe
- a queue can also be used to achieve efficient thread communication
- when a thread has locked an object and waiting for another object to be realised by another thread, other thread also Waiting for the first thread to release so continue forever waiting called deadlock 