import math


# -- functions --
def calculate_pri_current(tx_size_val, pri_volt_val, tx_phase_val, pri_current_val):
    try:
        p = float(tx_size_val.get())
        v = float(pri_volt_val.get())
        phase = tx_phase_val.get()
        if phase == "3-Phase":
            i = (p * 1000) / (math.sqrt(3) * v)
        else:
            i = (p * 1000) / v
        pri_current_val.set(f"{i:.1f}")
    except ValueError:
        pass


def calculate_sec_current(tx_size_val, sec_volt_val, tx_phase_val, sec_current_val):
    try:
        p = float(tx_size_val.get())
        v = float(sec_volt_val.get())
        phase = tx_phase_val.get()
        if phase == "3-Phase":
            i = (p * 1000) / (math.sqrt(3) * v)
        else:
            i = (p * 1000) / v
        sec_current_val.set(f"{i:.1f}")
    except ValueError:
        pass


def calculate_over_current(pri_current_val, sec_current_val, pri_over_current_val, sec_over_current_val):
    try:
        i_pri = float(pri_current_val.get())
        i_sec = float(sec_current_val.get())
        over_curr_pri = i_pri * 1.25
        over_curr_sec = i_sec * 1.25
        pri_over_current_val.set(f"{over_curr_pri:.1f}")
        sec_over_current_val.set(f"{over_curr_sec:.1f}")
    except ValueError:
        pass


def calculate_breaker_size(pri_over_current_val, sec_over_current_val, pri_breaker_size, sec_breaker_size):
    try:
        i_pri_min = float(pri_over_current_val.get())
        i_sec_min = float(sec_over_current_val.get())
        current_vals = [16, 21, 26, 31, 36, 41, 46, 51, 61, 71, 81, 91, 101, 111, 126, 151, 176, 201, 226, 251, 301,
                        351, 401, 451, 501, 601, 701, 801, 1001, 1201, 1601, 2001, 2501, 3001, 4001, 5001, 6001]
        breaker_vals = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250,
                        300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000]

        # primary breaker size
        bkr_size_pri = None
        for i, val in enumerate(current_vals):
            if i_pri_min < val:
                bkr_size_pri = breaker_vals[i]
                break
            else:
                bkr_size_pri = "N/A"
        pri_breaker_size.set(f"{bkr_size_pri:.1f}")

        # secondary breaker size
        bkr_size_sec = None
        for i, val in enumerate(current_vals):
            if i_sec_min < val:
                bkr_size_sec = breaker_vals[i]
                break
            else:
                bkr_size_sec = "N/A"
        sec_breaker_size.set(f"{bkr_size_sec:.1f}")
    except ValueError:
        pass


def calculate_conductor_size(pri_breaker_size, sec_breaker_size, pri_conductor_size, sec_conductor_size):
    try:
        i_pri = float(pri_breaker_size.get())
        i_sec = float(sec_breaker_size.get())
        current_vals = [15, 20, 30, 40, 55, 70, 85, 95, 100, 115, 130, 150, 175, 200, 230, 255, 285, 310, 335, 380,
                        420, 460, 475, 490, 520, 545, 590, 625, 650, 665]
        conductor_sizes = ["No. 14", "No. 12", "No. 10", "No. 8", "No. 6", "No. 4", "No. 3", "No. 2", "No. 1", "No. 1/0",
                          "No. 2/0", "No. 3/0", "No. 4/0", "250kCMIL", "300kCMIL", "350kCMIL", "400kCMIL", "500kCMIL",
                          "600kCMIL", "700kCMIL", "750kCMIL", "800kCMIL", "900kCMIL", "1000kCMIL", "1250kCMIL",
                          "1500kCMIL", "1750kCMIL", "2000kCMIL"]

        # primary conductor size
        cond_size_pri = None
        for i, val in enumerate(current_vals):
            if i_pri < val:
                cond_size_pri = conductor_sizes[i]
                break
            else:
                cond_size_pri = "N/A"
        pri_conductor_size.set(f"{cond_size_pri}")

        # secondary conductor size
        cond_size_sec = None
        for i, val in enumerate(current_vals):
            if i_sec < val:
                cond_size_sec = conductor_sizes[i]
                break
            else:
                cond_size_sec = "N/A"
        sec_conductor_size.set(f"{cond_size_sec}")
    except ValueError:
        pass


def calculate_bond_size(pri_breaker_size, sec_breaker_size, pri_bond_size, sec_bond_size):
    try:
        i_pri = float(pri_breaker_size.get())
        i_sec = float(sec_breaker_size.get())
        current_vals = [20, 30, 60, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000,
                        6000]
        bond_sizes = ["No. 14", "No. 12", "No. 10", "No. 8", "No. 6", "No. 4", "No. 3", "No. 2", "No. 1", "No. 1/0",
                      "No. 2/0", "No. 3/0", "No. 4/0", "250kCMIL", "350kCMIL", "400kCMIL", "500kCMIL", "700kCMIL",
                      "800kCMIL"]

        bond_size_pri = None
        for i, val in enumerate(current_vals):
            if i_pri < val:
                bond_size_pri = bond_sizes[i]
                break
            else:
                bond_size_pri = "N/A"
        pri_bond_size.set(f"{bond_size_pri}")

        bond_size_sec = None
        for i, val in enumerate(current_vals):
            if i_sec < val:
                bond_size_sec = bond_sizes[i]
                break
            else:
                bond_size_sec = "N/A"
        sec_bond_size.set(f"{bond_size_sec}")
    except ValueError:
        pass


def change_tx_selections(tx_phase_val, tx_size_input, tx_size_val):
    if tx_phase_val.get() == "3-Phase":
        tx_size_input["values"] = ("3", "6", "9", "15", "30", "45", "75", "112.5", "150", "225", "300", "500", "750",
                                "1000")
    else:
        tx_size_input["values"] = ("0.25", "0.5", "0.75", "1", "1.5", "2", "3", "5", "7.5", "10", "15", "25", "37.5", "50",
                                "75", "100", "167", "250", "333")
    # when changing from 3-phase to 1-phase or vice-versa, if the current tx size value is not in the list of
    # allowable selections in the new menu, clear the value so the user must select a new value
    if tx_size_val.get() not in tx_size_input["values"]:
        tx_size_val.set("")


def change_voltage_selections(tx_phase_val, pri_volt_input, sec_volt_input, pri_volt_val, sec_volt_val):
    if tx_phase_val.get() == "3-Phase":
        pri_volt_input["values"] = ("600", "480", "240", "208")
        sec_volt_input["values"] = ("600", "480", "240", "208")
    else:
        pri_volt_input["values"] = ("600", "480", "240", "208", "120")
        sec_volt_input["values"] = ("600", "480", "240", "208", "120")
    # when changing from 3-phase to 1-phase or vice-versa, if the current pri and sec voltage is not in the list of
    # allowable selections in the new menu, clear the value so the user must select a new value
    if pri_volt_val.get() not in pri_volt_input["values"]:
        pri_volt_val.set("")
    if sec_volt_val.get() not in sec_volt_input["values"]:
        sec_volt_val.set("")
