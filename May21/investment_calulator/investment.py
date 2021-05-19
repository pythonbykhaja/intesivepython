principal = 500000
fd_rate_of_intrest = 5.5
mf_rate_of_intrest = 7.5
period_in_years = 2
fd_after_period = principal * (1+ fd_rate_of_intrest/100)** period_in_years
mf_after_period = principal * (1+ mf_rate_of_intrest/100)** period_in_years

print(f"FD after {period_in_years} years is {fd_after_period}")
print(f"MF after {period_in_years} years is {mf_after_period}")