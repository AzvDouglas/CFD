import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do domínio e da grade
L = 1.0  # Comprimento do domínio
H = 1.0  # Altura do domínio
Nx = 100  # Número de pontos na direção x
Ny = 100  # Número de pontos na direção y
dx = L / (Nx - 1)  # Tamanho do passo na direção x
dy = H / (Ny - 1)  # Tamanho do passo na direção y

# Inicialização das variáveis
u = np.zeros((Nx, Ny))  # Componente x da velocidade
v = np.zeros((Nx, Ny))  # Componente y da velocidade

# Condições de contorno
u[:, 0] = 1.0  # Velocidade na parede superior
u[:, -1] = 0.0  # Velocidade na parede inferior
v[0, :] = 0.0  # Velocidade na parede esquerda e direita
v[-1, :] = 0.0

# Iteração para resolver as equações de Navier-Stokes
for it in range(100):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[i, j] = 0.25 * (u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1])
            v[i, j] = 0.25 * (v[i + 1, j] + v[i - 1, j] + v[i, j + 1] + v[i, j - 1])

# Plotagem dos resultados
X, Y = np.meshgrid(np.linspace(0, L, Nx), np.linspace(0, H, Ny))
plt.streamplot(X, Y, u, v)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Streamlines of Flow')
plt.show()
