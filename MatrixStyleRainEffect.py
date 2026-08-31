import random
import time
CHARACTERS = "ｦｱｳｴｵｶｷｹｺｻｼｽｾｿﾀﾂﾃﾅﾆﾇﾈﾊﾋﾎﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ1234567890"
while True:
    row = "".join(random.choice(CHARACTERS) if random.random() < 0.2 else " " for _ in range(50))
    # Generate a row of 40 random characters or empty spaces
    print(f"\033[32m{row}\033[0m")

    time.sleep(0.4)

