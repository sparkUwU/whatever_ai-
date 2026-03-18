import numpy as np
import pandas as pd

# Example temperatures in Celsius
celsius_temps = np.array([0, 20, 30, 40, 100])

# Convert to Fahrenheit using NumPy
fahrenheit_temps = (celsius_temps * 1.8) + 32

# Create a Pandas DataFrame
df = pd.DataFrame({
    'Celsius': celsius_temps,
    'Fahrenheit': fahrenheit_temps
})

print(df)
