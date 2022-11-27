import matplotlib.pyplot as plt
import numpy as np

# Exemple d'utilisation d'un graphe en polaire
# Cet exemple

r = np.arange(0, 6, 0.01)  # arange renvoie une liste de valeurs également espacées de 0.01 comprises entre 0 et 6
theta = 2 * np.pi * r

fig = plt.figure()

ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, r)

ax.set_xticks(np.arange(0, 2.0 * np.pi, np.pi / 6.0))
ax.set_ylim(0, 4)
ax.set_yticks(np.arange(0, 4, 1.0))

plt.show()


# Exemple trouvé sur https://gsalvatovallverdu.gitlab.io/post/2012-01-11-guide-graphique-polaires-spheriques/
# Cet exemple forme d'abord la liste des angles puis celle des valeurs en appliquant f à la première

def f(t): # fonction définissant la courbe définie avant pour alléger le code
    return np.sqrt(5. / (16. * np.pi)) * (3. * (np.cos(t))**2 - 1.)


pas = 1
theta = np.radians(np.arange(0, 360, pas))  # arange renvoie une liste de valeurs entre 0 et 360 également espacées
# de pas et radians le convertit (je vous laisse deviner en quoi) :)
valeurs = np.abs(f(theta))

ax = plt.subplot(111, projection="polar")
ax.plot(theta, valeurs)  # tracé de la courbe beue

angle = np.arccos(1. / np.sqrt(3))
ax.plot(2 * [angle], [0, 0.7], "r", 2 * [angle + np.pi], [0, 0.7], "r",
        2 * [-angle], [0, 0.7], "r", 2 * [-angle + np.pi], [0, 0.7], "r") # tracé des lignes rouges
ax.set_theta_zero_location("N")  # valeurs possibles N (north) E (east) S (south) W (west), défini où est le zéro des
# polaires

plt.show()


# Exemple de tracé de surface
fig = plt.figure(figsize=(8, 6))
ax3d = plt.axes(projection="3d")

xdata = np.linspace(-3, 3, 100)
ydata = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xdata, ydata)  # utile pour effectuer des calculs sur des listes
Z = X**2 - Y**2

ax3d.plot_surface(X, Y, Z, cmap='plasma')  # il est possible de changer les codes couleurs
ax3d.set_title('Hyperboloide hyperbolique')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')

plt.show()


# Deuxième exemple
fig = plt.figure(figsize=(8, 6))
ax3d = plt.axes(projection="3d")

xdata = np.linspace(-3, 3, 100)
ydata = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xdata, ydata)
Z = X**2 + Y**2

ax3d.plot_surface(X, Y, Z, cmap='plasma')
ax3d.set_title('Hyperboloide')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')

plt.show()

# Troisième exemple
fig = plt.figure(figsize=(8, 6))
ax3d = plt.axes(projection="3d")

xdata = np.linspace(-3, 3, 100)
ydata = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xdata, ydata)
Z = (X**2 + Y**2)**(1/2)

ax3d.plot_surface(X, Y, Z, cmap='plasma')
ax3d.set_title('Hyperboloide')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')

plt.show()