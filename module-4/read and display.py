try:
    file = open("log.txt", "r")
    lines = 0
    words = 0
    characters = 0
    warnings = 0
    errors = 0
    print("Log File Contents:\n")
    for line in file:
        print(line, end="")
        lines += 1
        words += len(line.split())
        characters += len(line.strip("\n"))
        if "WARNING" in line.upper() or "WARN" in line.upper():
            warnings += 1
        if "ERROR" in line.upper() or "CRITICAL" in line.upper():
            errors += 1
    file.close()
    print("\n\nLog Summary:")
    print("Total Lines:", lines)
    print("Total Words:", words)
    print("Total Characters:", characters)
    print("Total Warnings:", warnings)
    print("Total Errors:", errors)
except FileNotFoundError:
    print("Error: log.txt file does not exist.")
