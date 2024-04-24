def membandingkan_file(fileM, fileN):
    with open(fileM, 'r') as fM, open(fileN, 'r') as fN:
        while True:
            line1 = fM.readline()
            line2 = fN.readline()
            if not line1 and not line2:
                break
            if line1!= line2:
                print(f"Difference at line {fM.tell()}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")

membandingkan_file('pM.txt', 'pN.txt')