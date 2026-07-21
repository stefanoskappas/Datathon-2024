"""
    Εμείς θέλουμε το πρόγραμμα να βγάζει τα αποτελέσματα από δεδομένα κυκλοφορίας οχημάτων. Πιο συγκεκριμένα θα δέχεται τα
    ορίσματα id δρόμου, κατεύθυνση, ημερομηνία και ώρα καταγραφής, μέση ταχύτητα οχημάτων, αριθμός οχημάτων την δεδομένη χρονική
    στιγμή καταγραφής. Τα πρόγραμμα θα βρεί τον πιο πολυσύχναστο δρόμο (αυτός με τις περισσότερες καταγραφές) και στην συνέχεια 
    θα εμφανίσει τα αποτελέσματα για το id του πιο πολυσύχναστου δρόμου, την πιο συχνή κατεύθυνση των οχημάτων, την μέση 
    ταχύτητα που αναπτύσσουν, τον αριθμό των οχημάτων που διασχίζουν αυτό τον δρόμο (τόσο για τον πολυσύχναστο όσο και 
    γενικότερα). Τέλος θα εμφανίσει την ημερομηνία και ώρα της τελευταίας καταγραφής που έγινε, την μεγαλύτερη μέγιστη ταχύτητα 
    των οχημάτων, και τον μέγιστο αριθμό των οχημάτων που καταγράφηκαν την δεδομένη στιγμή (για όλη την καταγραφή). 
"""
# Δήλωση της βιβλιοθήκης που χειρίζεται τα CSV αρχεία.
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# Άνοιγμα ενός CSV αρχείου για διάβασμα.
file = open ("datafile.csv", "r", encoding="utf-8")
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
# Αποθήκευση του CSV αρχείου στον πίνακα γραμμών.
for row in file:
    index += 1
    if index > 1:
        ROWS.append(row)
        number_of_rows += 1
# Αποθήκευση του CSV αρχείου στον πίνακα κελιών.
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
            COL2.append(int(row))
    if (index % 5) == 3:
        # Εμφάνιση ακρίβειας δευτερολέπτου ημερομηνίας.
        indexcol = 0
        str = ""
        for col in row:
            indexcol += 1
            if indexcol < 19:
                str += col
            else:
                str += col
                COL3.append(str)
    if (index % 5) == 4:
        COL4.append(float(row))
    if (index % 5) == 0:
        COL5.append(int(row))
# Ταξινόμηηση του πίνακα ως προς το πεδίο Link_ID σε περίπτωση που το αρχείο είναι μη ταξινομημένο.
def tros(arg):
    for row in range (0, number_of_rows):
        for col in range(row+1, number_of_rows):
            if arg[col] < arg[row]:
                temp1 = COL1[col]
                COL1[col] = COL1[row]
                COL1[row] = temp1
                temp2 = COL2[col]
                COL2[col] = COL2[row]
                COL2[row] = temp2
                temp3 = COL3[col]
                COL3[col] = COL3[row]
                COL3[row] = temp3
                temp4 = COL4[col]
                COL4[col] = COL4[row]
                COL4[row] = temp4
                temp5 = COL5[col]
                COL5[col] = COL5[row]
                COL5[row] = temp5
tros(COL1)
# Μεταβλητές που θα μας χρησιμεύσουν στους υπολογισμούς.
maxcol1 = 0
maxcol2 = 0
mincol2 = 0
maxcol3 = ""
maxcol4 = 0.0
mincol4 = 0.0
maxcol5 = 0
mincol5 = 0
rrow = []
max = 0
maxspeed = 0
maxcars = 0
# Εύρεση των μέγιστων τιμών ανά στήλη.
for row in range(1, number_of_rows):
    maxcol1 += 1
    if COL1[row] != COL1[row-1] or row == number_of_rows - 1:
        rrow.append(maxcol1)
        rrow.append(COL1[row-1])
        maxcol1 = 1
# Εύρεση του πιο πολυσύγχναστου Link_Id.
for row in range(0, len(rrow), 2):
    if rrow[row] > maxcol1:
        maxcol1 = rrow[row+1]
        max = rrow[row]
