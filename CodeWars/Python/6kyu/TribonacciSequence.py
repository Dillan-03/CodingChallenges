def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return [signature[0], signature[1], signature[2]]
    else:
        for i in range(3, n):
            signature.append(signature[i-3] + signature[i-2] + signature[i-1])
        return signature