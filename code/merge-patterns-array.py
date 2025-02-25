import json
import glob


def merge_json_files(directory_path):
    merged_data = []
    file_paths = glob.glob(directory_path + '/*.json')
    for path in file_paths:
        print(path)
        with open(path, 'r') as file:
            merged_data.append(json.load(file))
    return merged_data


#directory_path = "../generic-patterns"
directory_path = "../ruleset-files/GBV"
output_file = "merged.json"
merged_data = merge_json_files(directory_path)
with open(output_file, 'w') as outfile:
    json.dump(merged_data, outfile)
print(merged_data)