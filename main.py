import curses
from curses import wrapper
import minesweeper

Y0, X0 = 5, 5
SIZE_Y, SIZE_X = 10, 10
MINE_AMOUNT = 15
TITLE = "[ Minesweeper ]"
MENU = ['play: 10x10', 'play: 20x20', 'Scoreboard', "Exit"]


def scoreboard(std_scr):

    std_scr.clear()
    height, width = std_scr.getmaxyx()
    std_scr.border()
    std_scr.addstr(0, width // 2 - len(TITLE) // 2, TITLE)
    x = width // 2 - len(MENU[2]) // 2
    y = height // 2
    std_scr.addstr(y, x, MENU[2])
    std_scr.refresh()
    std_scr.getch()

def print_menu(std_scr, select_row_ind):

    std_scr.clear()
    height, width = std_scr.getmaxyx()
    std_scr.border()
    std_scr.addstr(0, width//2 - len(TITLE)//2, TITLE)

    for index, i in enumerate(MENU):
        x = width//2 - len(i)//2
        y = height//2 - len(MENU)//2 + index

        if index == select_row_ind:
            std_scr.attron(curses.color_pair(1))
            std_scr.addstr(y, x, i)
            std_scr.attroff(curses.color_pair(1))
        else:
            std_scr.addstr(y, x, i)

    std_scr.refresh()


def loop_menu(std_scr):
    current_row = 0

    while True:
        print_menu(std_scr, current_row)

        key = std_scr.getch()

        if key == curses.KEY_UP:
            if current_row > 0:
                current_row -= 1
            else:
                current_row = len(MENU) - 1

        elif key == curses.KEY_DOWN:
            if current_row < len(MENU) - 1:
                current_row += 1
            else:
                current_row = 0

        elif key in (curses.KEY_ENTER, 10, 13):

            if current_row == len(MENU) - 1: # EXIT
                break

            elif current_row == len(MENU) - 2: #SCOREBOARD
                scoreboard(std_scr)

            else:
                pass




def start(std_scr):

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)

    loop_menu(std_scr)
    # ms = minesweeper.Minesweeper(SIZE_X, SIZE_Y, MINE_AMOUNT)
    #
    # curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    # curses.mouseinterval(0)
    #
    # std_scr.clear()
    # std_scr.border()
    # std_scr.refresh()
    #
    # sx = max(SIZE_X, 8)
    # score_win = curses.newwin(3, 2 * sx + 3, Y0, X0)
    # score_win.addstr(1, 2, "000")
    # score_win.addstr(1, (2 * sx + 3) // 2, "☺")
    # score_win.addstr(1, 2 * sx - 4, '00:00')
    # score_win.border()
    # score_win.refresh()
    #
    # mine_win = curses.newwin(SIZE_Y + 2, 2 * SIZE_X + 3, Y0 + 3, X0)
    # mine_win.border()
    # # mine_win.addstr(1, 1, "a")
    #
    # for y in range(SIZE_Y):
    #     for x in range(SIZE_X):
    #         mine_win.addch(y + 1, 2 * x + 2, str(ms.plane[y][x]))
    #
    # mine_win.refresh()
    #
    # while True:
    #     c = std_scr.get_wch()
    #
    #     if c == 'q':
    #         break
    #     if c == curses.KEY_MOUSE:
    #         idm, xm, ym, zm, btm = curses.getmouse()
    #         std_scr.addstr(0, 5, f"[{ym: >2} x {xm: >2} | {'L' if btm & curses.BUTTON1_RELEASED else 'R' if btm & curses.BUTTON3_RELEASED else '!'}]")

    std_scr.getch()


if __name__ == '__main__':
    wrapper(start)
