
# Many programming languages have a special function that is automatically executed when an operating system starts to run a program.
# This function is usually called main() and must have a specific return type and arguments according to the language standard. 
# On the other hand, the Python interpreter executes scripts starting at the top of the file, and there is no specific function that
# Python automatically executes. Nevertheless, having a defined starting point for the execution of a program is useful for understanding
# how a program works. Python programmers have come up with several conventions to define this starting point.
# A Basic Python main(). In some Python scripts, you may see a function definition and a conditional statement that looks like the example below:

# def main():
#     print("Hello World!")

# if __name__ == "__main__":
#     main()
# # In this code, there is a function called main() that prints the phrase Hello World! when the Python interpreter executes it. 
# # There is also a conditional (or if) statement that checks the value of __name__ and compares it to the string "__main__". 
# # When the if statement evaluates to True, the Python interpreter executes main(). You can read more about conditional statements in Conditional Statements in Python.
# print("This is my file to test Python's execution methods.")
# print("The variable __name__ tells me which context this file is running in.")
# print("The value of __name__ is:", repr(__name__))




# Remember that, in Python, there is no difference between strings defined with single quotes (') and double quotes ("). You can read more about defining strings in Basic Data Types in Python.
# You will find identical output if you include a shebang line in your script and execute it directly (./execution_methods.py), or use the %run magic in IPython or Jupyter Notebooks.
# You may also see Python scripts executed from within packages by adding the -m argument to the command. Most often, you will see this recommended when you’re using pip: python3 -m pip install package_name.
# Adding the -m argument runs the code in the __main__.py module of a package. You can find more information about the __main__.py file in How to Publish an Open-Source Python Package to PyPI.
# In all three of these cases, __name__ has the same value: the string '__main__'.
# Technical detail: The Python documentation defines specifically when __name__ will have the value '__main__':
# A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt. (Source)
# __name__ is stored in the global namespace of the module along with the __doc__, __package__, and other attributes. You can read more about these attributes in the Python Data Model documentation and, specifically for modules and packages, in the Python Import documentation.

# Importing Into a Module or the Interactive Interpreter
# Now let’s take a look at the second way that the Python interpreter will execute your code: imports. When you are developing a module or script, you will most likely want to take advantage of modules that someone else has already built, which you can do with the import keyword.
# During the import process, Python executes the statements defined in the specified module (but only the first time you import a module). To demonstrate the results of importing your execution_methods.py file, start the interactive Python interpreter and then import your execution_methods.py file:

# This is my file to test Python's execution methods.
# The variable __name__ tells me which context this file is running in.
# The value of __name__ is: 'execution_methods'
# In this code output, you can see that the Python interpreter executes the three calls to print(). The first two lines of output are exactly the same as when you executed the file as a script on the command line because there are no variables in either of the first two lines. However, there is a difference in the output from the third print().

# When the Python interpreter imports code, the value of __name__ is set to be the same as the name of the module that is being imported. You can see this in the third line of output above. __name__ has the value 'execution_methods', which is the name of the .py file that Python is importing from.
# Note that if you import the module again without quitting Python, there will be no output.
# Note: For more information on how importing works in Python, check out the official documentation as well as Absolute vs Relative Imports in Python.
# Best Practices for Python Main Functions
# Now that you can see the differences in how Python handles its different execution modes, it’s useful for you to know some best practices to use. These will apply whenever you want to write code that you can run as a script and import in another module or an interactive session.
# You will learn about four best practices to make sure that your code can serve a dual purpose:
# Put most code into a function or class.
# Use __name__ to control execution of your code.
# Create a function called main() to contain the code you want to run.
# Call other functions from main().
#  ut Most Code Into a Function or Class
# Remember that the Python interpreter executes all the code in a module when it imports the module. Sometimes the code you write will have side effects that you want the user to control, such as:
# Running a computation that takes a long time
# Writing to a file on the disk
# Printing information that would clutter the user’s terminal
# In these cases, you want the user to control triggering the execution of this code, rather than letting the Python interpreter execute the code when it imports your module.

# Therefore, the best practice is to include most code inside a function or a class. This is because when the Python interpreter encounters the def or class keywords, it only stores those definitions for later use and doesn’t actually execute them until you tell it to.
# Save the code below to a file called best_practices.py to demonstrate this idea:

# from time import sleep

