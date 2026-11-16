# Gradient Descent to find the minimum of y = (x + 3)^2
def f(x):
    return (x + 3) ** 2

def slope(x):
    return 2 * (x + 3)

x = 2
learning_rate = 0.1

for i in range(50):
    x = x - learning_rate * slope(x)
    print("Step", i + 1, ": x =", round(x, 4),
          " y =", round(f(x), 4))

print("\nLocal minimum is at x =", round(x, 4))
print("Minimum value of y =", round(f(x), 4))
