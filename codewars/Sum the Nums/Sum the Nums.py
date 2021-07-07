def sum_of_sums(n):
    #return sumnum(sumnum2(n))
    #return sum([
    #    i+1 for i in range(
    #        sum([
    #            sum([
    #                i+1 for i in range(n)
    #            ])
    #        ])
    #    )
    #])
    return sum([
            i+1 for i in range(
                        sum([
                            sum([
                                i+1 for i in range(i+1)
                            ]) for i in range(n)
                        ])
                    )
            ])
inp = int(input())
print(sum_of_sums(inp))