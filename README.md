# bookbot_redo
Bookbot project redo without looking.
Bookbot is a Python command-line tool that processes a .txt file. The script counts the total number of words and the frequency of each character.
**How I Solved Problems:** I was able to successfully complete this project without looking at the guided project. I encountered a problem with using `sys.argv`. I initially had this code in my main function:
`# get filepath from the command line
filepath = sys.argv[1]`
if len(sys.argv) < 2:
    print("Usage: Python3 main.py <path_to_file>")
    sys.exit(1)`

As you can probably tell, the above code will return an IndexError if you run the main.py without any argument. This is because I was trying to retrieve the element in `sys.argv[1]` before checking if it exists. When you run `Python3 main.py`, the `sys.argv` list only contains ["main.py"]. The index of a list with one element is 0. So `sys.argv[1]` will not exist. It took some time to really understand what was going on. I relized I needed to check if `sys.argv[1]` exists before capturing it in a variable. So this:
**Correct version:**
`if len(sys.arg) < 2:
    print("Usage: Python3 main.py <path_to_file>")
    filepath = sys.argv[1]`

The corrected code will first check that at most 2 elements exists in the list before retrieving `sys.argv[1]`


**Takeaway:** My biggest takeaway is the importance of slowing down, debugging, and following the dataflow to understand how data moves around a program. By slowing down and debuggin, I was able to understand a little more about `sys.argv`.
