import numpy as np

def euler_method(f, t0, y0, t_end, n):
    """Euler's method to solve dy/dt = f(t, y) from t0 to t_end with n steps."""
    t = np.linspace(t0, t_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    h = (t_end - t0) / n
    
    for i in range(n):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    
    return y[-1]

def runge_kutta_method(f, t0, y0, t_end, n):
    """Runge-Kutta 4th order method to solve dy/dt = f(t, y) from t0 to t_end with n steps."""
    t = np.linspace(t0, t_end, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    h = (t_end - t0) / n
    
    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + h/2 * k1)
        k3 = f(t[i] + h/2, y[i] + h/2 * k2)
        k4 = f(t[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return y[-1]

# Differential equation f(t, y) = t - y^2
def differential_equation(t, y):
    return t - y**2

# Parameters
t0 = 0
y0 = 1
t_end = 2
n = 10

# Solve using Euler and Runge-Kutta methods
euler_result = euler_method(differential_equation, t0, y0, t_end, n)
runge_kutta_result = runge_kutta_method(differential_equation, t0, y0, t_end, n)

euler_result, runge_kutta_result

# print(f'Euler Method: {euler_result}')
# print(f'Runge-Kutta Method: {runge_kutta_result}')

