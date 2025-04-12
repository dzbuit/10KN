
# 10KN: Ten Thousand Korean Numeric System 🇰🇷

10KN is a compact, fixed-width numeric encoding system using digits (0-9) and Korean Hangul ('가'-'힣').  
Each character in 10KN can represent 0 to 9999, significantly reducing the length of large numeric identifiers.

This system was designed to support massive numeric datasets such as prime/composite number databases, while also maintaining lexicographical sortability, visual clarity, and cultural identity.

## Features

- Compact fixed-width encoding using 0-9 and 9,999 Hangul characters
- Each position represents values 0-9999
- Ideal for compressing large integers and sorting them as strings
- Full reversibility via `encode_kn10()` and `decode_kn10()`
- Created by blueradiance (2025), licensed for public use with attribution

---

## 10KN: 만 단위 기반의 한국형 숫자 압축 시스템 🇰🇷

10KN은 숫자(0-9)와 한글(유니코드 '가'-'힣')을 활용하여  
0-9999 범위의 값을 하나의 문자로 표현하는 고정폭 숫자 인코딩 시스템입니다.

소수/합성수 데이터베이스와 같이 초대형 숫자를 다루는 상황에서  
문자열 압축, 정렬, 표현성, 시각적 명확성을 동시에 고려해 개발되었습니다.

## 주요 특징

- 자릿수당 0-9999 표현, 10진수보다 훨씬 짧은 고정 길이
- 숫자와 한글만으로 구성되어 정렬성과 직관성 확보
- `encode_kn10()`, `decode_kn10()` 함수로 완전한 복원 가능
- 2025년 blueradiance 제작, 출처 표기 시 자유 사용 가능
