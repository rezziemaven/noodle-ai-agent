import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_dir_path = os.path.normpath(os.path.join(working_dir_path, directory))
        if not os.path.isdir(target_dir_path):
            return f'Error: "{directory}" is not a directory'

        valid_target_dir = (
            os.path.commonpath([working_dir_path, target_dir_path]) == working_dir_path
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        contents = os.listdir(target_dir_path)
        output = ""
        for c in contents:
            if c == "__pycache__":
                continue
            c_path = target_dir_path + "/" + c
            output += f"- {c}: file_size={os.path.getsize(c_path)} bytes, is_dir={not os.path.isfile(c_path)}\n"
        return output
    except Exception as e:
        return f"Error: {e}"
