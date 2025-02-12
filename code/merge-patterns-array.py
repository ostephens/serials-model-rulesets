import json
import glob


def merge_json_files(directory_path):
    merged_data = []
    file_paths = glob.glob(directory_path + '/sg-*.json')
    for path in file_paths:
        with open(path, 'r') as file:
            data = {}
            data['ruleset'] = json.load(file)
            merged_data.append(data)
    return merged_data


directory_path = "./"
output_file = "merged.json"
merged_data = merge_json_files(directory_path)
with open(output_file, 'w') as outfile:
    json.dump(merged_data, outfile)
print(merged_data)