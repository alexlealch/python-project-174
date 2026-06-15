import json

def generate_diff(path1, path2):
    with open(path1, 'r') as f1, open(path2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    
    all_keys = sorted(keys1 | keys2)
    
    lines = ["{"]
    
    for key in all_keys:
        if key in keys1 and key in keys2:
            if data1[key] == data2[key]:
                lines.append(f"  {key}: {data1[key]}")
            else:
                lines.append(f"  - {key}: {data1[key]}")
                lines.append(f"  + {key}: {data2[key]}")
        elif key in keys1:
            lines.append(f"  - {key}: {data1[key]}")
        elif key in keys2:
            lines.append(f"  + {key}: {data2[key]}")
            
    lines.append("}")
    
    return "\n".join(lines)
