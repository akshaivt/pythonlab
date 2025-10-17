color = input("Enter color names separated by commas: ")
color_list = color.split(",")
color_list = [c.strip() for c in color_list]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

