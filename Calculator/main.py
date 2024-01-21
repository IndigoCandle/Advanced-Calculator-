
from Calculator.calculator import Calculator


def main():
    while True:
        try:

            expression = input("Enter and expression:")
        except EOFError:
            print("\n Please dont press ctrl+d :)")
            break
        except KeyboardInterrupt:
            print("\n Please dont interrupt the process :(")
            break
        try:
            result = Calculator(expression).result
            print(result)

            if input("Do another calculation? (yes/no): ").lower() != 'yes':
                break
        except Exception as e:
            print(f"Error | {e}")
            break


if __name__ == "__main__":
    main()
