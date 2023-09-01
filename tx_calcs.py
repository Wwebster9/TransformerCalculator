import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness
import sv_ttk
from functions import calculate_pri_current, calculate_sec_current, calculate_over_current, calculate_breaker_size,\
    calculate_conductor_size, calculate_bond_size, change_tx_selections, change_voltage_selections

# calls the function to set the DPI awareness for the app
set_dpi_awareness()

# -- window setup --
root = tk.Tk()
root.title("Transformer Calculations")
root.columnconfigure(0, weight=1)  # allows the column to stay centered as the window size is adjusted
root.grid()

# set standard fonts to be used throughout app
SEGOE_10 = font.Font(family="Segoe UI Variable", size=10)
SEGOE_12 = font.Font(family="Segoe UI Variable", size=12)

# set theme using custom sv_ttk library imported to give a Windows 11 style to the app
sv_ttk.set_theme("light")
# setup style object and configure Button styling to use same font as used throughout app
style = ttk.Style()
style.configure("Button.TButton", font=SEGOE_12)

# frame setup
main = ttk.Frame(root, padding=30)
main.grid()

# -- variables --
tx_size_val = tk.StringVar()
tx_phase_val = tk.StringVar()
pri_volt_val = tk.StringVar()
sec_volt_val = tk.StringVar()
pri_current_val = tk.StringVar()
sec_current_val = tk.StringVar()
pri_over_current_val = tk.StringVar()
sec_over_current_val = tk.StringVar()
pri_breaker_size = tk.StringVar()
sec_breaker_size = tk.StringVar()
pri_conductor_size = tk.StringVar()
sec_conductor_size = tk.StringVar()
pri_bond_size = tk.StringVar()
sec_bond_size = tk.StringVar()

# tx size label and entry fields
tx_size_label = ttk.Label(main, text="Transformer Size (kVA):", font=SEGOE_12)
tx_size_label.grid(row=0, column=0, sticky="W")
tx_size_input = ttk.Combobox(main, textvariable=tx_size_val, font=SEGOE_10, width=12)
tx_size_input["values"] = ("3", "6", "9", "15", "30", "45", "75", "112.5", "150", "225", "300", "500", "750", "1000")
tx_size_input.current(3)  # sets default to value at index 3 (15)
tx_size_input["state"] = "readonly"
tx_size_input.grid(row=0, column=1, sticky="W")

# tx phase label and entry fields
tx_phase_label = ttk.Label(main, text="3-Phase or 1-Phase:", font=SEGOE_12)
tx_phase_label.grid(row=1, column=0, sticky="W")
tx_phase_input = ttk.Combobox(main, textvariable=tx_phase_val, font=SEGOE_10, width=12)
tx_phase_input["values"] = ("3-Phase", "1-Phase")
tx_phase_input.current(0)  # sets default to value at index 0 (3-Phase)
tx_phase_input["state"] = "readonly"
tx_phase_input.grid(row=1, column=1, sticky="W")

# primary voltage label and entry fields
pri_volt_label = ttk.Label(main, text="Primary Voltage (V):", font=SEGOE_12)
pri_volt_label.grid(row=2, column=0, sticky="W")
pri_volt_input = ttk.Combobox(main, textvariable=pri_volt_val, font=SEGOE_10, width=12)
pri_volt_input["values"] = ("600", "480", "240", "208")
pri_volt_input.current(0)  # sets default to value at index 0 (600V)
pri_volt_input["state"] = "readonly"
pri_volt_input.grid(row=2, column=1, sticky="W")

# secondary voltage label and entry fields
sec_volt_label = ttk.Label(main, text="Secondary Voltage (V):", font=SEGOE_12)
sec_volt_label.grid(row=3, column=0, sticky="W")
sec_volt_input = ttk.Combobox(main, textvariable=sec_volt_val, font=SEGOE_10, width=12)
sec_volt_input["values"] = ("600", "480", "240", "208")
sec_volt_input.current(3)  # sets default to value at index 3 (208V)
sec_volt_input["state"] = 'readonly'
sec_volt_input.grid(row=3, column=1, sticky="W")

