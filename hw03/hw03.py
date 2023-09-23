HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):# ?
    """         确定返回类型和运算关系
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    # 想要函数接受参数，要用lambda x
    # 由内层函数进行回调的时候，外层函数会失真，不知道内层函数传达
    # lambda x : x 以函数作为参数的时候，会失真，不知道传入的是函数，返回值无类型
    def func_adder(g):
        "*** YOUR CODE HERE ***"
        return composer(lambda x : func(g(x)))
    return func, func_adder



def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3 :
        return n
    else:
        return g(n-1) + 2*g(n - 2) + 3*g(n - 3)
    
    

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    g_list = []
    for i in range(1,n+1):
        if i <= 3 :
            g_list.append(i)
        else:
            g_list.append(g_list[i-2] + 2*g_list[i-3] + 3*g_list[i-4])
    print(g_list[-1])


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # 数学归纳思路：取中间任何一位作为终点，确定有什么分支的if条件，根据这个终点和前面的关系来写递归式
    if n // 10 == 0:
        return 0
    if n % 10 == n % 100 // 10:
        return missing_digits(n // 10)
    return n % 10 - n % 100 // 10 - 1 + missing_digits(n // 10)




def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # 拿纸算一下
    def count(total, coin):
        if total < 0 or coin > total:
            return 0
        if total == coin:
            return 1
        return count(total-coin, coin) + count(total, coin * 2)
    return count(total, 1)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    # 清楚一般规律
    if start == 1 and end == 3:
        if n == 1:
            print("Move the top disk from rod 1 to rod 3")
            return
        move_stack(n-1, 1, 2)
        move_stack(1, 1, 3)
        move_stack(n-1, 2, 3)
    if start == 1 and end == 2:
        if n == 1:
            print("Move the top disk from rod 1 to rod 2")
            return
        move_stack(n-1, 1, 3)
        move_stack(1, 1, 2)
        move_stack(n-1, 3, 2)
    if start == 2 and end == 3:
        if n == 1:
            print("Move the top disk from rod 2 to rod 3")
            return
        move_stack(n-1, 2, 1)
        move_stack(1, 2, 3)
        move_stack(n-1, 1, 3)
    if start == 2 and end == 1:
        if n == 1:
            print("Move the top disk from rod 2 to rod 1")
            return
        move_stack(n-1, 2, 3)
        move_stack(1, 2, 1)
        move_stack(n-1, 3, 1)
    if start == 3 and end == 2:
        if n == 1:
            print("Move the top disk from rod 3 to rod 2")
            return
        move_stack(n-1, 3, 1)
        move_stack(1, 3, 2)
        move_stack(n-1, 1, 2)
    if start == 3 and end == 1:
        if n == 1:
            print("Move the top disk from rod 3 to rod 1")
            return
        move_stack(n-1, 3, 2)
        move_stack(1, 3, 1)
        move_stack(n-1, 2, 1)

    '''
    便捷解法：递归只要把函数堪称整体就可以了，不用考虑细节！！！！
    via = 6 - start - end
    def move(n, start, end, via):
        if n == 1:
            print_move(start, end)
        else:
            move(n - 1, start, via, end)
            print_move(start, end)
            move(n - 1, via, end, start)
    move(n, start, end, via)
    '''

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # 右面是定义的f递归函数主体，左边是递归调用的开始
    return (lambda f: lambda x: f(f, x))(lambda f,x: 1 if x <= 1 else mul(x, f(f, x-1)))

