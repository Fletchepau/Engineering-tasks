import sys
import cadquery as cq

def grade_submission(base_path, sub_path, min_reduction=0.15):
    try:
        base = cq.importers.importStep(base_path)
        sub = cq.importers.importStep(sub_path)
    except Exception as e:
        print(f"FAIL: Could not load STEP file. Error: {e}")
        return False

    base_vol = base.val().Volume()
    sub_vol = sub.val().Volume()

    if sub_vol <= 0:
        print("FAIL: Submitted model has zero or negative volume.")
        return False

    # Check overall bounding box envelope (40x40x40mm with 0.5mm tolerance)
    bb = sub.val().BoundingBox()
    dims = sorted([round(bb.xlen, 2), round(bb.ylen, 2), round(bb.zlen, 2)])
    if dims != [40.0, 40.0, 40.0]:
        print(f"FAIL: Bounding box dimensions altered ({dims} mm). Must remain 40x40x40 mm.")
        return False

    # Calculate mass/volume reduction percentage
    reduction = (base_vol - sub_vol) / base_vol
    print(f"Base Volume:      {base_vol:.2f} mm^3")
    print(f"Submitted Volume: {sub_vol:.2f} mm^3")
    print(f"Mass Reduction:   {reduction * 100:.2f}%")

    if reduction >= min_reduction:
        print("PASS: Mass reduction target (>= 15.0%) achieved!")
        return True
    else:
        print(f"FAIL: Mass reduction ({reduction * 100:.2f}%) is below the 15.0% target.")
        return False

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "optimized_motor_mount.STEP"
    success = grade_submission("base_motor_mount.STEP", target_file)
    sys.exit(0 if success else 1)
