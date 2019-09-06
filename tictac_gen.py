# Kirill Varchenko, 2018

import numpy as np
import itertools as it

def tictac_gen(n=3, d=2, coords=True):
    # возвращает генератор всех вариантов линий, выйгрышных в d-мерных крестиках-ноликах на поле n*n*...*n
    # т.е. все возможные диагонали и линии, параллельные осям координат
    
    # По умолчанию (при coords=True) возвращается список координат единиц
    # При coords=False возвращается сама 0,1-матрица
    
    for m in range(d):
        # m = 0..d-1 - размерность грани, по которой идёт перебор
        # также m - количество фиксированных координат
        # d-m координат возрастают или убывают
        for fixed_coords in it.combinations(range(d), m):
            changing_coords = np.setdiff1d(range(d), fixed_coords)
            # из меняющихся координат c_inc возрастают, c_dec убывают
            # c_inc+c_dec = d-m     
            for c_dec in range(d-m):
                # при этом 0-я координата исключается из выбора,
                # чтобы убрать дублирующиеся варианты, потому что, например,
                # (2,0,0,0) - (1,1,1,1) - (0,2,2,2) 
                # т.е. "0-я убывает, 1-2-3 возрастают" даёт ту же линию, что "1-2-3 убывают, 0-я возрастает"            
                for dec_coords in it.combinations(changing_coords[1:], c_dec):
                    inc_coords = np.setdiff1d(changing_coords, dec_coords)              
                    # фиксированные координаты перебирают все возможные комбинации
                    ranges = [range(n)]*m
                    for c in it.product(*ranges):
                        ret = np.zeros((n,d), dtype=int)
                        ret[:,fixed_coords] = c
                        ret[:,inc_coords] = np.arange(n).reshape((n,1))
                        ret[:,dec_coords] = np.arange(n-1,-1,-1).reshape((n,1))
                        if coords:
                            yield ret
                        else:
                            t = np.zeros((n,)*d, dtype=int)
                            t[tuple(ret.transpose())] = 1
                            yield t

if __name__ == '__main__':
    for i in tictac_gen(coords=False):
        print(i)
