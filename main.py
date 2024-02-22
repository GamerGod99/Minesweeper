import curses
from curses import wrapper
import minesweeper

Y0, X0 = 5, 5
SIZE_Y, SIZE_X = 10, 10
MINE_AMOUNT = 15


def start(std_scr):
    ms = minesweeper.Minesweeper(SIZE_X, SIZE_Y, MINE_AMOUNT)

    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    curses.mouseinterval(0)

    std_scr.clear()
    std_scr.border()
    std_scr.refresh()

    sx = max(SIZE_X, 8)
    score_win = curses.newwin(3, 2 * sx + 3, Y0, X0)
    score_win.addstr(1, 2, "000")
    score_win.addstr(1, (2 * sx + 3) // 2, "☺")
    score_win.addstr(1, 2 * sx - 4, '00:00')
    score_win.border()
    score_win.refresh()

    mine_win = curses.newwin(SIZE_Y + 2, 2 * SIZE_X + 3, Y0 + 3, X0)
    mine_win.border()
    # mine_win.addstr(1, 1, "a")

    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            mine_win.addch(y + 1, 2 * x + 2, str(ms.plane[y][x]))

    mine_win.refresh()

    while True:
        c = std_scr.get_wch()

        if c == 'q':
            break
        if c == curses.KEY_MOUSE:
            idm, xm, ym, zm, btm = curses.getmouse()
            std_scr.addstr(0, 5, f"[{ym: >2} x {xm: >2} | {'L' if btm & curses.BUTTON1_RELEASED else 'R' if btm & curses.BUTTON3_RELEASED else '!'}]")

    std_scr.getch()


if __name__ == '__main__':
    wrapper(start)
