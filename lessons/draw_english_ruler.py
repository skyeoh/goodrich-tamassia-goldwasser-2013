# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 4.2 on page 153

def draw_line(tick_length, tick_label = ''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:                                     # stop when length drops to 0
        draw_interval(center_length - 1)              # recursively draw top ticks
        draw_line(center_length)                          # draw center tick
        draw_interval(center_length - 1)               # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')                          # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)                # draw interior ticks for inch
        draw_line(major_length, str(j))                  # draw inch j line and label

if __name__ == '__main__':
    print('2-inch ruler with major tick length 4')
    draw_ruler(2, 4)

    print()
    print('1-inch ruler with major tick length 5')
    draw_ruler(1, 5)

    print()
    print('3-inch ruler with major tick length 3')
    draw_ruler(3, 3)

    print()
    print('4-inch ruler with major tick length 2')
    draw_ruler(4, 2)

    print()
    print('10-inch ruler with major tick length 1')
    draw_ruler(10, 1)
