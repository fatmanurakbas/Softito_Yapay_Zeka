from __future__ import annotations
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--parameters-billions", type=float, required=True); args = parser.parse_args()
    params = args.parameters_billions * 1e9
    for name, bits in (("FP32",32),("FP16/BF16",16),("INT8",8),("INT4 teorik",4)):
        print(f"{name:12}: {params * bits / 8 / 1024**3:.2f} GiB (yalnızca ağırlıklar)")