# print("This is my file to demonstrate best practices.")
# def process_data(data):
#     print("Beginning data processing...")
#     modified_data = data + " that has been modified"
#     sleep(3)
#     print("Data processing finished.")
#     return modified_data
#In this code, you first import sleep() from the time module.
#sleep() pauses the interpreter for however many seconds you give as an argument and will produce a function that takes a long time to run for this example. Next, you use print() to print a sentence describing the purpose of this code.
#Then, you define a function called process_data() that does five things:
# Prints some output to tell the user that the data processing is starting
# Modifies the input data
# Pauses the execution for three seconds using sleep()
# Prints some output to tell the user that the processing is finished
# Returns the modified data
# Execute the Best Practices File on the Command Line
# Now, what will happen when you execute this file as a script on the command line?
# The Python interpreter will execute the from time import sleep and print() lines that are outside the function definition, then it will create the definition of the function called process_data(). Then, the script will exit without doing anything further, because the script does not have any code that executes process_data().
# The code block below shows the result of running this file as a script:
# $ python3 best_practices.py
# This is my file to demonstrate best practices.
# The output that we can see here is the result of the first print(). Notice that importing from time and defining process_data() produce no output. Specifically, the outputs of the calls to print() that are inside the definition of process_data() are not printed!
# Import the Best Practices File in Another Module or the Interactive Interpreter
# When you import this file in an interactive session (or another module), the Python interpreter will perform exactly the same steps as when it executes file as a script.
# Once the Python interpreter imports the file, you can use any variables, classes, or functions defined in the module you’ve imported. To demonstrate this, we will use the interactive Python interpreter. Start the interactive interpreter and then type import best_practices:
# >>> import best_practices
# This is my file to demonstrate best practices.
# The only output from importing the best_practices.py file is from the first print() call defined outside process_data(). Importing from time and defining process_data() produce no output, just like when you executed the code from the command line.

# Use if __name__ == "main" to Control the Execution of Your Code
# What if you want process_data() to execute when you run the script from the command line but not when the Python interpreter imports the file?

# You can use the if __name__ == "main" idiom to determine the execution context and conditionally run process_data() only when __name__ is equal to "__main__". Add the code below to the bottom of your best_practices.py file:

# if __name__ == "__main__":
#     data = "My data read from the Web"
#     print(data)
#     modified_data = process_data(data)
#     print(modified_data)
# In this code, you’ve added a conditional statement that checks the value of __name__. This conditional will evaluate to True when __name__ is equal to the string "__main__". Remember that the special value of "__main__" for the __name__ variable means the Python interpreter is executing your script and not importing it.

# Inside the conditional block, you have added four lines of code (lines 12, 13, 14, and 15):

# Lines 12 and 13: You are creating a variable data that stores the data you’ve acquired from the Web and printing it.
# Line 14: You are processing the data.
# Line 15: You are printing the modified data.
# Now, run your best_practices.py script from the command line to see how the output will change:

# $ python3 best_practices.py
# This is my file to demonstrate best practices.
# My data read from the Web
# Beginning data processing...
# Data processing finished.
# My data read from the Web that has been modified
# First, the output shows the result of the print() call outside of process_data().
# After that, the value of data is printed. This happened because the variable __name__ has the value "__main__" when the Python interpreter executes the file as a script, so the conditional statement evaluated to True.
# Next, your script called process_data() and passed data in for modification. When process_data() executes, it prints some status messages to the output. Finally, the value of modified_data is printed.
# Now you should check what happens when you import the best_practices.py file from the interactive interpreter (or another module). The example below demonstrates this situation:
# >>> import best_practices
# This is my file to demonstrate best practices.
# Notice that you get the same behavior as before you added the conditional statement to the end of the file! This is because the __name__ variable had the value "best_practices", so Python did not execute the code inside the block, including process_data(), because the conditional statement evaluated to False.
# Create a Function Called main() to Contain the Code You Want to Run
# Now you are able to write Python code that can be run from the command line as a script and imported without unwanted side effects. Next, you are going to learn about how to write your code to make it easy for other Python programmers to follow what you mean.
# Many languages, such as C, C++, Java, and several others, define a special function that must be called main() that the operating system automatically calls when it executes the compiled program. This function is often called the entry point because it is where execution enters the program.
# By contrast, Python does not have a special function that serves as the entry point to a script. You can actually give the entry point function in a Python script any name you want!
# Although Python does not assign any significance to a function named main(), the best practice is to name the entry point function main() anyways. That way, any other programmers who read your script immediately know that this function is the starting point of the code that accomplishes the primary task of the script.
# In addition, main() should contain any code that you want to run when the Python interpreter executes the file. This is better than putting the code directly into the conditional block because a user can reuse main()if they import your module.

