import turtle
import time
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#141414")
t.color("white")
t.width(2)
grid_width = 200
t.hideturtle()
def grid():
    t.up()

    #outline
    t.goto(grid_width * -3/2, grid_width * 3/2)
    t.down()
    t.goto(grid_width * 3/2, grid_width * 3/2)
    t.goto(grid_width * 3/2, grid_width * -3/2)
    t.goto(grid_width * -3/2, grid_width * -3/2)
    t.goto(grid_width * -3/2, grid_width * 3/2)
    t.up()

    #vertical lines
    t.goto(grid_width * -1/2, grid_width * 3/2)
    t.down()
    t.goto(grid_width * -1/2, grid_width * -3/2)
    t.goto(grid_width * 1/2, grid_width * -3/2)
    t.goto(grid_width * 1/2, grid_width * 3/2)
    t.up()

    #horizontal lines
    t.goto(grid_width * -3/2, grid_width * 1/2)
    t.down()
    t.goto(grid_width * 3/2, grid_width * 1/2)
    t.goto(grid_width * 3/2, grid_width * -1/2)
    t.goto(grid_width * -3/2, grid_width * -1/2)
    t.up()

grid_factor = {
    -1: (-3/2, -1/2),
    0: (-1/2, 1/2),
    1: (1/2, 3/2)
}
turns = "X"
records = set()
initial_list = [["","",""],["","",""],["","",""]]
#{(-1,0,"x")}

def reset():
    global records
    global initial_list
    t.clear()
    t.goto(0, 0)
    records = set()
    initial_list = [["","",""],["","",""],["","",""]]
    turtle.onscreenclick(handle_click, 1, True)
    grid()

def handle_click(x, y):
    t.goto(x, y)
    if abs(x) > grid_width * 3/2 or abs(y) > grid_width * 3/2:
        print("Out of Grid")
        return
    global turns
    global records
    global initial_list
    grid_x, grid_y = 0, 0
    for i in grid_factor:
        if x > grid_factor[i][0] * grid_width and x < grid_factor[i][1] * grid_width:
            grid_x = i
        if y > grid_factor[i][0] * grid_width and y < grid_factor[i][1] * grid_width:
            grid_y = i
    if (grid_x, grid_y, "X") in records or (grid_x, grid_y, "O") in records:
        return
    records.add((grid_x, grid_y, turns))
    initial_list[1 - grid_y][1 + grid_x] = turns
    if turns == "X":
        t.goto((grid_factor[grid_x][0] * grid_width)+grid_width/4, (grid_factor[grid_y][0] * grid_width)+grid_width/4)
        t.down()
        t.goto((grid_factor[grid_x][1] * grid_width)-grid_width/4, (grid_factor[grid_y][1] * grid_width)-grid_width/4)
        t.up()
        t.goto((grid_factor[grid_x][0] * grid_width)+grid_width/4, (grid_factor[grid_y][1] * grid_width)-grid_width/4)
        t.down()
        t.goto((grid_factor[grid_x][1] * grid_width)-grid_width/4, (grid_factor[grid_y][0] * grid_width) + grid_width/4)
        t.up()
        turns = "O"
    else:
        t.goto( (grid_factor[grid_x][0] + grid_factor[grid_x][1])*grid_width/2, (grid_factor[grid_y][0] * grid_width) + grid_width/4)
        t.down()
        t.circle(grid_width/4)
        t.up()
        turns = "X"
    
    if len(records) >= 5:
        winner = check_winner(initial_list)
        if winner or len(records) == 9:
            turtle.onscreenclick(t.goto, 1, False)
            t.clear()
            t.goto(0, 0)
            t.color("yellow")
            if winner:
                t.write(f"{winner} Won!", align="center", font=("Cooper Black", 100, "italic"))
            else:
                t.write(f"It's a draw!", align="center", font=("Cooper Black", 100, "italic"))
            t.color("white")
            time.sleep(5)
            reset()

n = turtle.onscreenclick(handle_click, 1, True)
def check_winner(board):

    for row in board:
        if all(cell == row[0] and cell != "" for cell in row):
            return row[0]

    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != "" for row in range(3)):
            return board[0][col]


    if all(board[i][i] == board[0][0] and board[i][i] != "" for i in range(3)):
        return board[0][0]

    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != "" for i in range(3)):
        return board[0][2]

    return None

grid()
turtle.done()