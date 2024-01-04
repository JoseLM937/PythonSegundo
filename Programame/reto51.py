def esSudokuCorrecto(miSudoku):
    for valor in range(9):
        if len(set(miSudoku[valor])) != 9:
            return False
        for i in range(9):
         if len(set(miSudoku[i][valor])) != 9:
            return False
