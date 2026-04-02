JOIN_FILE = "join.txt" #The file result you get from the decode.py
OUTPUT_FILE = "ascii.txt"

with open(JOIN_FILE, "r", encoding="utf-8") as f:
    data = f.read()

# split seperator
parts = data.split()

text = ""
for p in parts:
    try:
        n = int(p)
        if 0 <= n <= 255:
            text += chr(n)
        else:
            text += f"[{p}]"
    except ValueError:
        text += f"[{p}]"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[+] Decoded text:")
print(text[:2000])
print(f"\n[+] Saved to {OUTPUT_FILE}")
