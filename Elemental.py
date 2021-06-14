import sys
p1 = ['H', 'He']
p2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
p3 = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
p4 = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
p5 = ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']
p6 = ['Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
p7 = ['Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']

g1 = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
g2 = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
g3 = ['Sc', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ac','Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es',  'Fm', 'Md', 'No', 'Lr']
g4 = ['Ti', 'Zr', 'Hf']
g5 = ['V', 'Nb', 'Ta']
g6 = ['Cr', 'Mo', 'W']
g7 = ['Mn', 'Tc', 'Re']
g8 = ['Fe', 'Ru', 'Os']
g9 = ['Co', 'Rh', 'Ir']
g10 = ['Ni', 'Pd', 'Pt']
g11 = ['Cu', 'Ag', 'Au']
g12 = ['Zn', 'Cd', 'Hg']
g13 = ['B', 'Al', 'Ga', 'In', 'Tl']
g14 = ['C', 'Si', 'Ge', 'Sn', 'Pb']
g15 = ['N', 'P', 'As', 'Sb', 'Bi']
g16 = ['O', 'S', 'Se', 'Te', 'Po']
g17 = ['F', 'Cl', 'Br', 'I', 'At']
g18 = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']

elemNameList = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Proctinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadium', 'Roentgenium', 'Copernicium']

allElements = p1 + p2 + p3 + p4 + p5 + p6 + p7

print("This Program Gives Information about the Element you enter.")
print("Note : This program is made for elements 1 to 103.")

while True:
    print("")
    print("")
    print("New Element (:+:)----------------------------------------------------(:+:)")
    print("")
    print("Type the Symbol of the Element you want to know about : ")
    print("Or Type 'Q' to Quit : ")
    elem = input()
    if elem == "Q" or elem == "q":
        sys.exit("Program Completed.")

    elemIndex = allElements.index(elem)
    aN = allElements.index(elem) + 1
    elemName = elemNameList[elemIndex]

    if elem in p1 :
        period = 1
    elif elem in p2:
        period = 2
    elif elem in p3:
        period = 3
    elif elem in p4:
        period = 4
    elif elem in p5:
        period = 5
    elif elem in p6:
        period = 6
    elif elem in p7:
        period = 7

    if elem in g1:
        group = 1
    elif elem in g2:
        group = 2
    elif elem in g3:
        group = 3
    elif elem in g4:
        group = 4
    elif elem in g5:
        group = 5
    elif elem in g6:
        group = 6
    elif elem in g7:
        group = 7
    elif elem in g8:
        group = 8
    elif elem in g9:
        group = 9
    elif elem in g10:
        group = 10
    elif elem in g11:
        group = 11
    elif elem in g12:
        group = 12
    elif elem in g13:
        group = 13
    elif elem in g14:
        group = 14
    elif elem in g15:
        group = 15
    elif elem in g16:
        group = 16
    elif elem in g17:
        group = 17
    elif elem in g18:
        group = 18

    print("")
    print("(+) Element       : ", elemName)
    print("(+) Group         : ", group)
    print("(+) Period        : ", period)
    print("(+) Atomic Number : ", aN)

    if aN <= 2 :
        n1_1 = aN
        eC = "1s[" + str(n1_1) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[" + str(n1_1) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 10 :
        n2 = aN - 2
        if n2 <= 2:
            n2_1 = n2
            n2_2 = 0
        elif n2 <= 8:
            n2_1 = 2
            n2_2 = n2 - 2
        eC = "[He]2s[" + str(n2_1) + "]2p[" + str(n2_2) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[" + str(n2_1) + "]2p[" + str(n2_2) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 18:
        n3 = aN - 10
        if n3 <= 2:
            n3_1 = n3
            n3_2 = 0
        elif n3 <= 8:
            n3_1 = 2
            n3_2 = n3 - 2
        eC = "[Ne]3s[" + str(n3_1) + "]3p[" + str(n3_2) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[2]2p[6]")
        print("         3rd Shell : ", "3s[" + str(n3_1) + "]3p[" + str(n3_2) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 36:
        n4 = aN - 18
        if 1 <= n4 <= 2:
            n4_1 = n4
            n3_3 = 0
            n4_2 = 0
        elif 3 <= n4 <= 12:
           n4_1 = 2
           n3_3 = n4 - 2
           n4_2 = 0
           if n3_3 == 4 or n3_3 == 9:
               n4_1 = n4_1 - 1
               n3_3 = n3_3 + 1
               n4_2 = 0
        elif 13 <= n4 <= 18:
            n4_1 = 2
            n3_3 = 10
            n4_2 = n4 - 12
        eC = "[Ar]4s[" + str(n4_1) + "]3d[" + str(n3_3) + "]4p[" + str(n4_2) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[2]2p[6]")
        print("         3rd Shell : ", "3s[2]3p[6]3d[" + str(n3_3) + "]")
        print("         4th Shell : ", "4s[" + str(n4_1) + "]4p[" + str(n4_2) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 54:
        n5 = aN - 36
        if 1 <= n5 <= 2:
            n5_1 = n5
            n4_3 = 0
            n5_2 = 0
        elif 3 <= n5 <= 12:
            n5_1 = 2
            n4_3 = n5 - 2
            n5_2 = 0
            if 3 <= n4_3 <= 4 or 6 <= n4_3 <= 7 or n4_3 == 9:
                n5_1 = 1
                n4_3 = n4_3 + 1
                n5_2 = 0
            elif n4_3 == 8:
                n5_1 = 0
                n4_3 = n4_3 + 2
                n5_2 = 0
        elif 13 <= n5 <= 18:
            n5_1 = 2
            n4_3 = 10
            n5_2 = n5 - 12
        eC = "[Kr]5s[" + str(n5_1) + "]4d[" + str(n4_3) + "]5p[" + str(n5_2) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[2]2p[6]")
        print("         3rd Shell : ", "3s[2]3p[6]3d[10]")
        print("         4th Shell : ", "4s[2]4p[6]4d[" + str(n4_3) + "]")
        print("         5th Shell : ", "5s[" + str(n5_1) + "]5p[" + str(n5_2) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 86:
        n6 = aN - 54
        if 1 <= n6 <= 2:
            n6_1 = n6
            n4_4 = 0
            n5_3 = 0
            n6_2 = 0
        elif 3 <= n6 <= 26:
            n6_1 = 2
            n4_4 = n6 - 2
            n5_3 = 0
            n6_2 = 0
            if n4_4 == 1 or n4_4 == 8:
                n6_1 = 2
                n4_4 = n4_4 - 1
                n5_3 = 1
                n6_2 = 0
            elif n4_4 >= 14:
                n6_1 = 2
                n5_3 = n4_4 - 14
                n4_4 = 14
                n6_2 = 0
                if n5_3 == 8 or n5_3 == 9:
                    n6_1 = 1
                    n4_4 = 14
                    n5_3 = n5_3 + 1
                    n6_2 = 0
        elif 27 <= n6 <= 32:
            n6_1 = 2
            n4_4 = 14
            n5_3 = 10
            n6_2 = n6 - 26
        eC = "[Xe]6s[" + str(n6_1) + "]4f[" + str(n4_4) + "]5d[" + str(n5_3) + "]6p[" + str(n6_2) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[2]2p[6]")
        print("         3rd Shell : ", "3s[2]3p[6]3d[10]")
        print("         4th Shell : ", "4s[2]4p[6]4d[10]4f[" + str(n4_4) + "]")
        print("         5th Shell : ", "5s[2]5p[6]5d[" + str(n5_3) + "]")
        print("         6th Shell : ", "6s[" + str(n6_1) + "]6p[" + str(n6_2) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")
    elif aN <= 103:
        n7 = aN - 86
        if n7 == 1 or n7 == 2:
            n7_1 = n7
            n5_4 = 0
            n6_3 = 0
        elif 3 <= n7 <= 17:
            n7_1 = 2
            n5_4 = n7 - 2
            n6_3 = 0
            if n5_4 == 1 or 3 <= n5_4 <= 5 or n5_4 == 8:
                n7_1 = 2
                n5_4 = n5_4 - 1
                n6_3 = 1
            elif n5_4 == 2:
                n7_1 = 2
                n5_4 = 0
                n6_3 = 2
            elif n5_4 >= 14 :
                n7_1 = 2
                n6_3 = n5_4 - 14
                n5_4 = 14
        eC = "[Rn]7s[" + str(n7_1) + "]5f[" + str(n5_4) + "]6d[" + str(n6_3) + "]"
        print("(+) Electronic Configuration : ", eC)
        print("(+) More Elaboration of Electronic Configuration :")
        print("         1st Shell : ", "1s[2]")
        print("         2nd Shell : ", "2s[2]2p[6]")
        print("         3rd Shell : ", "3s[2]3p[6]3d[10]")
        print("         4th Shell : ", "4s[2]4p[6]4d[10]4f[14]")
        print("         5th Shell : ", "5s[2]5p[6]5d[10]5f[" + str(n5_4) + "]")
        print("         6th Shell : ", "6s[2]6p[6]6d[" + str(n6_3) + "]")
        print("         7th Shell : ", "7s[" + str(n7_1) + "]")
        print("")
        print("(:+:) Created by Muhriz Ali.")

