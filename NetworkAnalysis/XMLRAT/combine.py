#!/usr/bin/env python3

def read_and_concat(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:      
            parts = line.split("=")
            if len(parts) == 2:
                # Take the part after "=" and get rid of blank
                value = parts[1].strip()
                # Delete the ""
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                result.append(value)
    return "".join(result)

if __name__ == "__main__":
    filename = ""   # insert your input file here
    concatenated = read_and_concat(filename)
    print("Result:", concatenated)
