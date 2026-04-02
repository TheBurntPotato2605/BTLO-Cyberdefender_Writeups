import os
import re
from PIL import Image
from pyzbar.pyzbar import decode

# =========================
# YOUR CHANGES
# =========================
IMAGE_DIR = " "    #The directory you downloaded the challenge's image
RESULT_FILE = " "  #The result file
JOIN_FILE = " "    #The file after joining decoded barcode


# =========================
# SORT NATURAL (1,2,3,...10)
# =========================
def natural_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith((".png"))]
files.sort(key=natural_key)

print(f"[+] Total files: {len(files)}")

results = []

with open(RESULT_FILE, "w", encoding="utf-8") as f:
    for i, file in enumerate(files, 1):
        path = os.path.join(IMAGE_DIR, file)

        try:
            img = Image.open(path)
            decoded = decode(img)

            if decoded:
                data = decoded[0].data.decode("utf-8", errors="ignore")
                f.write(f"{file} | {data}\n")
                results.append(data)
            else:
                f.write(f"{file} | FAIL\n")
                results.append("")

        except Exception as e:
            f.write(f"{file} | ERROR\n")
            results.append("")

        if i % 500 == 0:
            print(f"Processed {i}/{len(files)}")

# =========================
# CONCATENATE 
# =========================
joined = "".join([x for x in results if x != ""])

with open(JOIN_FILE, "w", encoding="utf-8") as f:
    f.write(joined)

print("\n[+] DONE")
print(f"[+] Result file: {RESULT_FILE}")
print(f"[+] Joined file: {JOIN_FILE}")
