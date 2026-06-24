from datetime import datetime

day = datetime.now().weekday()

if day >= 5:
    print("Weekend")
else:
    print("Working Day")