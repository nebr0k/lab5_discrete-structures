def generate_result_set(A, B, C):
    result_set = set()
    for a in A:
        for b in B:
            for c in C:
                result_set.add((b, a, c))
    return result_set



def determine(bitA, bitB, U):
    A = ""
    B = ""
    N = len(U)
    notA = [0] * N
    notAString = ""
    aAndB = [0] * N
    aAndBString = ""
    aOrB = [0] * N
    aOrBString = ""
    aDifferenceB = [0] * N
    aDifferenceBString = ""
    aXorB = [0] * N
    aXorBString = ""

    for i in range(N):
        if bitA[i] == 1:
            A += U[i]
        if bitB[i] == 1:
            B += U[i]
        notA[i] = 1 - bitA[i]
        if notA[i] == 1:
            notAString += U[i]
        aAndB[i] = 1 if bitA[i] == 1 and bitB[i] == 1 else 0
        if aAndB[i] == 1:
            aAndBString += U[i]
        aOrB[i] = 1 if bitA[i] == 1 or bitB[i] == 1 else 0
        if aOrB[i] == 1:
            aOrBString += U[i]
        aDifferenceB[i] = 1 if bitA[i] == 1 and bitB[i] == 0 else 0
        if aDifferenceB[i] == 1:
            aDifferenceBString += U[i]
        aXorB[i] = bitA[i] ^ bitB[i]
        if aXorB[i] == 1:
            aXorBString += U[i]

    print(f"U: {U}")
    print(f"A: {bitA}\t{A}")
    print(f"B: {bitB}\t{B}")
    print(f"notA: {notA}\t{notAString}")
    print(f"aAndB: {aAndB}\t{aAndBString}")
    print(f"aOrB: {aOrB}\t{aOrBString}")
    print(f"aDifferenceB: {aDifferenceB}\t{aDifferenceBString}")
    print(f"aXorB: {aXorB}\t{aXorBString}")

def createBitArray(U, T):
    result = [0] * len(U)
    for i in range(len(U)):
        for j in range(len(T)):
            if T[j] == U[i]:
                result[i] = 1
                break
    return result


if __name__ == "__main__":
    A = {'a', 'b', 'c'}
    B = {'x', 'y', 'z'}
    C = {0, 1}

    result_set = generate_result_set(A, B, C)
    print(result_set)

    U = input("Input U: ")
    Uc = sorted(U)
    U = "".join(Uc)
    A = input("Input A: ")
    B = input("Input B: ")
    bitA = createBitArray(U, A)
    bitB = createBitArray(U, B)
    determine(bitA, bitB, U)


