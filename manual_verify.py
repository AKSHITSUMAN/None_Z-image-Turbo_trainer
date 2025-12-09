import sys
import os
from pathlib import Path

# Add project root to sys.path
sys.path.append(os.getcwd())

try:
    from src.models.model_detector import create_model_detector, ModelStatus

    # Explicitly point to the directory we listed earlier
    path = Path("d:/AI/None_Z-image-Turbo_trainer/zimage_models")
    print(f"Testing Path: {path}")
    print(f"Path Exists: {path.exists()}")
    if path.exists():
         print(f"Is Dir: {path.is_dir()}")
         # Verify model_index.json manually
         mi = path / "model_index.json"
         print(f"model_index.json exists: {mi.exists()} size: {mi.stat().st_size if mi.exists() else 0}")

    detector = create_model_detector("zimage", path)
    print(f"Detector Spec: {detector.spec.name}")
    print(f"Detector Rules Count: {len(detector.rules)}")
    
    # Check if schema loaded
    if hasattr(detector, 'rules'):
        for i, rule in enumerate(detector.rules):
            print(f"  Rule {i}: {rule}")

    print("\nRunning validate_local()...")
    result = detector.validate_local()
    
    print("-" * 30)
    print(f"Overall Status: {result['overall_status']}")
    print(f"Summary: {result['summary']}")
    print("-" * 30)
    
    if result['overall_status'] != ModelStatus.VALID:
        print("Details of components:")
        for k, v in result['components'].items():
            print(f"{k}: {v}")

except Exception as e:
    import traceback
    traceback.print_exc()