# Change the best_practices.py file so that it looks like the code below:
# from time import sleep
# print("This is my file to demonstrate best practices.")
# def process_data(data):
#     print("Beginning data processing...")
#     modified_data = data + " that has been modified"
#     sleep(3)
#     print("Data processing finished.")
#     return modified_data

# def main():
#     data = "My data read from the Web"
#     print(data)
#     modified_data = process_data(data)
#     print(modified_data)

# if __name__ == "__main__":
#     main()
# In this example, you added the definition of main() that includes the code that was previously inside the conditional block. Then, you changed the conditional block so that it executes main(). If you run this code as a script or import it, you will get the same output as in the previous section.
# Call Other Functions From main()
# Another common practice in Python is to have main() execute other functions, rather than including the task-accomplishing code in main(). This is especially useful when you can compose your overall task from several smaller sub-tasks that can execute independently.
# For example, you may have a script that does the following:
# Reads a data file from a source that could be a database, a file on the disk, or a web API
# Processes the data
# Writes the processed data to another location
# If you implement each of these sub-tasks in separate functions, then it is easy for a you (or another user) to re-use a few of the steps and ignore the ones you don’t want. Then you can create a default workflow in main(), and you can have the best of both worlds.
# Whether to apply this practice to your code is a judgment call on your part. Splitting the work into several functions makes reuse easier but increases the difficulty for someone else trying to interpret your code because they have to follow several jumps in the flow of the program.
# Modify your best_practices.py file so that it looks like the code below:
from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
# In this example code, the first 10 lines of the file have the same content that they had before. The second function definition on line 12 creates and returns some sample data, and the third function definition on line 17 simulates writing the modified data to a database.
# On line 21, main() is defined. In this example, you have modified main() so that it calls the data reading, data processing, and data writing functions in turn.
# First, the data is created from read_data_from_web(). This data is passed to process_data(), which returns the modified_data. Finally, modified_data is passed into write_data_to_database().
# The last two lines of the script are the conditional block that checks __name__ and runs main() if the if statement is True.
# Now, you can run the whole processing pipeline from the command line, as shown below:
# $ python3 best_practices.py
# This is my file to demonstrate best practices.
# Reading data from the Web
# Beginning data processing...
# Data processing finished.
# Writing processed data to a database
# Data from the web that has been modified
# In the output from this execution, you can see that the Python interpreter executed main(), which executed read_data_from_web(), process_data(), and write_data_to_database(). However, you can also import the best_practices.py file and re-use process_data() for a different input data source, as shown below:
# >>> import best_practices as bp
# This is my file to demonstrate best practices.
# >>> data = "Data from a file"
# >>> modified_data = bp.process_data(data)
# Beginning data processing...
# Data processing finished.
# >>> bp.write_data_to_database(modified_data)
# Writing processed data to a database
# Data from a file that has been modified
# In this example, you imported best_practices and shortened the name to bp for this code.
# The import process caused the Python interpreter to execute all of the lines of code in the best_practices.py file, so the output shows the line explaining the purpose of the file.
# Then, you stored data from a file in data instead of reading the data from the Web. Then, you reused process_data()and write_data_to_database() from the best_practices.py file. In this case, you took advantage of reusing your code instead of defining all of the logic in main().
# Summary of Python Main Function Best Practices
# Here are four key best practices about main() in Python that you just saw:
# Put code that takes a long time to run or has other effects on the computer in a function or class, so you can control exactly when that code is executed.
# Use the different values of __name__ to determine the context and change the behavior of your code with a conditional statement.

# You should name your entry point function main() in order to communicate the intention of the function, even though Python does not assign any special significance to a function named main().
# If you want to reuse functionality from your code, define the logic in functions outside main() and call those functions within main().
# Conclusion
# Congratulations! You now know how to create Python main() functions.
# You learned the following:
# Knowing the value of the __name__ variable is important to write code that serves the dual purpose of executable script and importable module.
# __name__ takes on different values depending on how you executed your Python file. __name__ will be equal to:
# "__main__" when the file is executed from the command line or with python -m (to execute a package’s __main__.py file)
# The name of the module, if the module is being imported
# Python programmers have developed a set of good practices to use when you want to develop reusable code.
# Now you’re ready to go write some awesome Python main() function code!