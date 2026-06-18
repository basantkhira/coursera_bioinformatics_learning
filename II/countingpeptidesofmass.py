def count_peptides_with_mass(m):

    aa_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    
    dp = [0] * (m + 1)
    dp[0] = 1  # empty peptide has mass 0
    
    for mass in range(1, m + 1):
        for aa in aa_masses:
            if mass - aa >= 0:
                dp[mass] += dp[mass - aa]
    
    return dp[m]

m = input("m: ")
print(count_peptides_with_mass(m))