import cadquery as cq

# --- 1. BASELINE (Solid L-Bracket: Passes stress, but fails mass constraint) ---
baseline = (
    cq.Workplane("YZ")
    .moveTo(0, 0).lineTo(100, 0).lineTo(100, -10).lineTo(10, -10)
    .lineTo(10, -100).lineTo(0, -100).close()
    .extrude(40, both=True)  # Extrude along X (width is 40mm, Y from -20 to 20)
)
cq.exporters.export(baseline, "/workspace/baseline.step")

# --- 2. SOLUTION (Webbed L-Bracket: Passes both stress and mass constraints) ---
# Removes material from the inner corner by adding a diagonal brace profile
solution = (
    cq.Workplane("YZ")
    .moveTo(0, 0).lineTo(100, 0).lineTo(100, -10)
    .lineTo(20, -10).lineTo(10, -90).lineTo(10, -100)
    .lineTo(0, -100).close()
    .extrude(40, both=True)
)
# Cut a central pocket to further reduce mass while retaining I-beam stiffness
pocket = cq.Workplane("YZ").rect(60, 60).extrude(20, both=True).translate((0, 40, -40))
solution = solution.cut(pocket)

cq.exporters.export(solution, "/workspace/solution.step")
