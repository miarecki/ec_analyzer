import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify

class EllipticCurvePlotter:
	def __init__(self, equation, start_u, stop_u, start_v, stop_v, figure, canvas):
		self.equation = equation
		self.start_u = start_u
		self.stop_u = stop_u
		self.start_v = start_v
		self.stop_v = stop_v
		self.figure = figure
		self.canvas = canvas

		self.figure.set_size_inches(7.3, 7.3)  # Adjust the size as needed
		self.figure.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0, hspace=0)

	def plot_elliptic_curve(self):
		# Parse the equation to get the variables
		u, v = symbols('u v')

		# Parse the equation to obtain the left-hand side and right-hand side
		lhs = eval(self.equation.split('=')[0].strip())
		rhs = eval(self.equation.split('=')[1].strip())

		# Create a lambda function for numerical evaluation
		curve_eq = lambdify((u, v), lhs - rhs, 'numpy')

		# Set up the domain for u and v
		u_number = abs(self.start_u - self.stop_u) * 100
		v_number = abs(self.start_v - self.stop_v) * 100

		u_values = np.linspace(self.start_u, self.stop_u, u_number)
		v_values = np.linspace(self.start_v, self.stop_v, v_number)

		# Ensure 0 is in the array and maintain sorted order
		u_values = np.sort(np.concatenate([[0], u_values]))
		v_values = np.sort(np.concatenate([[0], v_values]))

		# Create a meshgrid of u and v values
		u_mesh, v_mesh = np.meshgrid(u_values, v_values)

		# Calculate the values of the elliptic curve equation
		curve_values = curve_eq(u_mesh, v_mesh)

		# Plot the contour of the elliptic curve on the existing figure
		ax = self.figure.add_subplot(111)
		ax.contour(u_mesh, v_mesh, curve_values, levels=[0], colors='b', label='Elliptic Curve')
		'''
		# Set labels and title
		ax.set_xlabel('u')
		ax.set_ylabel('v')
		ax.set_title('Elliptic Curve: ' + self.equation)
		'''
		# Customize the appearance of the plot
		ax.spines["left"].set_position(("data", 0))
		ax.spines["bottom"].set_position(("data", 0))
		ax.spines["top"].set_visible(False)
		ax.spines["right"].set_visible(False)

		# Draw arrows at the end of the axes
		ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
		ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

		ax.set_xlim(self.start_u, self.stop_u)
		ax.set_ylim(self.start_v, self.stop_v)

		# Get the current tick positions
		xticks = ax.get_xticks()
		yticks = ax.get_yticks()

		# Remove "0.0" from tick labels
		xticklabels = [f"{x:.2f}" if x != 0 else "" for x in xticks]
		yticklabels = [f"{y:.2f}" if y != 0 else "" for y in yticks]

		# Set the modified tick labels
		ax.set_xticks(xticks)
		ax.set_yticks(yticks)
		ax.set_xticklabels(xticklabels)
		ax.set_yticklabels(yticklabels)

		# Draw the updated figure on the canvas
		self.canvas.draw()



	def plot_general_add(self):
		# Parse the equation to get the variables
		u, v = symbols('u v')

		self.equation = "v**2 = u**3 - 5*u + 3"

		# Parse the equation to obtain the left-hand side and right-hand side
		lhs = eval(self.equation.split('=')[0].strip())
		rhs = eval(self.equation.split('=')[1].strip())

		# Create a lambda function for numerical evaluation
		curve_eq = lambdify((u, v), lhs - rhs, 'numpy')

		# Set up the domain for u and v
		u_number = abs(self.start_u - self.stop_u) * 100
		v_number = abs(self.start_v - self.stop_v) * 100

		u_values = np.linspace(self.start_u, self.stop_u, u_number)
		v_values = np.linspace(self.start_v, self.stop_v, v_number)

		# Ensure 0 is in the array and maintain sorted order
		u_values = np.sort(np.concatenate([[0], u_values]))
		v_values = np.sort(np.concatenate([[0], v_values]))

		# Create a meshgrid of u and v values
		u_mesh, v_mesh = np.meshgrid(u_values, v_values)

		# Calculate the values of the elliptic curve equation
		curve_values = curve_eq(u_mesh, v_mesh)

		# Plot the contour of the elliptic curve on the existing figure
		ax = self.figure.add_subplot(111)
		ax.contour(u_mesh, v_mesh, curve_values, levels=[0], colors='b', label='Elliptic Curve')

		u_1, v_1 = -2.4723, 0.5
		u_2, v_2 = 0, 3**0.5

		# P = [u_1, v_1]
		# Q = [u_2, v_2]

		m = (v_2 - v_1) / (u_2 - u_1)
		b = v_1 - m * u_1

		x_values = u_values

		y_values = m * x_values + b
		
		ax.plot(x_values, y_values, color = 'red', zorder=1)

		x = [2.721, 2.721]
		y = [-3.088, 3.088]

		ax.plot(x, y, color='red', linestyle='--', zorder=1)

		# Points
		P = (-2.4723, 0.5)
		Q = (0, 3**0.5)
		R_prime = (2.721, 3.089)  # R'
		R = (2.721, -3.089)

		# Plotting the points
		ax.scatter(*P, color='black', zorder = 2)
		ax.scatter(*Q, color='black', zorder = 2)
		ax.scatter(*R_prime, color='black', zorder = 2)
		ax.scatter(*R, color='black', zorder = 2)

		# Labeling the points
		ax.text(P[0] - 0.3, P[1] + 0.1, r'$P$', horizontalalignment='center', fontsize = 12)
		ax.text(Q[0] - 0.4, Q[1], r'$Q$', horizontalalignment='center', fontsize = 12)
		ax.text(R_prime[0] - 0.3, R_prime[1], r"$R'$", horizontalalignment='center', fontsize = 12)
		ax.text(R[0] + .6, R[1] + 0.1, r'$R = P \boxplus Q$', verticalalignment='top', horizontalalignment='center', fontsize = 12)

		# Customize the appearance of the plot
		ax.spines["left"].set_position(("data", 0))
		ax.spines["bottom"].set_position(("data", 0))
		ax.spines["top"].set_visible(False)
		ax.spines["right"].set_visible(False)

		# Draw arrows at the end of the axes
		ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
		ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

		ax.set_xlim(self.start_u, self.stop_u)
		ax.set_ylim(self.start_v, self.stop_v)

		# Get the current tick positions
		xticks = ax.get_xticks()
		yticks = ax.get_yticks()

		# Remove "0.0" from tick labels
		xticklabels = [f"{x:.2f}" if x != 0 else "" for x in xticks]
		yticklabels = [f"{y:.2f}" if y != 0 else "" for y in yticks]

		# Set the modified tick labels
		ax.set_xticks([])
		ax.set_yticks([])
		ax.set_xticklabels([])
		ax.set_yticklabels([])

		# Draw the updated figure on the canvas
		self.canvas.draw()




	def plot_general_double(self):
		# Parse the equation to get the variables
		u, v = symbols('u v')

		self.equation = "v**2 = u**3 - 5*u + 3"

		# Parse the equation to obtain the left-hand side and right-hand side
		lhs = eval(self.equation.split('=')[0].strip())
		rhs = eval(self.equation.split('=')[1].strip())

		# Create a lambda function for numerical evaluation
		curve_eq = lambdify((u, v), lhs - rhs, 'numpy')

		# Set up the domain for u and v
		u_number = abs(self.start_u - self.stop_u) * 100
		v_number = abs(self.start_v - self.stop_v) * 100

		u_values = np.linspace(self.start_u, self.stop_u, u_number)
		v_values = np.linspace(self.start_v, self.stop_v, v_number)

		# Ensure 0 is in the array and maintain sorted order
		u_values = np.sort(np.concatenate([[0], u_values]))
		v_values = np.sort(np.concatenate([[0], v_values]))

		# Create a meshgrid of u and v values
		u_mesh, v_mesh = np.meshgrid(u_values, v_values)

		# Calculate the values of the elliptic curve equation
		curve_values = curve_eq(u_mesh, v_mesh)

		# Plot the contour of the elliptic curve on the existing figure
		ax = self.figure.add_subplot(111)
		ax.contour(u_mesh, v_mesh, curve_values, levels=[0], colors='b', label='Elliptic Curve')

		y_values = (7**.5)*(6 - u_values)/7
		
		ax.plot(u_values, y_values, color = 'red', zorder=1)

		x = [2.1429, 2.1429]
		y = [-1.4579, 1.4579]

		ax.plot(x, y, color='red', linestyle='--', zorder=1)

		# Points
		P = (-1, 7**.5)
		R_prime = (2.1429, 1.4579)  # R'
		R = (2.1429, -1.4579)

		# Plotting the points
		ax.scatter(*P, color='black', zorder = 2)
		ax.scatter(*R_prime, color='black', zorder = 2)
		ax.scatter(*R, color='black', zorder = 2)

		# Labeling the points
		ax.text(P[0] + 0.1, P[1] + 0.1, r'$P$', horizontalalignment='center', fontsize = 12)
		ax.text(R_prime[0] - 0.1, R_prime[1] + 0.2, r"$R'$", horizontalalignment='center', fontsize = 12)
		ax.text(R[0] + .6, R[1] + 0.1, r'$R = [2]P$', verticalalignment='top', horizontalalignment='center', fontsize = 12)

		# Customize the appearance of the plot
		ax.spines["left"].set_position(("data", 0))
		ax.spines["bottom"].set_position(("data", 0))
		ax.spines["top"].set_visible(False)
		ax.spines["right"].set_visible(False)

		# Draw arrows at the end of the axes
		ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
		ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

		ax.set_xlim(self.start_u, self.stop_u)
		ax.set_ylim(self.start_v, self.stop_v)

		# Get the current tick positions
		xticks = ax.get_xticks()
		yticks = ax.get_yticks()

		# Remove "0.0" from tick labels
		xticklabels = [f"{x:.2f}" if x != 0 else "" for x in xticks]
		yticklabels = [f"{y:.2f}" if y != 0 else "" for y in yticks]

		# Set the modified tick labels
		ax.set_xticks([])
		ax.set_yticks([])
		ax.set_xticklabels([])
		ax.set_yticklabels([])

		# Draw the updated figure on the canvas
		self.canvas.draw()