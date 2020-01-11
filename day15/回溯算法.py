
class Solver:
    scale=8

    def __init__(self):
        self.linex = [False] * Solver.scale
        self.diay = [False] * (Solver.scale+Solver.scale)
        self.diax = [False] * (Solver.scale+Solver.scale)
        self.resolution = [0] * Solver.scale
        self.solved_cnt = 0

    def solve(self,i=0):
        if i == Solver.scale:
            print('find')
            self.solved_cnt += 1
            for i in range(Solver.scale):
                print(' ' * self.resolution[i] + '*')
                # print(tuple((i, self.resolution[i])), end=' ')
            print()
            
            return


        for j in range(Solver.scale):
            if self.linex[j] or self.diay[i+j] or self.diax[j-i+Solver.scale]:
                continue
            
            # 记录状态
            self.resolution[i] = j
            
            # 转移到下一行
            self.linex[j] = True
            self.diay[i+j]= True
            self.diax[j-i+Solver.scale] = True
            
            # 求解剩下行
            self.solve(i+1)
            
            # 从下一行状态回到这一行
            self.linex[j] = False
            self.diay[i+j]= False
            self.diax[j-i+Solver.scale] = False

if __name__ == '__main__':
    x = Solver()
    x.solve()
    print(x.solved_cnt)


