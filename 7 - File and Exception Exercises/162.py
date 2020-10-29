""" While 80 characters is a common width for a terminal window, some terminals are
narrow or wider. This can present challenges when displaying documents containing
paragraphs of text. The lines might be too long and wrap, making them difficult to
read, or they might be too short and fail to make use of the available space.
Write a program that opens a file and displays it so that each line is filled as full as
possible. If you read a line that is too long then your program should break it up into
words and add words to the current line until it is full. Then your program should
start a new line and display the remaining words. Similarly, if you read a line that is
too short then you will need to use words from the next line of the file to finish filling
the current line of output. For example, consider a file containing the following lines
from “Alice’s Adventures in Wonderland”: """
