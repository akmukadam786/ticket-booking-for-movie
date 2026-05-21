
# ============================================
#        MOVIE TICKET BOOKING SYSTEM
# ============================================

print("=" * 45)
print("     WELCOME TO MOVIEMAX BOOKING SYSTEM")
print("=" * 45)

# ── Gather user input ──────────────────────
name      = input("\nEnter your name: ")
age       = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"

print("\n── Select Seat Type ──")
print("  1. Premium")
print("  2. Gold")
print("  3. Standard")
seat_choice = input("Enter choice (1/2/3): ").strip()

if seat_choice == "1":
    seat_type = "Premium"
elif seat_choice == "2":
    seat_type = "Gold"
else:
    seat_type = "Standard"

print("\n── Select Show Time ──")
print("  1. Morning")
print("  2. Afternoon")
print("  3. Evening")
show_choice = input("Enter choice (1/2/3): ").strip()

if show_choice == "1":
    show_time = "Morning"
elif show_choice == "2":
    show_time = "Afternoon"
else:
    show_time = "Evening"

is_weekend = input("\nIs it a weekend? (yes/no): ").strip().lower() == "yes"

# ── Base price ─────────────────────────────
base_price = 15

# ── Eligibility check ──────────────────────
print("\n" + "=" * 45)
print("           BOOKING SUMMARY")
print("=" * 45)

if age >= 21 or (age >= 18 and (show_time != "Evening" or is_member)):
    print(f"\nHi {name}! Ticket booking condition satisfied.")

    # ── Discount ───────────────────────────
    discount = 0
    if is_member and age >= 21:
        discount = 3
        print("✓ Membership discount applied.")
    else:
        print("✗ No membership discount.")

    # ── Extra charges ──────────────────────
    extra_charges = 0
    if is_weekend or show_time == "Evening":
        extra_charges = 2
        print("✓ Extra charges applied (weekend/evening).")
    else:
        print("✗ No extra charges.")

    # ── Service charges ────────────────────
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1

    # ── Final price ────────────────────────
    final_price = base_price + extra_charges + service_charges - discount

    print("\n── Price Breakdown ───────────────────")
    print(f"  Base price      : R{base_price}")
    print(f"  Seat ({seat_type:<9}): R{service_charges}")
    print(f"  Show ({show_time:<9}): R{extra_charges}")
    print(f"  Discount        : -R{discount}")
    print("  " + "-" * 30)
    print(f"  TOTAL           : R{final_price}")
    print("=" * 45)
    print("\nEnjoy your movie! 🎬")

else:
    print(f"\nSorry {name}, ticket booking failed due to age restrictions.")
    print("Users under 18 cannot book tickets.")
    print("Users 18-20 can only book non-evening shows (or with membership).")
    print("=" * 45)
