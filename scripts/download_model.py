"""
多模型下载脚本

支持:
- Z-Image-Turbo (Tongyi-MAI/Z-Image-Turbo)
- LongCat-Image (meituan-longcat/LongCat-Image)

Usage:
    python download_model.py <local_dir> [model_id]
    
Examples:
    python download_model.py ./zimage_models                          # 默认下载 Z-Image
    python download_model.py ./zimage_models Tongyi-MAI/Z-Image-Turbo
    python download_model.py ./longcat_models meituan-longcat/LongCat-Image
"""

from modelscope.hub.snapshot_download import snapshot_download
import sys
import os

# 模型映射
MODEL_MAP = {
    "zimage": "Tongyi-MAI/Z-Image-Turbo",
    "longcat": "meituan-longcat/LongCat-Image",
    # 别名
    "z-image": "Tongyi-MAI/Z-Image-Turbo",
    "z-image-turbo": "Tongyi-MAI/Z-Image-Turbo",
    "longcat-image": "meituan-longcat/LongCat-Image",
}

def get_model_id(model_arg: str) -> str:
    """解析模型 ID"""
    # 如果是短名称，查找映射
    lower_arg = model_arg.lower().replace("_", "-")
    if lower_arg in MODEL_MAP:
        return MODEL_MAP[lower_arg]
    
    # 否则直接使用（假设是完整的 model_id）
    return model_arg

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_model.py <local_dir> [model_id]")
        print("\nSupported models:")
        print("  - zimage (default): Tongyi-MAI/Z-Image-Turbo")
        print("  - longcat: meituan-longcat/LongCat-Image")
        sys.exit(1)
    
    model_dir = sys.argv[1]
    
    # 获取模型 ID
    if len(sys.argv) >= 3:
        model_id = get_model_id(sys.argv[2])
    else:
        model_id = MODEL_MAP["zimage"]  # 默认 Z-Image
    
    print(f"=" * 50)
    print(f"Model ID: {model_id}")
    print(f"Target directory: {model_dir}")
    print(f"=" * 50)
    print(f"Starting download...")
    
    try:
        snapshot_download(model_id, local_dir=model_dir)
        print(f"\n{'=' * 50}")
        print(f"Download complete!")
        print(f"Model saved to: {model_dir}")
        print(f"{'=' * 50}")
    except Exception as e:
        print(f"\n{'=' * 50}")
        print(f"Download failed: {e}")
        print(f"{'=' * 50}")
        sys.exit(1)

if __name__ == "__main__":
    main()
