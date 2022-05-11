clock = [3, 3, 3, 2, 2, 2]
max = len(clock)
win = []
start = 0


def clock_move(current_pos, move, is_clockwise=True):
    if is_clockwise:
        new_pos = current_pos + move
        if new_pos >= max:
            new_pos = current_pos - max + move
    else:
        new_pos = current_pos - move
        if new_pos < 0:
            new_pos = max - abs(new_pos)
    return new_pos


print("Possible movements:")
while start < max:
    win = [start]
    movement = {start: True}
    current_pos = start

    while len(win) > 0 and len(win) < max:
        move = clock[current_pos]

        if movement[current_pos]:
            new_pos = clock_move(current_pos, move)
            if new_pos not in win:
                win.append(new_pos)
                movement[new_pos] = True
                current_pos = new_pos
            else:
                movement[current_pos] = False
        else:

            new_pos = clock_move(current_pos, move, False)
            if new_pos not in win:
                win.append(new_pos)
                movement[new_pos] = True
                current_pos = new_pos
            else:
                movement.pop(current_pos)
                win.pop()
                current_pos = win[-1]
                while not movement[current_pos]:
                    movement.pop(current_pos)
                    win.pop()
                    if len(win) <= 0:
                        break
                    current_pos = win[-1]
                if len(win) <= 0:
                    break
                movement[current_pos] = False

    start += 1
    if len(win) > 0:
        print(win)
