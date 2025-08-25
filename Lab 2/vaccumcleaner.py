print("shreyas t s,1BM23CS322")
def vacuum_cleaner_agent():
    # Take initial inputs
    state_A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
    state_B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
    location = input("Enter location (A or B): ").upper()

    cost = 0
    states = {'A': state_A, 'B': state_B}

    if states['A'] == 0 and states['B'] == 0:
        print("Turning vacuum off")
        print(f"Cost: {cost}")
        print(states)
        return

    def clean_location(loc):
        nonlocal cost
        if states[loc] == 1:
            print(f"Cleaned {loc}.")
            states[loc] = 0
            cost += 1

    if location == 'A':
        if states['A'] == 1:
            clean_location('A')
        else:
            print("A is clean")
        print("Moving vacuum right")
        cost += 1
        if states['B'] == 1:
            clean_location('B')
        else:
            print("B is clean")

        print("Is B clean now? (0 if clean, 1 if dirty):", states['B'])
        print("Is A dirty? (0 if clean, 1 if dirty):", states['A'])

        if states['A'] == 1:
            print("Moving vacuum left")
            cost += 1
            clean_location('A')

    elif location == 'B':
        if states['B'] == 1:
            clean_location('B')
        else:
            print("B is clean")
        print("Moving vacuum left")
        cost += 1
        if states['A'] == 1:
            clean_location('A')
        else:
            print("A is clean")

        print("Is A clean now? (0 if clean, 1 if dirty):", states['A'])
        print("Is B dirty? (0 if clean, 1 if dirty):", states['B'])

        if states['B'] == 1:
            print("Moving vacuum right")
            cost += 1
            clean_location('B')

    print(f"Cost: {cost}")
    print(states)

# Run the vacuum cleaner agent
vacuum_cleaner_agent()