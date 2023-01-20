"""
This problem is asking you to implement a program that uses a list in Python to perform various commands. The program will take as input an integer, N, which represents the number of commands that will be given to the program. Then, it will take N lines of input, each representing a command that the program should perform on the list.

The possible commands are:

insert i e: Insert integer e at position i in the list.
print: Print the current state of the list.
remove e: Delete the first occurrence of integer e from the list.
append e: Insert integer e at the end of the list.
sort: Sort the list in ascending order.
pop: Remove the last element from the list.
reverse: Reverse the order of the elements in the list.
The program should iterate through each command in the order they are given, and perform the corresponding operation on the list.

The program would first create an empty list, then perform the following operations:

insert 5 at position 0, resulting in the list [5]
insert 10 at position 1, resulting in the list [5, 10]
insert 6 at position 0, resulting in the list [6, 5, 10]
print the list, which would output [6, 5, 10]
remove the first occurrence of 6, resulting in the list [5, 10]
append 9 to the end of the list, resulting in the list [5, 10, 9]
append 1 to the end of the list, resulting in the list [5, 10, 9, 1]
sort the list, resulting in the list [1, 5, 9, 10]
print the list, which would output [1, 5, 9, 10]
remove the last element (10) from the list, resulting in the list [1, 5, 9]
reverse the order of the elements in the list, resulting in the list [9, 5, 1]
print the list, which would output [9, 5, 1]
"""
#solution
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()
"""
This program starts by taking an input N, and then create an empty list called lst. Then it will iterate N times, each time taking an input which is a string that contains command and its parameters separated by space.

For each iteration, it will split the input into a list of strings and check the first element of the list, which should be the command. Based on the command, the program will perform the corresponding operation on the list using the appropriate method. For example, if the command is 'insert' then it will use the insert() method to insert the element at the specified position. If the command is 'print' then it will use the print() function to print the current state of the list.

This solution uses a number of if-elif block to check the command and perform the corresponding operation on the list. Please note that in python indexes starts from 0 and not 1.
"""            