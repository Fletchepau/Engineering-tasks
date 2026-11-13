# Task: Drone Motor Mount Weight Optimization

## Objective
Modify the provided baseline drone motor mount geometry to reduce its total mass by at least 15%, while maintaining structural integrity under peak thrust loads.

## Input Files
* `base_motor_mount.STEP`: The unoptimized, initial geometry of the motor mount.
* Material: Aluminum 6061-T6 (Yield Strength: 276 MPa, Density: 2.7 g/cm³).

## Design Constraints
1. **Load:** The mount must withstand a continuous vertical thrust load of 50N applied to the motor mounting face.
2. **Safety Factor:** The modified geometry must maintain a minimum structural safety factor of 2.0.
3. **Mounting Interfaces:** The four M3 mounting holes (16x19mm pattern) and the central shaft clearance hole must remain unmodified.
4. **Manufacturing:** The final part must be machinable via standard 3-axis CNC milling (avoid internal, enclosed voids).

## Deliverables
* An optimized CAD file (`optimized_motor_mount.STEP`).
* A brief summary of the mass reduction achieved and the calculated safety factor.
