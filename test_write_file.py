from functions.write_file import write_file

test_cases = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

for tc in test_cases:
    print("==================================")
    print(f"Attempting to write content to file {tc[1]}...")
    print("----------------------------------")
    print(write_file(*tc))
    print(" ")
print("==================================")
