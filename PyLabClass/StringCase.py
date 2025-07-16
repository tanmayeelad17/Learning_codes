def covert_lc_to_uc(input_str):
    return input_str.upper()
def covert_uc_to_lc(input_str):
    return input_str.lower()
def swap_case(input_str):
    return input_str.swapcase()

input_str=input("Enter a string:")

upper_str=covert_lc_to_uc(input_str)
print("Lower case to Upper case:",upper_str)

lower_str=covert_uc_to_lc(input_str)
print("Upper string to Lower string :",lower_str)

swap_str=swap_case(input_str)
print("Swapcase:",swap_str)