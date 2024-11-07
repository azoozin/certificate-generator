import cert_gen as certGenerator

print('Welcome to the certificate generator!\n')
certGenerator.data_cleanup()

run = True
while(run):
    print('Please select an option:\n')
    print('1. Generate certificate')
    print('2. Exit')
    # userInput = int(input())
    userInput = input()
    
    match userInput:
        case '1':
            print('Input font scale (1-10):\n')
            font_scale = int(input())
            print('Input template file name:\n')
            template_file = input()

            certGenerator.generate_certs(font_scale, template_file)
            run = False
        case '2':
            run = False
        case _:
            print('Invalid input.\n')
            print('Please enter an option number\n')