# Transformer Overload Protection label (blue bar)
label = ttk.Label(main,
                  anchor="center",
                  text="Transformer Overload Protection:",
                  foreground="white",
                  background="#00B0F0",
                  borderwidth=1,
                  relief="solid",
                  font=SEGOE_12)
label.grid(row=4, column=0, columnspan=4, sticky="EW", pady=15, ipady=5)

# -- remaining labels for currents, breaker sizes, conductor and bond sizes --
pri_curr_label = ttk.Label(main, text="Primary Current (A):", font=SEGOE_12)
pri_curr_label.grid(row=5, column=0, sticky="W", pady=(0, 15))

over_curr_pri_label = ttk.Label(main, text="Over-current Protection Min. (A):", font=SEGOE_12)
over_curr_pri_label.grid(row=6, column=0, sticky="W", pady=(0, 15))

pri_bkr_size_label = ttk.Label(main, text="Breaker Size (A):", font=SEGOE_12)
pri_bkr_size_label.grid(row=7, column=0, sticky="W", pady=(0, 15))

pri_cond_size_label = ttk.Label(main, text="Conductor Size:", font=SEGOE_12)
pri_cond_size_label.grid(row=8, column=0, sticky="W", pady=(0, 15))

pri_bond_size_label = ttk.Label(main, text="Bond Size:", font=SEGOE_12)
pri_bond_size_label.grid(row=9, column=0, sticky="W", pady=(0, 15))

sec_curr_label = ttk.Label(main, text="Secondary Current (A):", font=SEGOE_12)
sec_curr_label.grid(row=5, column=2, sticky="W", pady=(0, 15))

over_curr_sec_label = ttk.Label(main, text="Over-current Protection Min. (A):", font=SEGOE_12)
over_curr_sec_label.grid(row=6, column=2, sticky="W", pady=(0, 15))

sec_bkr_size_label = ttk.Label(main, text="Breaker Size (A):", font=SEGOE_12)
sec_bkr_size_label.grid(row=7, column=2, sticky="W", pady=(0, 15))

sec_cond_size_label = ttk.Label(main, text="Conductor Size:", font=SEGOE_12)
sec_cond_size_label.grid(row=8, column=2, sticky="W", pady=(0, 15))

sec_bond_size_label = ttk.Label(main, text="Bond Size:", font=SEGOE_12)
sec_bond_size_label.grid(row=9, column=2, sticky="W", pady=(0, 15))

# -- calculation display fields for currents, breaker sizes, conductor and bond sizes --
pri_curr_display = ttk.Label(main, textvariable=pri_current_val, width=10, anchor="center", font=SEGOE_12)
pri_curr_display.grid(row=5, column=1, sticky="W", pady=(0, 15))

sec_curr_display = ttk.Label(main, textvariable=sec_current_val, width=10, anchor="center", font=SEGOE_12)
sec_curr_display.grid(row=5, column=3, sticky="W", pady=(0, 15), padx=(0, 20))

over_curr_display_pri = ttk.Label(main, textvariable=pri_over_current_val, width=10, anchor="center", font=SEGOE_12)
over_curr_display_pri.grid(row=6, column=1, sticky="W", pady=(0, 15))

over_curr_display_sec = ttk.Label(main, textvariable=sec_over_current_val, width=10, anchor="center", font=SEGOE_12)
over_curr_display_sec.grid(row=6, column=3, sticky="W", pady=(0, 15))

breaker_size_display_pri = ttk.Label(main, textvariable=pri_breaker_size, width=10, anchor="center", font=SEGOE_12)
breaker_size_display_pri.grid(row=7, column=1, sticky="W", pady=(0, 15))

breaker_size_display_sec = ttk.Label(main, textvariable=sec_breaker_size, width=10, anchor="center", font=SEGOE_12)
breaker_size_display_sec.grid(row=7, column=3, sticky="W", pady=(0, 15))

