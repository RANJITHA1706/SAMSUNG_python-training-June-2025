'''
$ python program2.py "meghalaya shillong" "manipur imphal" "mizoram aizal" "tripura agartala" "nagaland kohima"

states = []
capitals = list()

STATE      CAPITAL
-------------------

'''
import sys

states = []
capitals = []

print("%-15s %-12s" % ("States", "Capital"))
print("-" * 27)
list1 = [sys.argv[i].split() for i in range(len(sys.argv))]
for i in range(1, len(sys.argv)):
    parts = sys.argv[i].split()
    if len(parts) == 2:
        states.append(parts[0])
        capitals.append(parts[1])
for i in range(len(states)):
    print("%-15s %-12s" % (states[i], capitals[i]))
