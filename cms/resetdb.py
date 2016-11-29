import cms, os, sqlite3, sys
from cms import DB_FILENAME

def confirm():
	proceed_input = input("Are you sure you want to reset the database? This operation cannot be undone. (Y,n): ")
	if proceed_input == "n" or proceed_input == "N":
		sys.exit(0)
	elif proceed_input == "y" or proceed_input == "Y" or proceed_input == "":
		pass
	else:
		print("There was an error parsing your input. Use 'y', 'Y', 'n', or 'N'. Please try again.")
		confirm()

# Ask for confirmation
confirm()

# If database exists, remove it
if DB_FILENAME in os.listdir():
	os.remove(DB_FILENAME)
	print("Current database deleted.")

cms.create_db()
print("New database created.")

print("Database successfully reset.")
