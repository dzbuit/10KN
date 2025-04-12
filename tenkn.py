
# tenkn.py - 10KN (만진수) Encoder/Decoder by blueradiance

BASE_10KN = 10000
HANGUL_OFFSET = 0xAC00  # '가' = 0

def encode_10kn(n: int) -> str:
    if n == 0:
        return chr(HANGUL_OFFSET)
    result = []
    while n > 0:
        digit = n % BASE_10KN
        ch = chr(HANGUL_OFFSET + digit)
        result.insert(0, ch)
        n //= BASE_10KN
    return ''.join(result)

def decode_10kn(s: str) -> int:
    n = 0
    for ch in s:
        val = ord(ch) - HANGUL_OFFSET
        if not (0 <= val < BASE_10KN):
            raise ValueError(f"Invalid 10KN character: '{ch}'")
        n = n * BASE_10KN + val
    return n
