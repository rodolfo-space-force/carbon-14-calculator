# Purpose:
#     To calculate the age of an organic sample from the percentage
#     of the original carbon-14 remaining in the sample.
#
# Record of revisions:
#     Date         Programmer         Description of change
#     ==========   ================   ================================
#     28/12/2025   Rodolfo Milhomem   Python translation of original MATLAB code
#
# Define variables:
#     age     -- The age of the sample in years.
#     lambda  -- The radioactive decay constant for carbon-14,
#                in units of 1/year.
#     percent -- The percentage of carbon-14 remaining at the
#                time of the measurement.
#     ratio   -- The ratio of the carbon-14 remaining at the
#                time of the measurement to the original amount
#                of carbon-14.
#
# O CRC handbook of chemistry and physics estabelece que a meia vida do carbono-14
# é de 5730 anos, portanto a saida do programa esta correta.
# No caso do "Homem de Gelo" Ötzi, a famosa múmia natural encontrada nos Alpes entre a Áustria e a Itália em 1991
# os cientistas utilizaram datação por carbono-14 para estimar sua idade
# a porcentagem de carbono-14 remanescente no corpo de Ötzi é de aproximadamente 52,7% do original.
# ou seja, cerca de 5.300 anos atrás.


import math

# Set decay constant for carbon-14
lambda_decay = 0.00012097

# Prompt the user for the percentage of C-14 remaining
try:
    percent = float(input("Enter the percentage of carbon-14 remaining (%): "))
    if percent <= 0 or percent > 100:
        raise ValueError("Percentage must be between 0 and 100 (exclusive of 0).")

    # Perform calculations
    ratio = percent / 100  # Convert to fractional ratio
    age = (-1.0 / lambda_decay) * math.log(ratio)  # Get age in years

    # Tell the user about the age of the sample
    print(f"The age of the sample is {age:.2f} years.")

except ValueError as e:
    print("Invalid input:", e)

    # Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.
