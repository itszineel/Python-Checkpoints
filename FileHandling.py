import numpy as np

file = open("loans.csv", "r")

data = np.genfromtxt(
    file,
    delimiter=",",
    skip_header=1,
    dtype=str
)

file.close()

loan_amounts = data[:, 8]
loan_amounts = loan_amounts[loan_amounts != ""].astype(float)

mean = np.mean(loan_amounts)
median = np.median(loan_amounts)
standard_deviation = np.std(loan_amounts)

print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", standard_deviation)