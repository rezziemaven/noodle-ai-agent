import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))
        if os.path.isdir(full_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        valid_target_path = (
            os.path.commonpath([working_dir_path, full_file_path]) == working_dir_path
        )
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Make sure that all parent directories of the file_path exist
        print(os.path.dirname(full_file_path))
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        f = open(full_file_path, "w")
        f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"
