from pyamaze import maze, agent, textLabel
from queue import PriorityQueue


def h(cell1, cell2):
    # f(n)=g(n) + h(n)
    # h(n) manhattan
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2)


def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))

    aPath = {}

    while not open.empty():
        currCell = open.get()[2]
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                if d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0]+1, currCell[1])

                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score+h(childCell, (1, 1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score
                    open.put((temp_f_score, h(childCell, (1, 1)), childCell))
                    aPath[childCell] = currCell
    forwardPath = {}
    cell = (1, 1)
    while cell != start:
        forwardPath[aPath[cell]] = cell
        cell = aPath[cell]
    return forwardPath


if __name__ == '__main__':
    m = maze(30, 30)
    m.CreateMaze()

    path = aStar(m)

    a = agent(m, footprints=True)
    m.tracePath({a: path})
    l = textLabel(m, 'A Star path length', len(path)+1)

    m.run()
