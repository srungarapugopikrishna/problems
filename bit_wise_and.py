
# def bit_wise():
# n = int(raw_input())
# for _ in range(n):
#     ip = raw_input()
#     A = int(ip.split(' ')[0])
#     B = int(ip.split(' ')[1])
#     sol = A
#     for i in range(A, B+1):
#         sol = sol & i
#         if sol == 0:
#             break
#     print sol

# print bit_wise()


def significant_bit_position(n):
    sb_position = -1
    while n > 0:
        n = n >> 1
        sb_position += 1
    return sb_position


def bit_wise_and(A, B):
    res = 0
    while A > 0 and B > 0:
        sb_position1 = significant_bit_position(A)
        sb_position2 = significant_bit_position(B)
        if (sb_position1 != sb_position2):
            break
        sb_value = (1 << sb_position1)
        res = res + sb_value
        A = A - sb_value
        B = B - sb_value
    return res


n = int(raw_input())
for _ in range(n):
    ip = raw_input()
    A = int(ip.split(' ')[0])
    B = int(ip.split(' ')[1])
    print(bit_wise_and(A, B))
