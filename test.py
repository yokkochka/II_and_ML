k = 10
for i in range(1,100):
    print(f"i = {i}, k = {(7*k+1)%30}")
    k = (7*k+1)%30