from functions.get_files_info import get_files_info

test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]

for tc in test_cases:
    print("==================================")
    print(f"Listing contents of {tc[1]} in {tc[0]}...")
    print(get_files_info(*tc))
    print(" ")
print("==================================")
