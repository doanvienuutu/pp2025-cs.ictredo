import main
#def ui(stdscr):
 #   curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
  #  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
   # YELLOW_AND_RED = curses.color_pair(1)
    #RED_AND_GREEN = curses.color_pair(2)
#    stdscr.addstr("---------------------------------------------------------------------------------------------------------------------")
 #   stdscr.addstr("List courses:\n", YELLOW_AND_RED)
print("---------------------------------------------------------------------------------------------------------------------")
print("List course:\n")
for i in range(len(main.list_course)):
    print(main.list_course[i])
    print()
  #  stdscr.addstr("                        -----------------------------------------------------------------")
   # stdscr.addstr("List students:\n", YELLOW_AND_RED)
print("                        -----------------------------------------------------------------")
print("List student:\n")
for i in range(len(main.list_student)):
    print(main.list_student[i])
    print()
print("---------------------------------------------------------------------------------------------------------------------")
#wrapper(ui)