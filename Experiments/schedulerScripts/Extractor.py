import json
import re

# File to extract unique responses from the log file
def extract_unique_request_ids(filename):
    request_ids = set()
    pattern = re.compile(r'"requestID"\s*:\s*"([^"]+)"')

    with open(filename, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                request_ids.add(match.group(1))

    return sorted(request_ids)

def extract_qidvid_jsons(filename, output_file):
    unique_ids = extract_unique_request_ids(filename)
    # print(f"Unique request IDs extracted: {unique_ids}")

    blocks = []
    seen_blocks = set()  # To avoid duplicates
    in_json = False
    brace_count = 0
    current_json_lines = []
    requestList = []

    with open(filename, 'r') as file:
        for line in file:
            if '{"qidvid"' in line:
                in_json = True
                ini, deli, templine = line.partition('{"qidvid"')
                templine = deli + templine
                brace_count = templine.count('{') - templine.count('}')
                current_json_lines = [templine]
                continue

            if in_json:
                brace_count += line.count('{') - line.count('}')
                current_json_lines.append(line)

                if brace_count == 0:
                    json_text = ''.join(current_json_lines)
                    try:
                        parsed = json.loads(json_text)
                        canonical = json.dumps(parsed, sort_keys=True)
                        if canonical not in seen_blocks:
                            blocks.append(parsed)
                            seen_blocks.add(canonical)

                            tempreq = parsed["content"]["requestID"]
                            if tempreq not in unique_ids:
                                print(f"Warning: Request ID {tempreq} not in unique IDs list.")
                            unique_ids.remove(tempreq)
                            requestList.append(tempreq)
                        else:
                            print(f"Duplicate block detected. Skipping requestID: {parsed['content']['requestID']}")

                    except json.JSONDecodeError:
                        print("JSON decode error.")
                    in_json = False
                    current_json_lines = []
    if unique_ids:
        print(f"Warning: The following request IDs were not found in the JSON blocks: {unique_ids}")
    

    with open(output_file, 'w') as f:
        json.dump(blocks, f, indent=2)
    

    print(f"Extracted {len(blocks)} JSON blocks starting with '{{\"qidvid\":' to {output_file}")

if __name__ == "__main__":

    extract_qidvid_jsons("./Results/FIFO/schedularrunning.txt", "./Results/FIFO_CP_48.json")

    extract_qidvid_jsons("./Results/FIFOOrdered/schedularrunning.txt", "./Results/FIFOOrdered_CP_48.json")

    extract_qidvid_jsons("./Results/Wiscon_V1/schedularrunning.txt", "./Results/Wiscon_V1_CP_48.json")

    extract_qidvid_jsons("./Results/Wiscon_V2/schedularrunning.txt", "./Results/Wiscon_V2_CP_48.json")

    extract_qidvid_jsons("./Results/Wiscon_V3/schedularrunning.txt", "./Results/Wiscon_V3_CP_48.json")

    extract_qidvid_jsons("./Results/Colorado_V1/schedularrunning.txt", "./Results/Colorado_V1_CP_48.json")

    extract_qidvid_jsons("./Results/Colorado_V2/schedularrunning.txt", "./Results/Colorado_V2_CP_48.json")
