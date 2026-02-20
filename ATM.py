import tkinter as tk
from tkinter import messagebox
class SimpleATM:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple ATM")
        self.root.geometry("300x300")
        self.balance = 1000
        # Create widgets
        self.welcome_label = tk.Label(root, text="Welcome to Simple ATM", font=("Arial", 14))
        self.welcome_label.pack(pady=10)
        self.check_btn = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_btn.pack(fill=tk.X, padx=50, pady=5)
        self.deposit_btn = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_btn.pack(fill=tk.X, padx=50, pady=5)
        self.withdraw_btn = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.pack(fill=tk.X, padx=50, pady=5)
        self.exit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack(fill=tk.X, padx=50, pady=5)
    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.balance:.2f}")
    def deposit(self):
        amount = self.get_amount("Deposit")
        if amount and amount > 0:
            self.balance += amount
            messagebox.showinfo("Success", f"Deposited ${amount:.2f}\nNew balance: ${self.balance:.2f}")
    def withdraw(self):
        amount = self.get_amount("Withdraw")
        if amount:
            if amount > self.balance:
                messagebox.showerror("Error", "Not enough money!")
            elif amount <= 0:
                messagebox.showerror("Error", "Must be more than $0")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"Withdrew ${amount:.2f}\nNew balance: ${self.balance:.2f}")
    def get_amount(self, action):
        popup = tk.Toplevel(self.root)
        popup.title(action)
        tk.Label(popup, text=f"Amount to {action.lower()}:").pack(pady=10)
        amount_entry = tk.Entry(popup)
        amount_entry.pack(pady=5)
        result = []
        def submit():
            try:
                amount = float(amount_entry.get())
                if amount <= 0:
                    messagebox.showerror("Error", "Must be more than $0")
                    return
                result.append(amount)
                popup.destroy()
            except:
                messagebox.showerror("Error", "Please enter a number")
        tk.Button(popup, text="Submit", command=submit).pack(pady=10)
        popup.transient(self.root)
        popup.grab_set()
        self.root.wait_window(popup)
        return result[0] if result else None
if __name__ == "__main__":
    root = tk.Tk()
    atm = SimpleATM(root)
    root.mainloop()