# Εύρεση των αποτελεσμάτων που ψάχνουμε.
for row in range(0, number_of_rows):
    if COL1[row] == maxcol1:
        if COL2[row] == 1:
            maxcol2 += 1
        else:
            maxcol2 -= 1
        maxcol4 += COL4[row]
        maxcol5 += COL5[row]
    if COL2[row] == 1:
        mincol2 += 1
    else: 
        mincol2 -= 1
    if COL3[row] > maxcol3:
        maxcol3 = COL3[row]
    mincol4 += COL4[row]
    if COL4[row] > maxspeed:
        maxspeed = COL4[row]
    mincol5 += COL5[row]
    if COL5[row] > maxcars:
        maxcars = COL5[row]
maxcol4 = maxcol4 / max
mincol4 = mincol4 / number_of_rows
# Τροποποίηση του πίνακα με τις κατευθύνσεις σε εύγλωττη μορφή.
if maxcol2 > 0: 
    maxcol2 = "from-to"
else: 
    maxcol2 = "to-from"
if mincol2 > 0:
    mincol2 = "from-to"
else:
    mincol2 = "to-from"
# Εμφάνιση των αποτελεσμάτων των μέγιστων τιμών ανά κατηγορία.
print("Maximum road link =", maxcol1, ", Direction =", maxcol2, ", Average speed =", maxcol4, "km\h, Number of unique datapoints from cars =", maxcol5)
print("Generally, the Frequent direction =", mincol2, ", Average speed =", mincol4, "km\h, Number of unique datapoints from cars =", mincol5)
print("Latest traffic record =", maxcol3, ", Maximum average speed =", maxspeed, "km\h, Maximum number of unique datapoints from cars =", maxcars)
# Προετοιμασία των διαγραμμάτων.
LOC = []
TOFROM = [0, 0]
fromto_points = []
tofrom_points = []
for row in range (0, number_of_rows):
    if COL1[row] != COL1[row-1]:
        LOC.append(COL1[row])
for row in range(0, len(LOC)):
    index = 0
    TOFROM = [0, 0]
    for col in range(0, number_of_rows):
        if COL1[col] == LOC[row-1]:
            if COL2[col] == 1:
                TOFROM[0] += 1
            else:
                TOFROM[1] += 1
    fromto_points.append(TOFROM[0])
    tofrom_points.append(TOFROM[1])
# Πίνακας συσχέτισης του αριθμού των from-to και to-from διαδρομών ανά οδό.
plt.title("Αριθμός των from-to με to-from όλων των οδών.")
plt.xlabel("Αριθμός των from-to καταγραφών")
plt.ylabel("Αριθμός των to-from καταγραφών")
for row in range(0, len(LOC)):
    plt.plot(fromto_points[row], tofrom_points[row], "o")
plt.legend(LOC)
plt.show()
# Πίνακας συσχέτισης του αριθμού των καταγεγραμμένων οχημάτων ανά οδό.
fromto_points = []
for row in range(0, len(LOC)):
    TOFROM = [0, 0]
    for col in range(0, number_of_rows):
        if COL1[col] == LOC[row-1]:
            TOFROM[0] += COL5[col]
    fromto_points.append(TOFROM[0])
plt.title("Αριθμός των καταγραμμένων οχημάτων ως προς το Link_ID των δρόμων.")
plt.xlabel("Link_ID δρόμων")
plt.ylabel("Αριθμός καταγεγραμμένων οχημάτων")
plt.bar(LOC, fromto_points, width = 0.1)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
# Πίνακας συσχέτισης της μέσης ταχύτητας των οχημάτων ανά καταγραφή σε αύξουσα χρονική σειρά.
tros(COL3)
plt.title("Συσχέτιση της μέσης ταχύτητας των οχημάτων ανά χρονική περίοδο.")
plt.xlabel("Ώρα")
plt.ylabel("Μέση ταχύτητα")
short_labels = [label[-8:] for label in COL3]
plt.yticks(range(len(COL3)), short_labels)
plt.plot(COL4, COL3)
ax = plt.gca()
ax.yaxis.set_major_locator(ticker.MultipleLocator(3))
plt.show()
