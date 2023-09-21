# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping)
   and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL.
   Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

   _I name typically functions start with a verb to indicate that they perform an action. This makes it clear that the function is doing something. I also avoid names that can be easily misinterpreted or have multiple meanings and try not to make the names to long._

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

   _Lists are ordered collections of items and items can be accessed by their indices while dictionaries are unordered collections of key-value pairs Each key is unique and values can be accessed by their keys._

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

   _Yes, you can access any element in the list by specifying its index._

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.).
   What do you think are the pros/cons of a library that can work with any data type?

   _Pros:
   versatility - One of the primary advantages is the ability to work with a wide range of data types, including built-in types like integers and strings, as well as custom data types and user-defined objects.
   Code Reusability - I can reuse the same library for different data types, reducing code duplication and promoting a more modular and maintainable codebase._

   _Cons:
   performance - because the library handles multiple data types, it may take more time to process and optimization is limited.
   complexity - a library works with multiple data types may be harder to maintain, debug, and understand. This complexity can lead to potential bugs and challenges in code readability._

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
   Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

   _Overall, the functions and classes in the requests module are well-named and follow good naming conventions, making it easier for developers to work with the library and understand its functionality._

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

   _resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, adapter_kwargs)_

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?

   _The `**kwargs` argument is a dictionary that collects all the keyword arguments that are not explicitly defined in the function signature. It allows a function to accept an arbitrary number of keyword arguments without specifying them explicitly in the function signature. However, debugging code that uses `**kwargs` can be more challenging because you may not know which keyword arguments were passed or what their values are without inspecting the function implementation._

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text.
   Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

   _Arguments set to `None` means if they are optional and if not provided by the user their default values will be none. Arguments can be set to other values besides `None` as their default values. User can customize the behavior of the function by providing arguments when needed and rely on the predetermined value when they are not._
