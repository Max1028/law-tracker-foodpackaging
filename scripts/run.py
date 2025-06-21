import os
import json
from datetime import datetime
from crawler import tfda
from compare import compare_laws

# Step 1: 讀取舊資料
law_path = "data/laws"
diff_path = "data/diff"
os.makedirs(law_path, exist_ok=True)
os.makedirs(diff_path, exist_ok=True)

today = datetime.today().strftime("%Y-%m-%d")
new_file = os.path.join(law_path, f"{today}.json")
diff_file = os.path.join(diff_path, "latest.json")

# Step 2: 取得最新資料
new_data = tfda.fetch_tfda_laws()

# Step 3: 載入昨天的資料（如果有）
previous_files = sorted(os.listdir(law_path))
old_data = []
if previous_files:
    latest_old = os.path.join(law_path, previous_files[-1])
    if latest_old != new_file:
        with open(latest_old, encoding="utf-8") as f:
            old_data = json.load(f)

# Step 4: 比對差異
diff = compare_laws(old_data, new_data)

# Step 5: 儲存資料
with open(new_file, "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

with open(diff_file, "w", encoding="utf-8") as f:
    json.dump(diff, f, ensure_ascii=False, indent=2)

print(f"✔ 已更新法規資料，總筆數：{len(new_data)}，變更：{len(diff)}")
