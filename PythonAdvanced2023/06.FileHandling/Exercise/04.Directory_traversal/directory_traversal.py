import os

extensions_and_files = {}


def walk_directory(root_dir, depth):
    for dir_path, dir_names, filenames in os.walk(root_dir):
        # Calculate the current depth based on the directory separator
        current_depth = dir_path.count(os.path.sep) - root_dir.count(os.path.sep)

        if current_depth <= depth:
            for file in filenames:
                # Extract the file extension
                extension = os.path.splitext(file)[1]
                extensions_and_files.setdefault(extension, [])
                extensions_and_files[extension].append(file)


path = input()
max_depth = 1
walk_directory(path, max_depth)

with open("report.txt", "w") as report:
    for file_ext, files in sorted(extensions_and_files.items(), key=lambda x: (x[0], x[1].sort())):
        report.write(f".{file_ext}\n")
        report.writelines([f"- - - {file}\n" for file in files])
