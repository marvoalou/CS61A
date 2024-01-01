def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"

    # count = 0
    # def subyield():
    #     nonlocal g
    #     ls = []
    #     nonlocal count
    #     j = 0
    #     while count != 4:
    #         ls = []
    #         new = g()
    #         while j<=count:
    #             ls.append(next(new))
    #             j+=1
    #         count += 1
    #         def lsge(ls):
    #             '''列表变为生成器'''
    #             for i in ls:
    #                 yield i
    #         yield lsge(ls)
    #         j = 0

    # for sub in subyield():
    #     yield sub
    # ## 太丑陋了

    #思维要清晰，从顶层到顶层的思维
    cnt = 0
    def gen(cnt):
        it = g()
        j = 0
        while j <= cnt:
            yield next(it)
            j += 1
    it = g()
    for _ in it:
        yield gen(cnt)
        cnt+=1