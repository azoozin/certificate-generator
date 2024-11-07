import cv2
import os
print(f'cv2 version: ${cv2.__version__}\n')

name_list =[]

def data_cleanup():
    try:
        with open("name-list.txt") as file:
            for line in file:
                # print(line.strip())
                name_list.append(line.strip())
            print(f'{len(name_list)} names have been loaded.\n')
    except FileNotFoundError:
        print('Error: File name-list.txt not found')

def generate_certs():
    if not os.path.exists('generated-certs'):
        os.makedirs('generated-certs')
        print('Folder for generated certificates was not found.\n')
        print('Folder for generated certificates was created.\n')

    template_path = "cert-templates/template1.jpg"
    if not os.path.exists(template_path):
        print(f"Error: Template not found in {template_path}")
        return

    template = cv2.imread("cert-templates/template1.jpg")
    if template is None:
        print(f"Error: Unable to read template file at {template_path}")
        return


    for name in name_list:
        try:
            cert = template.copy()
            
            output_path = os.path.join('generated-certs', f'{name}.jpg')
            cv2.putText(cert, name, (815, 1500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imwrite(output_path, cert)
            print(f'Certificate for {name} generated.')
        except Exception as e:
            print(f'Error: Could not generate certificate for {name}: {str(e)}')

data_cleanup()
generate_certs()