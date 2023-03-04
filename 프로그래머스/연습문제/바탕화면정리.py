def solution(wallpaper):
    answer = []

    x_top = 1e9
    x_bottom = 0
    y_left = 1e9
    y_right = 0 
    for i, row in enumerate(wallpaper):
        for j, point in enumerate(row):
            if point == '#':
                x_top = min(x_top, i)
                x_bottom = max(x_bottom, i)
                y_left = min(y_left, j)
                y_right = max(y_right, j)

    answer = [x_top, y_left, x_bottom + 1, y_right + 1]

    return answer