# Feature: Lists.
# 27/10/2026

boodschap_lijst = ["Brood", "Eiren", "Melk", "Fruit", "Sap"]

boodschap_lijst.append("Snoep")
boodschap_lijst.remove("Sap")
boodschap_lijst_count = len(boodschap_lijst)

print(f"Boodschap lijst: {", ".join(boodschap_lijst)}")
print(f"Ik heb {boodschap_lijst_count} itens in mijn lijst.")

