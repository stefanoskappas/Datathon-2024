# Δήλωση της βιβλιοθήκης που χειρίζεται τα CSV αρχεία.
import csv
import matplotlib.pyplot as plt
import numpy as np
# Άνοιγμα ενός CSV αρχείου για διάβασμα.
file = open ("datafile.csv", "r")
# Πίνακες που αποθηκεύουν γραμμές, λέξεις, κελιά, στήλες του CSV αρχείου.
ROWS = []
words = ""
CELLS = []
index = 0
COL1 = []
COL2 = []
COL3 = []
COL4 = []
COL5 = []
number_of_rows = 0
# Αποθήκευση του CSV αρχείου στον πίνακα γραμμών
for row in file:
    index += 1
    if index > 1:
        ROWS.append(row)
        number_of_rows += 1
# Αποθήκευση του CSV αρχείου στον πίνακα κελιών
for row in ROWS:
    for col in row:
        if col == ',' or col == '\n':
            CELLS.append(words)
            words = ""
        else: 
            words += col
# Αποθήκευση του CSV αρχείου σε πίνακα στηλών και μορφοποίηση σε αριθμούς.
index = 0
for row in CELLS:
    index += 1
    if (index % 5) == 1:
        COL1.append(int(row))
    if (index % 5) == 2:
        if row == "":
            COL2.append(0.0)
        else:
            COL2.append(float(row))
    if (index % 5) == 3:
        # Εμφάνιση ακρίβειας δευτερολέπτου ημερομηνίας.
        indexcol = 0
        str = ""
        for col in row:
            indexcol += 1
            if indexcol < 20:
                str += col
                #print (col)
            else:
                COL3.append(str)
    if (index % 5) == 4:
        COL4.append(float(row))
    if (index % 5) == 0:
        COL5.append(float(row))
print(COL3)
# Εύρεση των μεγίστων τιμών ανά στήλη.
maxcol1 = 0.0
maxcol2 = 0.0
maxcol3 = ""
maxcol4 = 0.0
maxcol5 = 0.0
rrow1 = 0
rrow2 = 0
rrow4 = 0
rrow5 = 0
for row in range(0, number_of_rows):
    if COL1[row] > maxcol2:
        maxcol1 = COL1[row]
        rrow1 = row
    if COL2[row] == 1:
        maxcol2 += 1.0
    if COL2[row] == 2:
        maxcol2 -= 1.0
    if COL3[row] > maxcol3:
        maxcol3 = COL3[row]
    if COL4[row] > maxcol4:
        maxcol4 = COL4[row]
    if COL5[row] > maxcol5:
        maxcol5 = COL5[row]
        rrow5 = row
# Τροποποίηση του πίνακα με τις κατευθύνσεις σε εύγλωττη μορφή.
if maxcol2 > 0: maxcol2 = "from-to"
else: maxcol2 = "to-from"
if COL2[rrow1] > 0: COL2[rrow1] = "from-to"
else: COL2[rrow1] = "to-from"
if COL2[rrow2] > 0: COL2[rrow2] = "from-to"
else: COL2[rrow2] = "to-from"
if COL2[rrow4] > 0: COL2[rrow4] = "from-to"
else: COL2[rrow4] = "to-from"
if COL2[rrow5] > 0: COL2[rrow5] = "from-to"
else: COL2[rrow5] = "to-from"
# Εμφάνιση των αποτελεσμάτων των μέγιστων τιμών ανά κατηγορία.
print("Maximum road link =", maxcol1, ", Direction =", COL2[rrow1], ", Average speed =", COL4[rrow1], "km\h", ", Number of unique datapoints from cars ", COL5[rrow1])
print("Frequent direction =", maxcol2)
print("Latest traffic record =", maxcol3)
print("Maximum average speed =", maxcol4, "km\h", "Road link =", COL1[rrow4], "Timestamp =", COL3[rrow4], ", Average speed per track =", COL4[rrow4])
print("Number of unique datapoints from cars =", maxcol5, "Road link =", COL1[rrow5], ", Direction =". COL2[rrow5], ", Timestamp =", COL3[rrow5], ", Average speed =", COL4[rrow5])
# Ταξινόμηση των χρόνων.
COL3.sort()
for row in COL3:
    print(row)
# Διαγράμματα.
plt.plot(COL1, COL2)
plt.show()
plt.plot(COL4, COL5)
plt.show()
plt.plot(COL3, COL5)
plt.show()
plt.plot(COL4, COL5)
plt.show()