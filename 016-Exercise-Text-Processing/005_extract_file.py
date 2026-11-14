filename = input().split("\\")[-1]
filename, extension = filename.rsplit(".", 1)
print(f"File name: {filename}\nFile extension: {extension}")
