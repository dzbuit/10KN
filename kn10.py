
# kn10.py
# 10KN: Ten Thousand Korean Numeric System
# 숫자(0~9) + 한글 유니코드('가'~)만으로 수를 자릿수별 표현 (자릿당 0~9999)

UNICODE_START = 0xAC00  # '가'
MAX_VALUE = 9999
NUMERIC_DIGITS = [str(i) for i in range(10)]

def value_to_kn10_char(value):
    """정수(0~9999)를 10KN 문자(숫자 or 한글 유니코드)로 인코딩"""
    if 0 <= value <= 9:
        return str(value)
    elif 10 <= value <= MAX_VALUE:
        return chr(UNICODE_START + value - 1)
    else:
        raise ValueError("값은 0~9999 사이여야 합니다.")

def char_to_kn10_value(ch):
    """10KN 문자(숫자 or 한글) → 정수(0~9999)"""
    if ch in NUMERIC_DIGITS:
        return int(ch)
    codepoint = ord(ch)
    index = codepoint - UNICODE_START + 1
    if 10 <= index <= MAX_VALUE:
        return index
    else:
        raise ValueError("유효하지 않은 10KN 문자입니다.")

def encode_kn10(number):
    """정수를 10KN 문자열로 인코딩 (무한 자릿수 지원)"""
    if number == 0:
        return '0'
    result = []
    while number > 0:
        part = number % 10000
        result.insert(0, value_to_kn10_char(part))
        number //= 10000
    return ''.join(result)

def decode_kn10(kn10_str):
    """10KN 문자열을 정수로 디코딩"""
    number = 0
    for ch in kn10_str:
        number = number * 10000 + char_to_kn10_value(ch)
    return number
