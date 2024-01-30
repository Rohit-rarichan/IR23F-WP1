def reverse_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        file_size = input_file.seek(0, 2)  
        reversed_content = ""
        for pointerposition in (file_size-1, -1, -1):
            



# Example usage
input_file_path = input("This is the file with the content in it ")
output_file_path = input("This is the file you want to write in")


