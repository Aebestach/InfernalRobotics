#Extraction of titles and abstracts.
import os

folder_path = r'C:\Games\KSP\1.12.5 Stock\GameData\MagicSmokeIndustries\Parts'  # 文件夹路径
field_name_1 = 'title'  # 字段名称
field_name_2 = 'description'
output_file = 'en-us.cfg' # 输出文件

with open(output_file, 'w') as out:
    for dirpath, dirnames, filenames in os.walk(folder_path):
        folder_name = os.path.basename(dirpath)
        for filename in filenames:
            if filename.endswith('.cfg'):
                with open(os.path.join(dirpath, filename), 'r') as file:
                    for line in file:
                        if field_name_1 in line:
                            field_value = line.split('=')[1].strip()
                            out.write(f'\t\t#LOC_{folder_name}_title = {field_value}\n')
                        if field_name_2 in line:
                            field_value = line.split('=')[1].strip()
                            out.write(f'\t\t#LOC_{folder_name}_description = {field_value}\n\n')

