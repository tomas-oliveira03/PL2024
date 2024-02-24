import re
import sys


def main(fileInput):

    with open(fileInput) as file:

        fileContent = file.read()
        all_commands = re.findall(r'(on|off|=|[-+]?[0-9]+)', fileContent, flags=re.I)
        print()

        isOn = False
        sum = 0
        cont = 1
        for command in all_commands:
            command = command.lower()

            if command == "on":
                isOn = True
            elif command == "off":
                isOn = False
            elif command == "=":
                print(f"{cont}º sinal de igual -> {sum}")
                cont += 1
            elif isOn:
                sum += int(command)
        print(f"\nResultado final -> {sum}\n")


if __name__ == "__main__":
    input = sys.argv
    main(input[1])
