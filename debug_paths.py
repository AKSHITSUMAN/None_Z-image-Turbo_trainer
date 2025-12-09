import sys
import os
from pathlib import Path

# Add webui-vue/api to path so we can import core.config
sys.path.append(os.path.join(os.getcwd(), 'webui-vue', 'api'))

try:
    print("Attempting to import core.config...")
    from core.config import get_model_path, PROJECT_ROOT
    print(f"PROJECT_ROOT in config: {PROJECT_ROOT}")
    print(f"Current Working Dir: {os.getcwd()}")

    print("\n=== Path Resolution ===")
    for model_type in ["zimage", "longcat"]:
        path = get_model_path(model_type, "base")
        print(f"Model Type: {model_type}")
        print(f"Resolved Path: {path}")
        print(f"Exists: {path.exists()}")
        if path.exists():
            print("Contents (first 20):")
            try:
                items = list(path.iterdir())
                for item in items[:20]:
                    size_str = ""
                    if item.is_file():
                        size_str = f" ({item.stat().st_size} bytes)"
                    print(f"  - {item.name}{size_str}")
            except Exception as e:
                print(f"  Error listing dir: {e}")
        else:
            print("  (Path does not exist)")
        print("-" * 30)

except ImportError as e:
    print(f"ImportError: {e}")
    print("Ensure you are running this from the project root.")

print("\n=== .env Raw check ===")
if os.path.exists(".env"):
    print(".env found. Checking for MODEL_PATH entries...")
    with open(".env", "r", encoding='utf-8') as f:
        for line in f:
            if "MODEL_PATH" in line:
                print(f"RAW: {line.strip()}")
else:
    print(".env NOT FOUND in current directory.")