conductor_size_display_pri = ttk.Label(main, textvariable=pri_conductor_size, width=10, anchor="center", font=SEGOE_12)
conductor_size_display_pri.grid(row=8, column=1, sticky="W", pady=(0, 15))

conductor_size_display_sec = ttk.Label(main, textvariable=sec_conductor_size, width=10, anchor="center", font=SEGOE_12)
conductor_size_display_sec.grid(row=8, column=3, sticky="W", pady=(0, 15))

bond_size_display_pri = ttk.Label(main, textvariable=pri_bond_size, width=10, anchor="center", font=SEGOE_12)
bond_size_display_pri.grid(row=9, column=1, sticky="W", pady=(0, 15))

bond_size_display_sec = ttk.Label(main, textvariable=sec_bond_size, width=10, anchor="center", font=SEGOE_12)
bond_size_display_sec.grid(row=9, column=3, sticky="W", pady=(0, 15))

# -- calculate button --
calc_button1 = ttk.Button(main,
                          text="Calculate",
                          style="Button.TButton",
                          command=lambda:
                          [calculate_pri_current(tx_size_val, pri_volt_val, tx_phase_val, pri_current_val),
                           calculate_sec_current(tx_size_val, sec_volt_val, tx_phase_val, sec_current_val),
                           calculate_over_current(pri_current_val, sec_current_val, pri_over_current_val,
                                                  sec_over_current_val),
                           calculate_breaker_size(pri_over_current_val, sec_over_current_val, pri_breaker_size,
                                                  sec_breaker_size),
                           calculate_conductor_size(pri_breaker_size, sec_breaker_size, pri_conductor_size,
                                                    sec_conductor_size),
                           calculate_bond_size(pri_breaker_size, sec_breaker_size, pri_bond_size, sec_bond_size)])
calc_button1.grid(row=10, column=0, columnspan=4, sticky="EW")

# bind the enter key to all the calculate functions
root.bind("<Return>", lambda event: [calculate_pri_current(tx_size_val, pri_volt_val, tx_phase_val, pri_current_val),
                                     calculate_sec_current(tx_size_val, sec_volt_val, tx_phase_val, sec_current_val),
                                     calculate_over_current(pri_current_val, sec_current_val, pri_over_current_val,
                                                            sec_over_current_val),
                                     calculate_breaker_size(pri_over_current_val, sec_over_current_val, pri_breaker_size,
                                                            sec_breaker_size),
                                     calculate_conductor_size(pri_breaker_size, sec_breaker_size, pri_conductor_size,
                                                              sec_conductor_size),
                                     calculate_bond_size(pri_breaker_size, sec_breaker_size, pri_bond_size,
                                                         sec_bond_size)])

# bind the enter key on the number pad to all the calculate functions
root.bind("<KP_Enter>", lambda event: [calculate_pri_current(tx_size_val, pri_volt_val, tx_phase_val, pri_current_val),
                                       calculate_sec_current(tx_size_val, sec_volt_val, tx_phase_val, sec_current_val),
                                       calculate_over_current(pri_current_val, sec_current_val, pri_over_current_val,
                                                              sec_over_current_val),
                                       calculate_breaker_size(pri_over_current_val, sec_over_current_val,
                                                              pri_breaker_size,
                                                              sec_breaker_size),
                                       calculate_conductor_size(pri_breaker_size, sec_breaker_size, pri_conductor_size,
                                                                sec_conductor_size),
                                       calculate_bond_size(pri_breaker_size, sec_breaker_size, pri_bond_size,
                                                           sec_bond_size)])

# any time a combobox value is changed, two functions will be called which update the combobox values available
# this is done so the user can only select valid values for the transformer size and voltage
root.bind("<<ComboboxSelected>>", lambda event: [change_tx_selections(tx_phase_val, tx_size_input, tx_size_val),
                                                 change_voltage_selections(tx_phase_val, pri_volt_input, sec_volt_input,
                                                                           pri_volt_val, sec_volt_val)])

root.mainloop()
