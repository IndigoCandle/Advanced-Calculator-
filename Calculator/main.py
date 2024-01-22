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
            int_result_str = str(int(result))
            float_result_str = str(result)
            if int_result_str.__eq__(float_result_str):
                print(int(result))
            else:
                print(result)
        except (KeyboardInterrupt, SyntaxError) as e:
            print(f"{e}")
            break

        print(result)

        if input("Do another calculation? (yes/no): ").lower() != 'yes':
            break


if __name__ == "__main__":
    main()
