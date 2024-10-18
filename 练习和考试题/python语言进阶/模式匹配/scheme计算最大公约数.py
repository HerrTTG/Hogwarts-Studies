# (define (mod m n))
#     (- m (* n (quotient m n)))
#
# (define (gcd m n))
#     (if (= n 0))
#         m
#         (gcd n (mod m n))
#
# (display (gcd 18 45))

# 上面的scheme的表达式相当于python写的以下函数
def mod(m, n):
    return m - (m // n * n)


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, mod(m, n))


print(gcd(18, 45))
