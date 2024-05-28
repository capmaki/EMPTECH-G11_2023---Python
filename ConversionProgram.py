txt_1 = "Welcome to the Conversion Program made by {}!"
my_name = "Marlea A. Guevarra"

print(
    txt_1.format(my_name),
    "\n"
)

first_name = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last_name = input("Enter your last name: ")

txt_2 = "Hi, {} {} {}! Let us get started with converting."

print(
    txt_2.format(first_name, middle_initial, last_name),
    "\n"
)

print(
    "Converting measurements of Length and Width.",
    "\n"
)

m = float(input("Enter a number in meters to convert: "))

m_to_cm = float(m * 100)
m_to_in = float(m_to_cm/2.54)
m_to_km = float(m/1000)
m_to_yd = float(m * 1.09361)
m_to_ft = float(m/0.3048)

txt_3 = "{} meters is equal to {} centimeters."
txt_4 = "{} meters is equal to {} inches."
txt_5 = "{} meters is equal to {} kilometers."
txt_6 = "{} meters is equal to {} yards."
txt_7 = "{} meters is equal to {} feet."

print(
    "The number being converted is", m, "meters.",
    "\n"
)

print(
    "Here's the conversion summary:",
    "\n"
)

print(
    "\t",
    txt_3.format(m, m_to_cm)
)

print(
    "\t",
    txt_4.format(m, m_to_in)
)

print(
    "\t",
    txt_5.format(m, m_to_km)
)

print(
    "\t",
    txt_6.format(m, m_to_yd)
)

print(
    "\t",
    txt_7.format(m, m_to_ft)
)

print("\n")

print(
    "Converting measurements of Volume(Liquids).",
    "\n"
)

ml = float(input("Enter a number in milliliters to convert: "))

ml_to_l = float(ml * 0.001)
ml_to_kl = float(ml_to_l/1000)
ml_to_gal = float(ml_to_l/3.785)
ml_to_qt = float(ml_to_gal * 4)
ml_to_oz = float(ml_to_gal * 128)
ml_to_pt = float(ml_to_qt * 2)

txt_8 = "{} milliliters is equal to {} liters."
txt_9 = "{} milliliters is equal to {} kiloliters."
txt_10 = "{} milliliters is equal to {} gallons."
txt_11 = "{} milliliters is equal to {} quarts."
txt_12 = "{} milliliters is equal to {} ounces."
txt_13 = "{} milliliters is equal to {} pints."

print(
    "The number being converted is", ml, "milliliters.",
    "\n"
)

print(
    "Here are the conversions:",
    "\n"
)

print(
    "\t",
    txt_8.format(ml, ml_to_l)
)

print(
    "\t",
    txt_9.format(ml, ml_to_kl)
)

print(
    "\t",
    txt_10.format(ml, ml_to_gal)
)

print(
    "\t",
    txt_11.format(ml, ml_to_qt)
)

print(
    "\t",
    txt_12.format(ml, ml_to_oz)
)

print(
    "\t",
    txt_13.format(ml, ml_to_pt)
)

print("\n")

print(
    "Converting measurements of Day and Time.",
    "\n"
)

mins = float(input("Enter a number in minutes to convert: "))

mins_to_s = float(mins * 60)
mins_to_hr = float(mins/60)
mins_to_dy = float(mins_to_hr/24)
mins_to_wk = float(mins_to_dy/7)
mins_to_yr = float(mins_to_dy/365)
mins_to_mon = float(mins_to_yr * 12)

txt_14 = "{} minutes is equal to {} seconds."
txt_15 = "{} minutes is equal to {} hours."
txt_16 = "{} minutes is equal to {} days."
txt_17 = "{} minutes is equal to {} weeks."
txt_18 = "{} minutes is equal to {} months."
txt_19 = "{} minutes is equal to {} years."

print(
    "The number being converted is", mins, "minutes.",
    "\n"
)

print(
    "Here are the conversions:",
    "\n"
)

print(
    "\t",
    txt_14.format(mins, mins_to_s)
)

print(
    "\t",
    txt_15.format(mins, mins_to_hr)
)

print(
    "\t",
    txt_16.format(mins, mins_to_dy)
)

print(
    "\t",
    txt_17.format(mins, mins_to_wk)
)

print(
    "\t",
    txt_18.format(mins, mins_to_mon)
)

print(
    "\t",
    txt_19.format(mins, mins_to_yr)
)

print("\n")

print(
    "Converting measurements of Temperature.",
    "\n"
)

f = float(input("Enter a number in Fahrenheit to convert: "))

f_to_c = float((f - 32)/1.8)
f_to_k = float(f_to_c + 273.15)
f_to_r = float(f_to_c * 1.8 + 491.67)

txt_20 = "{} Fahrenheit is equal to {} Celsius."
txt_21 = "{} Fahrenheit is equal to {} Kelvin."
txt_22 = "{} Fahrenheit is equal to {} Rankine."

print(
    "\t",
    txt_20.format(f, f_to_c)
)

print(
    "\t",
    txt_21.format(f, f_to_k)
)

print(
    "\t",
    txt_22.format(f, f_to_r)
)

print("\n")

print("Thank you for using the Conversion Program!")
