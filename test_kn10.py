
from kn10 import encode_kn10, decode_kn10

def test_kn10():
    test_numbers = [0, 9, 10, 9999, 10000, 123456789, 9999999999999999]
    for num in test_numbers:
        encoded = encode_kn10(num)
        decoded = decode_kn10(encoded)
        assert num == decoded, f"Mismatch! {num} → {encoded} → {decoded}"
    print("✅ All 10KN tests passed!")

if __name__ == "__main__":
    test_kn10()
