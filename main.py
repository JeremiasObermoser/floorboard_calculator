# libraries
import math

# area size [mm]
length = 5000.0
width = 2000.0

# avaliable boards [mm]
board_length = 2000.0
board_width = 200.0
gap_width = 0.0

# needed rows
needed_rows_gapless = math.ceil(width / board_width)
needed_rows = math.ceil(width / (board_width + gap_width - gap_width / needed_rows_gapless))
print('needed rows: ', str(needed_rows))

# find whole boards
boards_in_row = length / board_length
whole_boards_in_row = math.floor(boards_in_row)
if whole_boards_in_row < boards_in_row :
    partial_boards = boards_in_row - whole_boards_in_row
    partial_boards_lengt = (boards_in_row * board_length) - (whole_boards_in_row * board_length)
print('partial boards: ', partial_boards)

partial_cuts = 0
partial_cuts_length = 0
if partial_boards <= board_length / 2 :
    while board_length > partial_cuts_length :
        partial_cuts += 1
        partial_cuts_length += partial_boards_lengt
        #print(partial_cuts)
        #print(partial_cuts_length)
    print(partial_cuts)
    print(partial_boards_lengt)