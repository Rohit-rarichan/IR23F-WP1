from pathlib import Path

def reverse_file(input_file_path, output_file_path):
    with open(Path(input_file_path), 'r') as input_file:
        file_size = input_file.seek(0, 2)  
        reversed_content = ""
        for pointerposition in (file_size-1, 0, -1):
            input_file.seek(pointerposition)
            char = input_file.read(1)
            reversed_content += char
        print(reversed_content)
    with open(Path(output_file_path), 'a') as output_file:
        output_file.write(reversed_content)


# Example usage
input_file_path = input("This is the file with the content in it ")
output_file_path = input("This is the file you want to write in")
reverse_file(input_file_path, output_file_path)

