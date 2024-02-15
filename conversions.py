# Conversion Program - Jordyn Wright
# Imports
import numpy
from colorama import Fore


# Main Method
def main():
    def begin():
        print(Fore.BLUE + "\033[1m Which type of conversion would you like to do?\n\033[0m" + Fore.MAGENTA +
              "   1. Length (l)     2. Area (a)\n"
              "   3. Volume (v)     4. Liquid Volume (lv)\n"
              "   5. Weight (w)     6. Temperature (tp)\n"
              "   7. Frequency (f)  8. Speed (s)\n"
              "   9. Time (ti)")
        try:
            command = (input(Fore.YELLOW + ">> ")).lower()
            while command in ["l", "a", "w", "v", "lv", "w", "tp", "f", "s", "ti",
                              "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return command
            while command not in ["l", "a", "w", "v", "lv", "w", "tp", "f", "s", "ti",
                                  "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print(Fore.RED + " Please enter a valid abbreviation or value 1-9. ")
                return begin()
        except ValueError:
            print(Fore.RED + " Please enter a valid abbreviation. ")
            return begin()
        except IndexError:
            print(Fore.RED + " Please enter a valid abbreviation. ")
            return begin()

    # 1. Length
    def length():
        if command == 'l' or command == '1':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: mm cm 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Millimeters (mm)  2. Centimeters (cm)\n"
                      "  3. Meters (m)        4. Kilometers (km)\n"
                      "  5. Inches (in)       6. Feet (ft)\n"
                      "  7. Yards (yd)        8. Miles (mi)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                mm = "Millimeters (mm)"
                cm = "Centimeters (cm)"
                m = "Meters (m)"
                km = "Kilometers (km)"
                inch = "Inches (in)"
                ft = "Feet (ft)"
                yd = "Yards (yd)"
                mi = "Miles (mi)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # length conversions
                # 1. Millimeters
                if start_unit == 'mm':
                    if end_unit == 'mm':
                        print(mm, " -> ", mm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(mm, " -> ", cm)
                        conversion = value / 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(mm, " -> ", m)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(mm, " -> ", km)
                        conversion = value / 100000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(mm, " -> ", inch)
                        conversion = value / 25.4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(mm, " -> ", ft)
                        conversion = value / 305
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(mm, " -> ", yd)
                        conversion = value / 914
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(mm, " -> ", mi)
                        conversion = value / 1609000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 2. Centimeters
                elif start_unit == 'cm':
                    if end_unit == 'mm':
                        print(cm, " -> ", mm)
                        conversion = value * 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(cm, " -> ", cm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(cm, " -> ", m)
                        conversion = value / 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(cm, " -> ", km)
                        conversion = value / 100000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(cm, " -> ", inch)
                        conversion = value / 2.54
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(cm, " -> ", ft)
                        conversion = value / 30.48
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(cm, " -> ", yd)
                        conversion = value / 91.44
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(cm, " -> ", mi)
                        conversion = value / 160934
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 3. Meters
                elif start_unit == 'm':
                    if end_unit == 'mm':
                        print(m, " -> ", mm)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(m, " -> ", cm)
                        conversion = value * 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(m, " -> ", m)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(m, " -> ", km)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(m, " -> ", inch)
                        conversion = value * 39.37
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(m, " -> ", ft)
                        conversion = value * 3.281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(m, " -> ", yd)
                        conversion = value * 1.094
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(m, " -> ", mi)
                        conversion = value / 1609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 4. Kilometers
                elif start_unit == 'km':
                    if end_unit == 'mm':
                        print(km, " -> ", mm)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(km, " -> ", cm)
                        conversion = value * 100000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(km, " -> ", m)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(km, " -> ", km)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(km, " -> ", inch)
                        conversion = value * 39370
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(km, " -> ", ft)
                        conversion = value * 3281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(km, " -> ", yd)
                        conversion = value * 1094
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(km, " -> ", mi)
                        conversion = value / 1.609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 5. Inches
                elif start_unit == 'in':
                    if end_unit == 'mm':
                        print(inch, " -> ", mm)
                        conversion = value * 25.4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(inch, " -> ", cm)
                        conversion = value * 2.54
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(inch, " -> ", m)
                        conversion = value / 39.37
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(inch, " -> ", km)
                        conversion = value / 39370
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'inch':
                        print(inch, " -> ", inch)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(inch, " -> ", ft)
                        conversion = value / 12
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(inch, " -> ", yd)
                        conversion = value / 36
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(inch, " -> ", mi)
                        conversion = value / 63360
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 6. Feet
                elif start_unit == 'ft':
                    if end_unit == 'mm':
                        print(ft, " -> ", mm)
                        conversion = value * 305
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(ft, " -> ", cm)
                        conversion = value * 30.48
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(ft, " -> ", m)
                        conversion = value / 3.281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(ft, " -> ", km)
                        conversion = value / 3281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(ft, " -> ", inch)
                        conversion = value * 12.0
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(ft, " -> ", ft)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(ft, " -> ", yd)
                        conversion = value / 3
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(ft, " -> ", mi)
                        conversion = value / 5280
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 7. Yards
                elif start_unit == 'yd':
                    if end_unit == 'mm':
                        print(yd, " -> ", mm)
                        conversion = value * 914
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(yd, " -> ", cm)
                        conversion = value * 91.44
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(yd, " -> ", m)
                        conversion = value / 1.094
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(yd, " -> ", km)
                        conversion = value / 1094
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(yd, " -> ", inch)
                        conversion = value * 36
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(yd, " -> ", ft)
                        conversion = value * 12
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(yd, " -> ", yd)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(yd, " -> ", mi)
                        conversion = value / 1760
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # 8. Miles
                elif start_unit == 'mi':
                    if end_unit == 'mm':
                        print(mi, " -> ", mm)
                        conversion = value * 1609000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'cm':
                        print(mi, " -> ", cm)
                        conversion = value * 160934
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(mi, " -> ", m)
                        conversion = value * 1609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'km':
                        print(mi, " -> ", km)
                        conversion = value * 1.609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(mi, " -> ", inch)
                        conversion = value * 63360
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(mi, " -> ", ft)
                        conversion = value * 5280
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(mi, " -> ", yd)
                        conversion = value * 1760
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(mi, " -> ", mi)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    length()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return length()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return length()

    # 2. Area
    def area():
        if command == 'a' or command == '2':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: km cm 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Square Centimeters (cm)  2. Square Meters (m)\n"
                      "  3. Hectare (ha)             4. Square Kilometers (km)\n"
                      "  5. Square Inches (in)       6. Square Feet (ft)\n"
                      "  7. Square Yards (yd)        8. Square Miles (mi)\n"
                      "  9. Acres (acre)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                cm = "Square Centimeters(sq cm)"
                m = "Square Meters(sq m)"
                ha = "Hectare(ha)"
                km = "Square Kilometers (sq km)"
                inch = "Square Inches (sq in)"
                ft = "Square Feet (sq ft)"
                yd = "Square Yards (sq yd)"
                mi = "Square Miles (sq mi)"
                acre = "Acres (acre)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # area conversions
                # 1. Square Centimeters
                if start_unit == 'cm':
                    if end_unit == 'cm':
                        print(cm, " -> ", cm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(cm, " -> ", m)
                        conversion = value * 10000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(cm, " -> ", ha)
                        conversion = value / 100000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(cm, " -> ", km)
                        conversion = value / 10000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(cm, " -> ", inch)
                        conversion = value / 6.452
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(cm, " -> ", ft)
                        conversion = value / 929
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(cm, " -> ", yd)
                        conversion = value / 8361
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(cm, " -> ", mi)
                        conversion = value / 25900000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(cm, " -> ", acre)
                        conversion = value / 40470000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 2. Square Meters
                elif start_unit == 'm':
                    if end_unit == 'cm':
                        print(m, " -> ", cm)
                        conversion = value * 10000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(m, " -> ", m)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(m, " -> ", ha)
                        conversion = value / 10000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(m, " -> ", km)
                        conversion = value / 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(m, " -> ", inch)
                        conversion = value * 1550
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(m, " -> ", ft)
                        conversion = value * 10.764
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(m, " -> ", yd)
                        conversion = value * 1.196
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(m, " -> ", mi)
                        conversion = value / 2590000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(m, " -> ", acre)
                        conversion = value / 4047
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 3. Hectare
                elif start_unit == 'ha':
                    if end_unit == 'cm':
                        print(ha, " -> ", cm)
                        conversion = value * 100000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(ha, " -> ", m)
                        conversion = value * 10000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(ha, " -> ", ha)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(ha, " -> ", km)
                        conversion = value / 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(ha, " -> ", inch)
                        conversion = value * 15500000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(ha, " -> ", ft)
                        conversion = value * 107639
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(ha, " -> ", yd)
                        conversion = value * 11960
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(ha, " -> ", mi)
                        conversion = value / 259
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(ha, " -> ", acre)
                        conversion = value * 2.471
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 4. Square Kilometers
                elif start_unit == 'km':
                    if end_unit == 'cm':
                        print(km, " -> ", cm)
                        conversion = value * 10000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(km, " -> ", m)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(km, " -> ", ha)
                        conversion = value * 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(km, " -> ", km)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(km, " -> ", inch)
                        conversion = value * 1550000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(km, " -> ", ft)
                        conversion = value * 10760000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(km, " -> ", yd)
                        conversion = value * 1196000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(km, " -> ", mi)
                        conversion = value / 2.59
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(km, " -> ", acre)
                        conversion = value * 247
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 5. Square Inches
                elif start_unit == 'in':
                    if end_unit == 'cm':
                        print(inch, " -> ", cm)
                        conversion = value * 6.452
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(inch, " -> ", m)
                        conversion = value / 1550
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(inch, " -> ", ha)
                        conversion = value / 15500000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(inch, " -> ", km)
                        conversion = value / 1550000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(inch, " -> ", inch)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(inch, " -> ", ft)
                        conversion = value / 144
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(inch, " -> ", yd)
                        conversion = value / 1296
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(inch, " -> ", mi)
                        conversion = value / 4014000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(inch, " -> ", acre)
                        conversion = value / 6273000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 6. Square Feet
                elif start_unit == 'ft':
                    if end_unit == 'cm':
                        print(ft, " -> ", cm)
                        conversion = value * 929
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(ft, " -> ", m)
                        conversion = value / 10.764
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(ft, " -> ", ha)
                        conversion = value / 107639
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(ft, " -> ", km)
                        conversion = value / 10760000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(ft, " -> ", inch)
                        conversion = value * 144
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(ft, " -> ", ft)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(ft, " -> ", yd)
                        conversion = value / 9
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(ft, " -> ", mi)
                        conversion = value / 27880000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(ft, " -> ", acre)
                        conversion = value / 43560
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 7. Square Yards
                elif start_unit == 'yd':
                    if end_unit == 'cm':
                        print(yd, " -> ", cm)
                        conversion = value * 8361
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(yd, " -> ", m)
                        conversion = value / 1.196
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(yd, " -> ", ha)
                        conversion = value / 11960
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(yd, " -> ", km)
                        conversion = value / 1196000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(yd, " -> ", inch)
                        conversion = value * 1296
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(yd, " -> ", ft)
                        conversion = value * 9
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(yd, " -> ", yd)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(yd, " -> ", mi)
                        conversion = value / 3098000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(yd, " -> ", acre)
                        conversion = value / 4840
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 8. Square Miles
                elif start_unit == 'mi':
                    if end_unit == 'cm':
                        print(mi, " -> ", cm)
                        conversion = value * 2590000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(mi, " -> ", m)
                        conversion = value * 2590000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(mi, " -> ", ha)
                        conversion = value * 259
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(mi, " -> ", km)
                        conversion = value * 2.59
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(mi, " -> ", inch)
                        conversion = value * 4014000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(mi, " -> ", ft)
                        conversion = value * 27880000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(mi, " -> ", yd)
                        conversion = value * 3098000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(mi, " -> ", mi)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(mi, " -> ", acre)
                        conversion = value * 640
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # 9. Acres
                elif start_unit == 'acre':
                    if end_unit == 'cm':
                        print(acre, " -> ", cm)
                        conversion = value * 40470000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(acre, " -> ", m)
                        conversion = value * 4047
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'ha':
                        print(acre, " -> ", ha)
                        conversion = value / 2.471
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ha)
                    elif end_unit == 'km':
                        print(acre, " -> ", km)
                        conversion = value / 247
                        conversion = numpy.around(conversion, 4)
                        print(conversion, km)
                    elif end_unit == 'in':
                        print(acre, " -> ", inch)
                        conversion = value * 6273000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                    elif end_unit == 'ft':
                        print(acre, " -> ", ft)
                        conversion = value * 43560
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(acre, " -> ", yd)
                        conversion = value * 4840
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'mi':
                        print(acre, " -> ", mi)
                        conversion = value / 640
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mi)
                    elif end_unit == 'acre':
                        print(acre, " -> ", acre)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, acre)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    area()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return area()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return area()

    # 3. Volume
    def volume():
        if command == 'v' or command == '3':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: mm cm 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Cubic Centimeter (cm)  2. Cubic Meter (m)\n"
                      "  3. Cubic Millimeters (mm) 4. Cubic Feet (ft)\n"
                      "  5. Cubic Yards (yd)       6. Cubic Inches (in)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                cm = "Cubic Centimeter (cu cm)"
                m = "Cubic Meter (cu m)"
                mm = "Cubic Millimeters (cu mm)"
                ft = "Cubic Feet (cu ft)"
                yd = "Cubic Yards (cu yd)"
                inch = "Cubic Inches (cu in)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # volume conversions
                # 1. Centimeters
                if start_unit == 'cm':
                    if end_unit == 'cm':
                        print(cm, " -> ", cm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(cm, " -> ", m)
                        conversion = value / 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(cm, " -> ", mm)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(cm, " -> ", ft)
                        conversion = value / 28317
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(cm, " -> ", yd)
                        conversion = value / 764555
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(cm, " -> ", inch)
                        conversion = value / 16.387
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # 2. Meters
                elif start_unit == 'm':
                    if end_unit == 'cm':
                        print(m, " -> ", cm)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(m, " -> ", m)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(m, " -> ", mm)
                        conversion = value * 1000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(m, " -> ", ft)
                        conversion = value * 35.315
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(m, " -> ", yd)
                        conversion = value * 1.308
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(m, " -> ", inch)
                        conversion = value * 61024
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # 3. Millimeters
                elif start_unit == 'mm':
                    if end_unit == 'cm':
                        print(mm, " -> ", cm)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(mm, " -> ", m)
                        conversion = value / 1000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(mm, " -> ", mm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(mm, " -> ", ft)
                        conversion = value / 28320000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(mm, " -> ", yd)
                        conversion = value / 764600000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(mm, " -> ", inch)
                        conversion = value / 16387
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # 4. Feet
                elif start_unit == 'ft':
                    if end_unit == 'cm':
                        print(ft, " -> ", cm)
                        conversion = value * 28317
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(ft, " -> ", m)
                        conversion = value / 35.315
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(ft, " -> ", mm)
                        conversion = value * 28320000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(ft, " -> ", ft)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(ft, " -> ", yd)
                        conversion = value / 27
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(ft, " -> ", inch)
                        conversion = value * 1728
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # 5. Yards
                elif start_unit == 'yd':
                    if end_unit == 'cm':
                        print(yd, " -> ", cm)
                        conversion = value * 764555
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(yd, " -> ", m)
                        conversion = value / 1.308
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(yd, " -> ", mm)
                        conversion = value * 764600000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(yd, " -> ", ft)
                        conversion = value * 27
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(yd, " -> ", yd)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(yd, " -> ", inch)
                        conversion = value * 46656
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # 6. Inches
                elif start_unit == 'in':
                    if end_unit == 'cm':
                        print(inch, " -> ", cm)
                        conversion = value * 16.387
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cm)
                    elif end_unit == 'm':
                        print(inch, " -> ", m)
                        conversion = value / 61024
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'mm':
                        print(inch, " -> ", mm)
                        conversion = value * 16387
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'ft':
                        print(inch, " -> ", ft)
                        conversion = value / 1728
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ft)
                    elif end_unit == 'yd':
                        print(inch, " -> ", yd)
                        conversion = value / 46656
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yd)
                    elif end_unit == 'in':
                        print(inch, " -> ", inch)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, inch)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    volume()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return volume()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return volume()

    # 4. Liquid Volume
    def liquidVolume():
        if command == 'lv' or command == '4':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: tsp oz 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Centiliters (cl)      2. Millimeters (mm)\n"
                      "  3. Liters (l)            4. Teaspoons (tsp)\n"
                      "  5. Tablespoons (tbsp)    6. Drams (d)\n"
                      "  7. Fluid Ounces (oz)     8. Gills (gi)\n"
                      "  9. Cups (c)              10. Pints (pt)\n"
                      "  11. Quarts (qt)          12. Gallons (gal)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                cl = "Centiliters (cl)"
                mm = "Millimeters (mm)"
                l = "Liters (l)"
                tsp = "Teaspoons (tsp)"
                tbsp = "Tablespoons (tbsp)"
                d = "Drams"
                oz = "Fluid Ounces (fl oz)"
                gi = "Gills (gi)"
                cup = "Cups"
                pt = "Pints (pt)"
                qt = "Quarts (qt)"
                gal = "Gallons (gal)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # liquid volume conversions
                # 1. Centiliters
                if start_unit == 'cl':
                    if end_unit == 'cl':
                        print(cl, " -> ", cl)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(cl, " -> ", mm)
                        conversion = value * 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(cl, " -> ", l)
                        conversion = value / 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(cl, " -> ", tsp)
                        conversion = value * 2.029
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(cl, " -> ", tbsp)
                        conversion = value / 1.479
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(cl, " -> ", d)
                        conversion = value * 2.705
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(cl, " -> ", oz)
                        conversion = value / 2.957
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(cl, " -> ", gi)
                        conversion = value / 11.829
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(cl, " -> ", cup)
                        conversion = value / 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(cl, " -> ", pt)
                        conversion = value / 47.318
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(cl, " -> ", qt)
                        conversion = value / 94.635
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(cl, " -> ", gal)
                        conversion = value / 379
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 2. Millimeters
                elif start_unit == 'mm':
                    if end_unit == 'cl':
                        print(mm, " -> ", cl)
                        conversion = value / 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(mm, " -> ", mm)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(mm, " -> ", l)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(mm, " -> ", tsp)
                        conversion = value / 4.929
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(mm, " -> ", tbsp)
                        conversion = value / 14.787
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(mm, " -> ", d)
                        conversion = value / 3.697
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(mm, " -> ", oz)
                        conversion = value / 29.574
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(mm, " -> ", gi)
                        conversion = value / 118294
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(mm, " -> ", cup)
                        conversion = value / 240000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(mm, " -> ", pt)
                        conversion = value / 473176
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(mm, " -> ", qt)
                        conversion = value / 946353
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(mm, " -> ", gal)
                        conversion = value / 3785000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 3. Liters
                elif start_unit == 'l':
                    if end_unit == 'cl':
                        print(l, " -> ", cl)
                        conversion = value * 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(l, " -> ", mm)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(l, " -> ", l)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(l, " -> ", tsp)
                        conversion = value * 203
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(l, " -> ", tbsp)
                        conversion = value * 67.628
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(l, " -> ", d)
                        conversion = value * 271
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(l, " -> ", oz)
                        conversion = value * 33.814
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(l, " -> ", gi)
                        conversion = value * 8.454
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(l, " -> ", cup)
                        conversion = value * 4.167
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(l, " -> ", pt)
                        conversion = value * 2.113
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(l, " -> ", qt)
                        conversion = value * 1.057
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(l, " -> ", gal)
                        conversion = value / 3.785
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 4. Teaspoons
                elif start_unit == 'tsp':
                    if end_unit == 'cl':
                        print(tsp, " -> ", cl)
                        conversion = value / 2.029
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(tsp, " -> ", mm)
                        conversion = value * 4.929
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(tsp, " -> ", l)
                        conversion = value / 203
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(tsp, " -> ", tsp)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(tsp, " -> ", tbsp)
                        conversion = value / 3
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(tsp, " -> ", d)
                        conversion = value * 1.333
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(tsp, " -> ", oz)
                        conversion = value / 6
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(tsp, " -> ", gi)
                        conversion = value / 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(tsp, " -> ", cup)
                        conversion = value / 48.692
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(tsp, " -> ", pt)
                        conversion = value / 96
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(tsp, " -> ", qt)
                        conversion = value / 192
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(tsp, " -> ", gal)
                        conversion = value / 768
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 5. Tablespoons
                elif start_unit == 'tbsp':
                    if end_unit == 'cl':
                        print(tbsp, " -> ", cl)
                        conversion = value * 1.479
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(tbsp, " -> ", mm)
                        conversion = value * 14.787
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(tbsp, " -> ", l)
                        conversion = value / 67.628
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(tbsp, " -> ", tsp)
                        conversion = value * 3
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(tbsp, " -> ", tbsp)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(tbsp, " -> ", d)
                        conversion = value * 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(tbsp, " -> ", oz)
                        conversion = value / 2
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(tbsp, " -> ", gi)
                        conversion = value / 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(tbsp, " -> ", cup)
                        conversion = value / 16.231
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(tbsp, " -> ", pt)
                        conversion = value / 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(tbsp, " -> ", qt)
                        conversion = value / 64
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(tbsp, " -> ", gal)
                        conversion = value / 256
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 6. Drams
                elif start_unit == 'd':
                    if end_unit == 'cl':
                        print(d, " -> ", cl)
                        conversion = value / 2.705
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(d, " -> ", mm)
                        conversion = value * 3.697
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(d, " -> ", l)
                        conversion = value / 271
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(d, " -> ", tsp)
                        conversion = value / 1.333
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(d, " -> ", tbsp)
                        conversion = value / 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(d, " -> ", d)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(d, " -> ", oz)
                        conversion = value / 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(d, " -> ", gi)
                        conversion = value / 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(d, " -> ", cup)
                        conversion = value / 64.932
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(d, " -> ", pt)
                        conversion = value / 128
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(d, " -> ", qt)
                        conversion = value / 256
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(d, " -> ", gal)
                        conversion = value / 1024
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 7. Fluid Ounces
                elif start_unit == 'oz':
                    if end_unit == 'cl':
                        print(oz, " -> ", cl)
                        conversion = value * 2.957
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(oz, " -> ", mm)
                        conversion = value * 29.574
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(oz, " -> ", l)
                        conversion = value / 33.814
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(oz, " -> ", tsp)
                        conversion = value * 6
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(oz, " -> ", tbsp)
                        conversion = value * 2
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(oz, " -> ", d)
                        conversion = value * 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(oz, " -> ", oz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(oz, " -> ", gi)
                        conversion = value / 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(oz, " -> ", cup)
                        conversion = value / 8.115
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(oz, " -> ", pt)
                        conversion = value / 16
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(oz, " -> ", qt)
                        conversion = value / 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(oz, " -> ", gal)
                        conversion = value / 128
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 8. Gills
                elif start_unit == 'gi':
                    if end_unit == 'cl':
                        print(gi, " -> ", cl)
                        conversion = value * 11.829
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(gi, " -> ", mm)
                        conversion = value * 118
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(gi, " -> ", l)
                        conversion = value / 8.454
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(gi, " -> ", tsp)
                        conversion = value * 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(gi, " -> ", tbsp)
                        conversion = value * 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(gi, " -> ", d)
                        conversion = value * 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(gi, " -> ", oz)
                        conversion = value * 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(gi, " -> ", gi)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(gi, " -> ", cup)
                        conversion = value / 2.029
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(gi, " -> ", pt)
                        conversion = value / 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(gi, " -> ", qt)
                        conversion = value / 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(gi, " -> ", gal)
                        conversion = value / 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 9. Cups
                elif start_unit == 'c':
                    if end_unit == 'cl':
                        print(cup, " -> ", cl)
                        conversion = value * 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(cup, " -> ", mm)
                        conversion = value * 240
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(cup, " -> ", l)
                        conversion = value / 4.167
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(cup, " -> ", tsp)
                        conversion = value * 48.692
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(cup, " -> ", tbsp)
                        conversion = value * 16.231
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(cup, " -> ", d)
                        conversion = value * 64.923
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(cup, " -> ", oz)
                        conversion = value * 8.115
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(cup, " -> ", gi)
                        conversion = value * 2.029
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(cup, " -> ", cup)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(cup, " -> ", pt)
                        conversion = value / 1.972
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(cup, " -> ", qt)
                        conversion = value / 3.943
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(cup, " -> ", gal)
                        conversion = value / 15.773
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 10. Pints
                elif start_unit == 'pt':
                    if end_unit == 'cl':
                        print(pt, " -> ", cl)
                        conversion = value * 47.318
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(pt, " -> ", mm)
                        conversion = value * 473
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(pt, " -> ", l)
                        conversion = value / 2.113
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(pt, " -> ", tsp)
                        conversion = value * 96
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(pt, " -> ", tbsp)
                        conversion = value * 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(pt, " -> ", d)
                        conversion = value * 128
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(pt, " -> ", oz)
                        conversion = value * 16
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(pt, " -> ", gi)
                        conversion = value * 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(pt, " -> ", cup)
                        conversion = value * 1.972
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(pt, " -> ", pt)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(pt, " -> ", qt)
                        conversion = value / 2
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(pt, " -> ", gal)
                        conversion = value / 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 11. Quarts
                elif start_unit == 'qt':
                    if end_unit == 'cl':
                        print(qt, " -> ", cl)
                        conversion = value * 94.635
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(qt, " -> ", mm)
                        conversion = value * 946
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(qt, " -> ", l)
                        conversion = value / 1.057
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(qt, " -> ", tsp)
                        conversion = value * 192
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(qt, " -> ", tbsp)
                        conversion = value * 64
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(qt, " -> ", d)
                        conversion = value * 256
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(qt, " -> ", oz)
                        conversion = value * 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(qt, " -> ", gi)
                        conversion = value * 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(qt, " -> ", cup)
                        conversion = value * 3.943
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(qt, " -> ", pt)
                        conversion = value * 2
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(qt, " -> ", qt)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(qt, " -> ", gal)
                        conversion = value / 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # 12. Gallons
                elif start_unit == 'gal':
                    if end_unit == 'cl':
                        print(gal, " -> ", cl)
                        conversion = value * 379
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cl)
                    elif end_unit == 'mm':
                        print(gal, " -> ", mm)
                        conversion = value * 3785
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mm)
                    elif end_unit == 'l':
                        print(gal, " -> ", l)
                        conversion = value * 3.785
                        conversion = numpy.around(conversion, 4)
                        print(conversion, l)
                    elif end_unit == 'tsp':
                        print(gal, " -> ", tsp)
                        conversion = value * 768
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tsp)
                    elif end_unit == 'tbsp':
                        print(gal, " -> ", tbsp)
                        conversion = value * 256
                        conversion = numpy.around(conversion, 4)
                        print(conversion, tbsp)
                    elif end_unit == 'd':
                        print(gal, " -> ", d)
                        conversion = value * 1024
                        conversion = numpy.around(conversion, 4)
                        print(conversion, d)
                    elif end_unit == 'oz':
                        print(gal, " -> ", oz)
                        conversion = value * 128
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'gi':
                        print(gal, " -> ", gi)
                        conversion = value * 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gi)
                    elif end_unit == 'c':
                        print(gal, " -> ", cup)
                        conversion = value * 15.773
                        conversion = numpy.around(conversion, 4)
                        print(conversion, cup)
                    elif end_unit == 'pt':
                        print(gal, " -> ", pt)
                        conversion = value * 8
                        conversion = numpy.around(conversion, 4)
                        print(conversion, pt)
                    elif end_unit == 'qt':
                        print(gal, " -> ", qt)
                        conversion = value * 4
                        conversion = numpy.around(conversion, 4)
                        print(conversion, qt)
                    elif end_unit == 'gal':
                        print(gal, " -> ", gal)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, gal)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values. ")
                    liquidVolume()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return liquidVolume()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return liquidVolume()

    # 5. Weight
    def weight():
        if command == 'w' or command == '5':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: mg lbs 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Kilograms (kg)  2. Milligrams (mg)\n"
                      "  3. Grams (g)       4. Ounces (oz)\n"
                      "  5. Stone (st)      6. Pounds (lbs)\n"
                      "  7. US Ton (ton)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                kg = "Kilograms (kg)"
                mg = "Milligrams (mg)"
                g = "Grams (g)"
                oz = "Ounces (oz)"
                st = "Stone (st)"
                lbs = "Pounds (lbs)"
                ton = "US Ton (tons)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # weight conversions
                # 1. Kilograms
                if start_unit == 'kg':
                    if end_unit == 'kg':
                        print(kg, " -> ", kg)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(kg, " -> ", mg)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(kg, " -> ", g)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(kg, " -> ", oz)
                        conversion = value * 35.274
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(kg, " -> ", st)
                        conversion = value / 6.35
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(kg, " -> ", lbs)
                        conversion = value * 2.205
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(kg, " -> ", ton)
                        conversion = value / 907
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 2. Milligrams
                elif start_unit == 'mg':
                    if end_unit == 'kg':
                        print(mg, " -> ", kg)
                        conversion = value / 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(mg, " -> ", mg)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(mg, " -> ", g)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(mg, " -> ", oz)
                        conversion = value / 28350
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(mg, " -> ", st)
                        conversion = value / 6350000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(mg, " -> ", lbs)
                        conversion = value / 453592
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(mg, " -> ", ton)
                        conversion = value / 907200000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 3. Grams
                elif start_unit == 'g':
                    if end_unit == 'kg':
                        print(g, " -> ", kg)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(g, " -> ", mg)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(g, " -> ", g)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(g, " -> ", oz)
                        conversion = value / 28.35
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(g, " -> ", st)
                        conversion = value / 6350
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(g, " -> ", lbs)
                        conversion = value / 454
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(g, " -> ", ton)
                        conversion = value / 907185
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 4. Ounces
                elif start_unit == 'oz':
                    if end_unit == 'kg':
                        print(oz, " -> ", kg)
                        conversion = value / 35.274
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(oz, " -> ", mg)
                        conversion = value * 28350
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(oz, " -> ", g)
                        conversion = value * 28.35
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(oz, " -> ", oz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(oz, " -> ", st)
                        conversion = value / 224
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(oz, " -> ", lbs)
                        conversion = value / 16
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(oz, " -> ", ton)
                        conversion = value / 32000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 5. Stone
                elif start_unit == 'st':
                    if end_unit == 'kg':
                        print(st, " -> ", kg)
                        conversion = value * 6.35
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(st, " -> ", mg)
                        conversion = value * 6350000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(st, " -> ", g)
                        conversion = value * 6350
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(st, " -> ", oz)
                        conversion = value * 224
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(st, " -> ", st)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(st, " -> ", lbs)
                        conversion = value * 14
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(st, " -> ", ton)
                        conversion = value / 143
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 6. Pounds
                elif start_unit == 'lbs':
                    if end_unit == 'kg':
                        print(lbs, " -> ", kg)
                        conversion = value / 2.205
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(lbs, " -> ", mg)
                        conversion = value * 453592
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(lbs, " -> ", g)
                        conversion = value * 454
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(lbs, " -> ", oz)
                        conversion = value * 16
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(lbs, " -> ", st)
                        conversion = value / 14
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(lbs, " -> ", lbs)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(lbs, " -> ", ton)
                        conversion = value / 2000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # 7. Ton
                elif start_unit == 'ton':
                    if end_unit == 'kg':
                        print(ton, " -> ", kg)
                        conversion = value * 907
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kg)
                    elif end_unit == 'mg':
                        print(ton, " -> ", mg)
                        conversion = value * 970200000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mg)
                    elif end_unit == 'g':
                        print(ton, " -> ", g)
                        conversion = value * 907185
                        conversion = numpy.around(conversion, 4)
                        print(conversion, g)
                    elif end_unit == 'oz':
                        print(ton, " -> ", oz)
                        conversion = value * 32000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, oz)
                    elif end_unit == 'st':
                        print(ton, " -> ", st)
                        conversion = value * 143
                        conversion = numpy.around(conversion, 4)
                        print(conversion, st)
                    elif end_unit == 'lbs':
                        print(ton, " -> ", lbs)
                        conversion = value * 2000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, lbs)
                    elif end_unit == 'ton':
                        print(ton, " -> ", ton)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ton)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    weight()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return weight()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return weight()

    # 6. Temperature
    def temperature():
        if command == 'tp' or command == '6':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: c k 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Fahrenheit (F)  2. Celsius (C)\n"
                      "  3. Kelvin (K)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                f = "Fahrenheit (F\u00b0)"
                c = "Celsius (C\u00b0)"
                k = "Kelvin (K\u00b0)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # 1. Fahrenheit
                if start_unit == 'f':
                    if end_unit == 'f':
                        print(f, " -> ", f)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, f)
                    elif end_unit == 'c':
                        print(f, " -> ", c)
                        conversion = (value - 32) * (5 / 9)
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                    elif end_unit == 'k':
                        print(f, " -> ", k)
                        conversion = (value - 32) * (5 / 9) + 273.15
                        conversion = numpy.around(conversion, 4)
                        print(conversion, k)
                # 2. Celsius
                elif start_unit == 'c':
                    if end_unit == 'f':
                        print(c, " -> ", f)
                        conversion = (value * (9 / 5)) + 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, f)
                    elif end_unit == 'c':
                        print(c, " -> ", c)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                    elif end_unit == 'k':
                        print(c, " -> ", k)
                        conversion = value + 273.15
                        conversion = numpy.around(conversion, 4)
                        print(conversion, k)
                # 3. Kelvin
                elif start_unit == 'k':
                    if end_unit == 'f':
                        print(k, " -> ", f)
                        conversion = (value - 273.15) * (9 / 5) + 32
                        conversion = numpy.around(conversion, 4)
                        print(conversion, f)
                    elif end_unit == 'c':
                        print(k, " -> ", c)
                        conversion = value - 273.15
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                    elif end_unit == 'k':
                        print(k, " -> ", k)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, k)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    temperature()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return temperature()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return temperature()

    # 7. Frequency
    def frequency():
        if command == 'f' or command == '7':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: hz mhz 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Kilohertz (kHz)  2. Hertz (Hz) \n"
                      "  3. Megahertz (MHz)  4. Gigahertz (GHz)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0]
                end_unit = selection[1]
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                khz = "Kilohertz (kHz)"
                hz = "Hertz (Hz)"
                mhz = "Megahertz (MHz)"
                ghz = "Gigahertz (GHz)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # frequency conversions
                # 1. Kilohertz
                if start_unit == 'khz':
                    if end_unit == 'khz':
                        print(khz, " -> ", khz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, khz)
                    elif end_unit == 'hz':
                        print(khz, " -> ", hz)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hz)
                    elif end_unit == 'mhz':
                        print(khz, " -> ", mhz)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mhz)
                    elif end_unit == 'ghz':
                        print(khz, " -> ", ghz)
                        conversion = value / 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ghz)
                # 2. Hertz
                elif start_unit == 'hz':
                    if end_unit == 'khz':
                        print(hz, " -> ", khz)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, khz)
                    elif end_unit == 'hz':
                        print(hz, " -> ", hz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hz)
                    elif end_unit == 'mhz':
                        print(hz, " -> ", mhz)
                        conversion = value / 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mhz)
                    elif end_unit == 'ghz':
                        print(hz, " -> ", ghz)
                        conversion = value / 1000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ghz)
                # 3. Megahertz
                elif start_unit == 'mhz':
                    if end_unit == 'khz':
                        print(mhz, " -> ", khz)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, khz)
                    elif end_unit == 'hz':
                        print(mhz, " -> ", hz)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hz)
                    elif end_unit == 'mhz':
                        print(mhz, " -> ", mhz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mhz)
                    elif end_unit == 'ghz':
                        print(mhz, " -> ", ghz)
                        conversion = value / 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ghz)
                # 4. Gigahertz
                elif start_unit == 'ghz':
                    if end_unit == 'khz':
                        print(ghz, " -> ", khz)
                        conversion = value * 1000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, khz)
                    elif end_unit == 'hz':
                        print(ghz, " -> ", hz)
                        conversion = value * 1000000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hz)
                    elif end_unit == 'mhz':
                        print(ghz, " -> ", mhz)
                        conversion = value * 1000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mhz)
                    elif end_unit == 'ghz':
                        print(ghz, " -> ", ghz)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ghz)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    frequency()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return frequency()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return frequency()

    # 8. Speed
    def speed():
        if command == 's' or command == '8':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: ms kph 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Miles Per Hour (mph)       2. Feet Per Second (fs)\n"
                      "  3. Kilometers Per Hour (kph)  4. Meters Per Second (ms)")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                mph = "Miles Per Hour (mph)"
                kph = "Kilometers Per Hour (km/h)"
                fs = "Feet Per Second (f/s)"
                ms = "Meters Per Second (m/s)"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # speed conversions
                # 1. Miles Per Hour
                if start_unit == 'mph':
                    if end_unit == 'mph':
                        print(mph, " -> ", mph)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mph)
                    elif end_unit == 'kph':
                        print(mph, " -> ", kph)
                        conversion = value * 1.609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kph)
                    elif end_unit == 'fs':
                        print(mph, " -> ", fs)
                        conversion = value * 1.467
                        conversion = numpy.around(conversion, 4)
                        print(conversion, fs)
                    elif end_unit == 'ms':
                        print(mph, " -> ", ms)
                        conversion = value / 2.237
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ms)
                # 2. Kilometers Per Hour
                elif start_unit == 'kph':
                    if end_unit == 'mph':
                        print(kph, " -> ", mph)
                        conversion = value / 1.609
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mph)
                    elif end_unit == 'kph':
                        print(kph, " -> ", kph)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kph)
                    elif end_unit == 'fs':
                        print(kph, " -> ", fs)
                        conversion = value / 1.097
                        conversion = numpy.around(conversion, 4)
                        print(conversion, fs)
                    elif end_unit == 'ms':
                        print(kph, " -> ", ms)
                        conversion = value / 3.6
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ms)
                # 3. Feet Per Second
                elif start_unit == 'fs':
                    if end_unit == 'mph':
                        print(fs, " -> ", mph)
                        conversion = value / 1.467
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mph)
                    elif end_unit == 'kph':
                        print(fs, " -> ", kph)
                        conversion = value * 1.097
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kph)
                    elif end_unit == 'fs':
                        print(fs, " -> ", fs)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, fs)
                    elif end_unit == 'ms':
                        print(fs, " -> ", ms)
                        conversion = value / 3.281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ms)
                # 4. Meters Per Second
                elif start_unit == 'ms':
                    if end_unit == 'mph':
                        print(ms, " -> ", mph)
                        conversion = value * 2.237
                        conversion = numpy.around(conversion, 4)
                        print(conversion, mph)
                    elif end_unit == 'kph':
                        print(ms, " -> ", kph)
                        conversion = value * 3.6
                        conversion = numpy.around(conversion, 4)
                        print(conversion, kph)
                    elif end_unit == 'fs':
                        print(ms, " -> ", fs)
                        conversion = value * 3.281
                        conversion = numpy.around(conversion, 4)
                        print(conversion, fs)
                    elif end_unit == 'ms':
                        print(ms, " -> ", ms)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, ms)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    speed()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return speed()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values. ")
                return speed()

    # 9. Time
    def time():
        if command == 'ti' or command == '9':
            try:
                # user input
                print(Fore.BLUE + "\033[1m Which unit are you converting from? Which unit would "
                                  "you like to convert to? \n Enter the values you would like to use after. "
                                  "Separate by spaces. (Ex: ms kph 45 23.6 -27) \n\033[0m" + Fore.WHITE +
                      "  0. Back to main menu\n" + Fore.MAGENTA +
                      "  1. Seconds (s)   2. Minutes (min)\n"
                      "  3. Hours (hr)    4. Days (da)\n"
                      "  5. Weeks (wk)    6. Months (m)\n"
                      "  7. Years (yr)    8. Decades (de)\n"
                      "  9. Centuries (c) ")
                selection = input(Fore.YELLOW + "Enter Selection >> ").split(" ")
                if selection[0] == '0':
                    return main()
                else:
                    pass
                start_unit = selection[0].lower()
                end_unit = selection[1].lower()
                value = list(map(float, selection[2:]))
                value = numpy.array(value)
                # names
                s = "Seconds (s)"
                min = "Minutes (min)"
                hr = "Hours (hr)"
                da = "Days"
                wk = "Weeks"
                m = "Months"
                yr = "Years (yr)"
                de = "Decades"
                c = "Centuries"
                # original values
                print(Fore.WHITE + "\nOriginal Values: ", value, Fore.GREEN)
                # time conversions
                # 1. Seconds
                if start_unit == 's':
                    if end_unit == 's':
                        print(s, " -> ", s)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(s, " -> ", min)
                        conversion = value / 60
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(s, " -> ", hr)
                        conversion = value / 3600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(s, " -> ", da)
                        conversion = value / 86400
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(s, " -> ", wk)
                        conversion = value / 604800
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(s, " -> ", m)
                        conversion = value / 2628000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(s, " -> ", yr)
                        conversion = value / 31540000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(s, " -> ", de)
                        conversion = value / 315400000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(s, " -> ", c)
                        conversion = value / 3154000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 2. Minutes
                elif start_unit == 'min':
                    if end_unit == 's':
                        print(min, " -> ", s)
                        conversion = value * 60
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(min, " -> ", min)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(min, " -> ", hr)
                        conversion = value / 60
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(min, " -> ", da)
                        conversion = value / 1440
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(min, " -> ", wk)
                        conversion = value / 10080
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(min, " -> ", m)
                        conversion = value / 43800
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(min, " -> ", yr)
                        conversion = value / 525600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(min, " -> ", de)
                        conversion = value / 5256000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(min, " -> ", c)
                        conversion = value / 52560000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 3. Hours
                elif start_unit == 'hr':
                    if end_unit == 's':
                        print(hr, " -> ", s)
                        conversion = value * 3600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(hr, " -> ", min)
                        conversion = value * 60
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(hr, " -> ", hr)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(hr, " -> ", da)
                        conversion = value / 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(hr, " -> ", wk)
                        conversion = value / 168
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(hr, " -> ", m)
                        conversion = value / 730
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(hr, " -> ", yr)
                        conversion = value / 8760
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(hr, " -> ", de)
                        conversion = value / 87600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(hr, " -> ", c)
                        conversion = value / 876000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 4. Days
                elif start_unit == 'da':
                    if end_unit == 's':
                        print(da, " -> ", s)
                        conversion = value * 86400
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(da, " -> ", min)
                        conversion = value * 1440
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(da, " -> ", hr)
                        conversion = value * 24
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(da, " -> ", da)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(da, " -> ", wk)
                        conversion = value / 7
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(da, " -> ", m)
                        conversion = value / 30.417
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(da, " -> ", yr)
                        conversion = value / 365
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(da, " -> ", de)
                        conversion = value / 3650
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(da, " -> ", c)
                        conversion = value / 36500
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 5. Weeks
                elif start_unit == 'wk':
                    if end_unit == 's':
                        print(wk, " -> ", s)
                        conversion = value * 604800
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(wk, " -> ", min)
                        conversion = value * 10080
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(wk, " -> ", hr)
                        conversion = value * 168
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(wk, " -> ", da)
                        conversion = value * 7
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(wk, " -> ", wk)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(wk, " -> ", m)
                        conversion = value / 4.345
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(wk, " -> ", yr)
                        conversion = value / 52.143
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(wk, " -> ", de)
                        conversion = value / 521
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(wk, " -> ", c)
                        conversion = value / 5214
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 6. Months
                elif start_unit == 'm':
                    if end_unit == 's':
                        print(m, " -> ", s)
                        conversion = value * 2628000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(m, " -> ", min)
                        conversion = value * 43800
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(m, " -> ", hr)
                        conversion = value * 730
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(m, " -> ", da)
                        conversion = value * 30.417
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(m, " -> ", wk)
                        conversion = value * 4.345
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(m, " -> ", m)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(m, " -> ", yr)
                        conversion = value / 12
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(m, " -> ", de)
                        conversion = value / 120
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(m, " -> ", c)
                        conversion = value / 1200
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 7. Years
                elif start_unit == 'yr':
                    if end_unit == 's':
                        print(yr, " -> ", s)
                        conversion = value * 31540000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(yr, " -> ", min)
                        conversion = value * 525600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(yr, " -> ", hr)
                        conversion = value * 8760
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(yr, " -> ", da)
                        conversion = value * 365
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(yr, " -> ", wk)
                        conversion = value * 52.143
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(yr, " -> ", m)
                        conversion = value * 12
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(yr, " -> ", yr)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(yr, " -> ", de)
                        conversion = value / 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(yr, " -> ", c)
                        conversion = value / 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 8. Decades
                elif start_unit == 'de':
                    if end_unit == 's':
                        print(de, " -> ", s)
                        conversion = value * 315400000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(de, " -> ", min)
                        conversion = value * 5256000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(de, " -> ", hr)
                        conversion = value * 87600
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(de, " -> ", da)
                        conversion = value * 3650
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(de, " -> ", wk)
                        conversion = value * 521
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(de, " -> ", m)
                        conversion = value * 120
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(de, " -> ", yr)
                        conversion = value * 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(de, " -> ", de)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(de, " -> ", c)
                        conversion = value / 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # 9. Centuries
                elif start_unit == 'c':
                    if end_unit == 's':
                        print(c, " -> ", s)
                        conversion = value * 3154000000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, s)
                    elif end_unit == 'min':
                        print(c, " -> ", min)
                        conversion = value * 52560000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, min)
                    elif end_unit == 'hr':
                        print(c, " -> ", hr)
                        conversion = value * 876000
                        conversion = numpy.around(conversion, 4)
                        print(conversion, hr)
                    elif end_unit == 'da':
                        print(c, " -> ", da)
                        conversion = value * 36500
                        conversion = numpy.around(conversion, 4)
                        print(conversion, da)
                    elif end_unit == 'wk':
                        print(c, " -> ", wk)
                        conversion = value * 5214
                        conversion = numpy.around(conversion, 4)
                        print(conversion, wk)
                    elif end_unit == 'm':
                        print(c, " -> ", m)
                        conversion = value * 1200
                        conversion = numpy.around(conversion, 4)
                        print(conversion, m)
                    elif end_unit == 'yr':
                        print(c, " -> ", yr)
                        conversion = value * 100
                        conversion = numpy.around(conversion, 4)
                        print(conversion, yr)
                    elif end_unit == 'de':
                        print(c, " -> ", de)
                        conversion = value * 10
                        conversion = numpy.around(conversion, 4)
                        print(conversion, de)
                    elif end_unit == 'c':
                        print(c, " -> ", c)
                        conversion = value * 1
                        conversion = numpy.around(conversion, 4)
                        print(conversion, c)
                # Error
                else:
                    print(Fore.RED + "Please enter valid abbreviations and values.  ")
                    time()
            except ValueError:
                print(Fore.RED + "Please enter valid abbreviations and values.  ")
                return time()
            except IndexError:
                print(Fore.RED + "Please enter valid abbreviations and values. ")
                return time()

    # All Functions
    command = begin()
    length()
    area()
    volume()
    liquidVolume()
    weight()
    temperature()
    frequency()
    speed()
    time()


# Start Program
if __name__ == '__main__':
    main()
    while True:
        print(Fore.BLUE + "\n\033[1m Would you like to do another conversion?\n\033[0m" +
              Fore.MAGENTA + "  1. Yes\n  2. No")
        try:
            redo = input(Fore.WHITE + ">> ").lower()
            if redo == '1' or redo == 'yes':
                main()
            elif redo == '2' or redo == 'no':
                print(Fore.YELLOW + "\n\033[1m Done!")
                break
            else:
                print(Fore.RED + " Please enter a value 1-2")
        except ValueError:
            print(Fore.RED + " Please enter a value 1-2")
