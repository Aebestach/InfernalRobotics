#Modify the cfg text for each part.
import os

folder_path = r'C:\Games\KSP\1.12.5 Stock\GameData\MagicSmokeIndustries\Parts' # 文件夹路径
field_name_1 = 'title' # 字段名称
field_name_2 = 'description'

for dirpath, dirnames, filenames in os.walk(folder_path):
    folder_name = os.path.basename(dirpath)
    for filename in filenames:
        if filename.endswith('.cfg'):
            with open(os.path.join(dirpath, filename), 'r') as file:
                content = file.read()
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if field_name_1 in line:
                        lines[i] = f'\ttitle = #LOC_{folder_name}_title'
                    if field_name_2 in line:
                        lines[i] = f'\tdescription = #LOC_{folder_name}_description'
                content = '\n'.join(lines)
            with open(os.path.join(dirpath, filename), 'w') as file:
                file.write(content)
