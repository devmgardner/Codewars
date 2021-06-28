def valid_solution(board):
    gs=[[x for r in board[:3] for x in r[:3]], [x for r in board[3:6] for x in r[:3]], [x for r in board[6:9] for x in r[:3]], [x for r in board[:3] for x in r[3:6]], [x for r in board[3:6] for x in r[3:6]], [x for r in board[6:9] for x in r[3:6]], [x for r in board[:3] for x in r[6:9]], [x for r in board[3:6] for x in r[6:9]], [x for r in board[6:9] for x in r[6:9]]]
    def cr(n):return all(i for i in [True if r.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for r in n for x in r])
    def cc(n):return all(i for i in [True if c.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for c in [[r[i] for r in n] for i in range(9)] for x in c])
    def cg(n):return all(i for i in [True if g.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for g in gs for x in g])
    return all(i for i in [cr(board), cc(board), cg(board)])