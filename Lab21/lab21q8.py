#Write a function protein_energy_temp() with an inner function
#calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
#random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0).

def protein_energy_temp():
    T = float(input("Enter temperature: "))
    H = float(input("Enter enthalpy: "))
    S = float(input("Enter entropy: "))

    def calculate_free_energy(enthalpy, entropy):
        return H - T * S

    G = calculate_free_energy(H, S)

    if G < 0:
        return "stable"
    else:
        return "unstable"

print(protein_energy_temp())