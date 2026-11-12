# Task: Mass Reduction of a Load-Bearing Shelf Bracket

## Objective
You are provided with a baseline CAD model of a shelf bracket at `/workspace/baseline.step`. The current design is too heavy. Your task is to remove material to reduce the total mass while ensuring the bracket can still safely support its design load without yielding.

## Material Properties (Steel AISI 1020)
* **Density:** $7,900\text{ kg/m}^3$ ($7.90 \times 10^{-6}\text{ kg/mm}^3$)
* **Young's Modulus:** $200,000\text{ MPa}$
* **Poisson's Ratio:** $0.29$
* **Yield Strength:** $295.0\text{ MPa}$

## Boundary Conditions & Loads
* **Fixed Face:** The entire rear vertical face ($X = 0\text{ mm}$, $Y \in [-20, 20]\text{ mm}$, $Z \in [-100, 0]\text{ mm}$) is rigidly fixed to a wall ($U_x = U_y = U_z = 0$).
* **Applied Load:** A static downward pressure load of $0.5\text{ MPa}$ is applied to the top horizontal face ($Z = 0\text{ mm}$, $X \in [0, 100]\text{ mm}$, $Y \in [-20, 20]\text{ mm}$), simulating a distributed weight.

## Constraints
1. **Mass Limit:** The final mass must be **$\le 0.45\text{ kg}$**.
2. **Stress Limit:** The maximum Von Mises stress must not exceed **$140.0\text{ MPa}$**.
3. **Mounting Surfaces:** The top horizontal face and rear vertical face must remain completely flat and unmodified to ensure flush mounting.
4. **Bounding Box:** The part must not extend beyond $X \in [0, 100]\text{ mm}$, $Y \in [-20, 20]\text{ mm}$, $Z \in [-100, 0]\text{ mm}$.

## Deliverable
Save the optimized solid geometry as `/workspace/submission.step`.
