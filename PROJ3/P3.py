def P3(A, B):
    a = sum(A)
    b = sum(B)
    x = len(A)
    if a == b:
        return x
    change = True
    while change:
        if sum(A)>sum(B) and A[0]<B[0]:
            del A[-1]
            del B[-1]
        elif sum(A)>sum(B) and A[0]>=B[0]:
            del A[0]
            del B[0]
        elif sum(A)<sum(B) and A[0]<=B[0]:
            del A[0]
            del B[0]
        elif sum(A)<sum(B) and A[0]>B[0]:
            del A[-1]
            del B[-1]
        elif sum(A) == sum(B):
            change = False
    y = len(A)
    return y