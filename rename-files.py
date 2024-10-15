import os

def replace_underscores_with_hyphens(cur_dir):
    for filename in os.listdir():
        if '_' in filename and filename.endswith('.py'):
            new_filename = filename.replace('_', '-')
            os.rename(os.path.join(cur_dir, filename), os.path.join(cur_dir, new_filename))

# Replace 'your_directory_path' with the path to your directory
replace_underscores_with_hyphens(os.getcwd())