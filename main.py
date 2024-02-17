import matplotlib.pyplot as plt
import numpy as np
import customtkinter
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog, messagebox

from ec_calculator import parse_equation, calculate_constant_values
from plotter import EllipticCurvePlotter

current_path = os.path.dirname(os.path.realpath(__file__))
	
class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		# configure window
		self.title("Elliptic Curve Analyzer")
		self.geometry("1024x720")
		self.resizable(0,0) # :)

		# change default font to Segoe - 14
		# make 'Enter' to analize

		# prettier (colors, icon)
		# plot <--- interpret an entry
		# errors

		# configure grid layout (2x2)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=0)

		# plot frame
		self.plot_frame = customtkinter.CTkFrame(self, width=584, corner_radius=0, fg_color = '#282828')
		self.plot_frame.grid(row=0, column=0, rowspan=4, columnspan=1, sticky="nsew")

		# Configure columns inside plot_frame
		for i in range(4):
			self.plot_frame.grid_columnconfigure(i, weight=1)

		# Configure rows inside plot_frame
		for i in range(4):
			self.plot_frame.grid_rowconfigure(i, weight=0)

		# Set up a frame for the canvas
		self.canvas_frame = customtkinter.CTkFrame(self.plot_frame)
		self.canvas_frame.grid(row=0, column=0, sticky="nsew")

		# Set up the Matplotlib figure and canvas
		self.figure = Figure(figsize=(7.3, 7.3), dpi=100)
		self.plot_canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
		self.plot_canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

		# results frame
		self.results_frame = customtkinter.CTkFrame(self, width=440, corner_radius=0, fg_color = '#2d2d2d')
		self.results_frame.grid(row=0, column=1, rowspan=4, columnspan = 1, sticky = 'nsew')

		# enter curve text
		self.enter_curve_text = customtkinter.CTkLabel(self.results_frame, text='Curve (ex. v^2 = u^3 + 3*u^2) :')
		self.enter_curve_text.grid(row=0, column=0, padx=20, pady=(5, 5), sticky='w')

		# curve combobox
		self.curve_combobox_values = ['v^2 = u^3 + 3*u^2'] # test default

		self.curve_combobox = customtkinter.CTkComboBox(self.results_frame, width=400, height=40, font=('Segoe', 15), values = self.curve_combobox_values)
		self.curve_combobox.grid(row=1, column=0, padx=20, pady=(5, 5))
		self.curve_combobox.set('')
		
		# results label
		self.results_label = customtkinter.CTkLabel(self.results_frame, text='Results:')
		self.results_label.grid(row=3, column=0, padx=20, pady=(5,5), sticky='w')

		# results textbox
		self.results_textbox = customtkinter.CTkTextbox(self.results_frame, width=400, height=500, font=('Segoe', 18))
		self.results_textbox.grid(row=4, column=0, padx=20, pady=(5,5))
		#self.results_textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 2)
		self.results_textbox.configure(state='disabled')

		# analize button
		self.analize_button = customtkinter.CTkButton(self.results_frame, width=120, height=35, font=('Segoe', 15, 'bold'), text='Analize', command = self.analize_event)
		self.analize_button.grid(row=5, column=0, padx=20, pady=(20,20), sticky='e')

		# save button
		self.save_button = customtkinter.CTkButton(self.results_frame, width=120, height=35, font=('Segoe', 15, 'bold'), text='Save', command=self.save_plot, state='disabled')
		self.save_button.grid(row=5, column = 0, padx=20, pady=(20,20), sticky='w')

		# entries for plot
		self.u_start_entry = customtkinter.CTkEntry(self.plot_frame, width=50)
		#self.u_start_entry.grid(row = 2, column = 1)
		self.u_start_entry.place(x=120, y=600)

		self.u_stop_entry = customtkinter.CTkEntry(self.plot_frame, width=50)
		#self.u_stop_entry.grid(row = 2, column = 3)
		self.u_stop_entry.place(x=300, y=600)

		self.v_start_entry = customtkinter.CTkEntry(self.plot_frame, width=50)
		#self.v_start_entry.grid(row = 3, column = 1)
		self.v_start_entry.place(x=120, y=650)

		self.v_stop_entry = customtkinter.CTkEntry(self.plot_frame, width=50)
		#self.v_stop_entry.grid(row = 3, column = 3)
		self.v_stop_entry.place(x=300, y=650)

		self.u_start_entry.insert(0, "-10")
		self.u_stop_entry.insert(0, "10")
		self.v_start_entry.insert(0, "-10")
		self.v_stop_entry.insert(0, "10")

		# label for entries
		self.u_start_label = customtkinter.CTkLabel(self.plot_frame, text='u_min:')
		self.u_stop_label = customtkinter.CTkLabel(self.plot_frame, text='u_max:')
		self.v_start_label = customtkinter.CTkLabel(self.plot_frame, text='v_min:')
		self.v_stop_label = customtkinter.CTkLabel(self.plot_frame, text='v_max:')

		#self.u_start_label.grid(row = 2, column = 0)
		#self.u_stop_label.grid(row = 2, column = 2)
		#self.v_start_label.grid(row = 3, column = 0)
		#self.v_stop_label.grid(row = 3, column = 2)
		self.u_start_label.place(x=50, y=600)
		self.u_stop_label.place(x=230, y=600)
		self.v_start_label.place(x=50, y=650)
		self.v_stop_label.place(x=230, y=650)

		# example of addition button
		self.addex_button = customtkinter.CTkButton(self.plot_frame, width=70, height=35, font=('Segoe', 14), text='Definition of addition', command=self.add_example)
		self.addex_button.place(x=400, y=600)

		# example of doubling button
		self.dupe_button = customtkinter.CTkButton(self.plot_frame, width=70, height=35, font=('Segoe', 14), text='Definition of doubling', command=self.double_example)
		self.dupe_button.place(x=400, y=650)

	def analize_event(self):
		self.results_textbox.configure(state = 'normal')
		self.results_textbox.delete("0.0", "end")
		self.results_textbox.insert("0.0", "")
		new = '\n'

		eq_str = self.curve_combobox.get().strip()

		try:
			a1, a2, a3, a4, a6 = parse_equation(eq_str)
			const_values = calculate_constant_values(a1, a2, a3, a4, a6)

			a_values = f"a1 = {a1}{new}a2 = {a2}{new}a3 = {a3}{new}a4 = {a4}{new}a6 = {a6}{new}{new}"
			b_values = f"b2 = {const_values[0]}{new}b4 = {const_values[1]}{new}b6 = {const_values[2]}{new}b8 = {const_values[3]}{new}{new}" 
			c_values = f"c4 = {const_values[4]}{new}c6 = {const_values[5]}{new}{new}"
			delta_and_j = f"delta = {const_values[6]}{new}j = {const_values[7]}"

			results = a_values + b_values + c_values + delta_and_j

			self.results_textbox.insert("0.0", results)
			self.results_textbox.configure(state = 'disabled')
			self.curve_combobox_values.append(eq_str)
			self.curve_combobox_values = list(dict.fromkeys(self.curve_combobox_values)) # ''delete'' dupes
			self.curve_combobox.configure(values=self.curve_combobox_values)

			u_start = int(self.u_start_entry.get().strip())
			u_stop = int(self.u_stop_entry.get().strip())
			v_start = int(self.v_start_entry.get().strip())
			v_stop = int(self.v_stop_entry.get().strip())

			eq_str = eq_str.replace("^", "**")
			# v^2 = u^3 + 3*u^2

			self.figure.clf()

			plot = EllipticCurvePlotter(eq_str, u_start, u_stop, v_start, v_stop, self.figure, self.plot_canvas)
			plot.plot_elliptic_curve()

			self.save_button.configure(state='normal')

		except Exception as e: 
			raise e
			self.results_textbox.delete("0.0", "end")
			self.results_textbox.insert("0.0", "Error!")
			self.results_textbox.configure(state = 'disabled')

	def save_plot(self):
		# Define the default file extension and file types
		file_types = [('PNG files', '*.png'), ('All files', '*.*')]

		# Prompt user to choose a file path for saving
		file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)

		if file_path:
			# Save the current figure to the specified file path
			self.figure.savefig(file_path, format='png')
			messagebox.showinfo("Save Successful", "Plot saved successfully!")

	def add_example(self):

			u_start = -4
			u_stop = 4
			v_start = -4
			v_stop = 4

			self.figure.clf()

			plot = EllipticCurvePlotter("", u_start, u_stop, v_start, v_stop, self.figure, self.plot_canvas)
			plot.plot_general_add()

			self.save_button.configure(state='normal')


	def double_example(self):

			u_start = -4
			u_stop = 4
			v_start = -4
			v_stop = 4

			self.figure.clf()

			plot = EllipticCurvePlotter("", u_start, u_stop, v_start, v_stop, self.figure, self.plot_canvas)
			plot.plot_general_double()

			self.save_button.configure(state='normal')




if __name__ == '__main__':
	app = App()
	app.mainloop()


