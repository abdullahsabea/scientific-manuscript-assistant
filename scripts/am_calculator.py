import argparse

def calculate_ved(power, speed, hatch, layer_thickness):
    """Calculate Volumetric Energy Density (VED) in J/mm^3"""
    try:
        ved = power / (speed * hatch * layer_thickness)
        return ved
    except ZeroDivisionError:
        return None

def check_basquin(stress_amp, fatigue_strength_coeff, fatigue_strength_exponent, cycles):
    """Check consistency of Basquin equation parameters"""
    # sigma_a = sigma_f' * (N_f)^b 
    # (Assuming simple form A * N_f^b where A = fatigue strength coeff, b = exponent)
    expected_stress = fatigue_strength_coeff * (cycles ** fatigue_strength_exponent)
    diff = abs(expected_stress - stress_amp) / stress_amp * 100
    return expected_stress, diff

def main():
    parser = argparse.ArgumentParser(description="Additive Manufacturing Parameter Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # VED Calculator
    ved_parser = subparsers.add_parser("ved", help="Calculate Volumetric Energy Density (J/mm^3)")
    ved_parser.add_argument("-P", "--power", type=float, required=True, help="Laser power (W)")
    ved_parser.add_argument("-v", "--speed", type=float, required=True, help="Scan speed (mm/s)")
    ved_parser.add_argument("-H", "--hatch", type=float, required=True, help="Hatch spacing (mm)")
    ved_parser.add_argument("-t", "--thickness", type=float, required=True, help="Layer thickness (mm)")

    # Basquin Checker
    basq_parser = subparsers.add_parser("basquin", help="Check Basquin equation consistency")
    basq_parser.add_argument("--stress", type=float, required=True, help="Reported stress amplitude (MPa)")
    basq_parser.add_argument("--coeff", type=float, required=True, help="Fatigue strength coefficient (MPa)")
    basq_parser.add_argument("--exp", type=float, required=True, help="Fatigue strength exponent (usually negative)")
    basq_parser.add_argument("--cycles", type=float, required=True, help="Reported cycles to failure (N_f)")

    args = parser.parse_args()

    if args.command == "ved":
        ved = calculate_ved(args.power, args.speed, args.hatch, args.thickness)
        if ved:
            print(f"Volumetric Energy Density (VED) = {ved:.2f} J/mm³")
        else:
            print("Error: Division by zero (check if v, h, or t are 0)")
    
    elif args.command == "basquin":
        exp_stress, diff = check_basquin(args.stress, args.coeff, args.exp, args.cycles)
        print(f"Reported Stress: {args.stress} MPa")
        print(f"Calculated Stress: {exp_stress:.2f} MPa")
        print(f"Difference: {diff:.1f}%")
        if diff > 10:
            print("⚠️ WARNING: Stated parameters deviate by >10% from the equation.")
        else:
            print("✅ OK: Parameters are consistent.")

if __name__ == "__main__":
    main()
