import pytest
import cadquery as cq
from fea_solver import run_calculix_static  # Hypothetical repo wrapper for the FEA solver

@pytest.fixture
def submission_path():
    return "/workspace/submission.step"

def test_mass_and_bounding_box(submission_path):
    part = cq.importers.importStep(submission_path)

    # 1. Mass check (Volume * Density of Steel)
    volume_mm3 = part.val().Volume()
    mass_kg = volume_mm3 * 7.9e-6
    assert mass_kg <= 0.45, f"Mass {mass_kg:.2f} kg exceeds 0.45 kg limit"

    # 2. Bounding Box check
    bb = part.val().BoundingBox()
    assert bb.xmin >= -0.1 and bb.xmax <= 100.1, "X dimension out of bounds"
    assert bb.ymin >= -20.1 and bb.ymax <= 20.1, "Y dimension out of bounds"
    assert bb.zmin >= -100.1 and bb.zmax <= 0.1, "Z dimension out of bounds"

def test_structural_integrity(submission_path):
    # Runs the mesher and CalculiX solver headlessly
    results = run_calculix_static(
        step_file=submission_path,
        youngs_modulus=200000,
        poissons_ratio=0.29,
        fixed_faces={"xmin": 0},                # Fixes the rear wall
        pressure_loads={"zmax": {"value": 0.5}} # 0.5 MPa on the top face
    )

    # 3. Stress check
    assert results.max_von_mises <= 140.0, (
        f"Stress {results.max_von_mises:.1f} MPa exceeds 140.0 MPa limit"
    )
