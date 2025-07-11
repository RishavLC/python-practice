data = b"This is binary data"  # Prefix 'b' makes it binary

with open("binary_file.bin", "wb") as f:
    f.write(data)