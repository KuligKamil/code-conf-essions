To select multiple lines and add a tab (indent) for them in Vim, you can follow these steps:

Enter Visual Mode:

Move the cursor to the first line you want to indent.
Press V to enter Visual Line mode.

Select Multiple Lines:

Use the j key to move the cursor down and select the lines you want to indent.
Indent the Selected Lines:

Press > to indent the selected lines.
Example
Move the cursor to the first line you want to indent.
Press V to start Visual Line mode.
Use j to select the lines you want to indent.
Press > to indent the selected lines.
Alternatively, you can use a range command in normal mode:

Move the cursor to the first line you want to indent.
Type :, then the range of lines you want to indent (e.g., :1,5> to indent lines 1 to 5).
Press Enter.
This will indent the specified range of lines.


ctr+v + end + go down + >



vim go back with the action

GitHub Copilot
To undo the last action in Vim, you can use the u command. This will revert the most recent change you made.

Steps to Undo the Last Action
Press u in normal mode to undo the last action.
Example
If you have just indented multiple lines and want to undo that action:

Press u to undo the indentation.
If you need to redo the action you just undid, you can use Ctrl + r.

Summary
Undo: Press u in normal mode.
Redo: Press Ctrl + r in normal mode.


Add -v or --verbose to see more debug messages.

Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv.
A reasonable level to start is -vvv, connection debugging might require -vvvv. (from the docs)


uv run ansible-playbook neovim.yml -K -vvvv