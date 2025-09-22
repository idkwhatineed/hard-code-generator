import argparse
from generator import PasswordGenerator

def main():
    parser = argparse.ArgumentParser(description='Strong password generator')
    parser.add_argument('-l', '--length', type=int, default=12, help='Password length')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of passwords')
    parser.add_argument('--no-upper', action='store_true', help='No uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='No digits')
    parser.add_argument('--no-symbols', action='store_true', help='No symbols')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    for i in range(args.number):
        password = generator.generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
        strength = generator.check_strength(password)
        print(f"Password {i+1}: {password} | Strength: {strength}")

if __name__ == "__main__":
    main()