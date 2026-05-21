# 🎬 Movie Ticket Booking System

A command-line Python app that calculates the final price of a movie ticket based on the user's age, membership status, seat type, and show time.

---

## 💡 Features

- Age-based eligibility checks
- Membership discount applied automatically
- Extra charges for evening shows and weekends
- Service charges based on seat type (Premium, Gold, Standard)
- Clean price breakdown summary

---

## 🚀 How to Run

Make sure you have Python 3 installed. Then in your terminal:

```bash
python movie_ticket_booking.py
```

Follow the prompts and the app will calculate your ticket price.

---

## 📋 Pricing Structure

| Item | Cost |
|---|---|
| Base Price | R15 |
| Premium Seat | +R5 |
| Gold Seat | +R3 |
| Standard Seat | +R1 |
| Evening / Weekend | +R2 |
| Membership Discount (21+) | -R3 |

---

## 🔒 Booking Rules

- Users **21 and above** can book any show
- Users **18 to 20** can only book non-evening shows
- Users **18 to 20** with a membership can book evening shows
- Users **under 18** cannot book tickets

---

## 🛠 Built With

- Python 3
- Core concepts: variables, booleans, if/elif/else statements, user input

---

## 👤 Author

**Abdul Kadir Mukadam**  
Freelance Developer · [GitHub](https://github.com/)
