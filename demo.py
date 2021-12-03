# name = input("What's your name: ")
# print("Hello", name, "how are you?")
# if you have to ask someone for his age what data-type do you think that should be? 



print("Hello Welcome to Nimi's Online Store.")
print("Please select any of the items available using the numbers.")
print("1.Doll 2.HeadPhones 3.Biology TextBook 4.Diary of a wimp kid book, 5.Cameras ")

users_choice = int(input("type here> "))

if users_choice == 1: # the double == is used to compare values
	print("Hi, a doll cost 1000 NGN")
	print("How many would you like to buy?")
	qty = int(input("type here> "))
	total_cost = qty * 1_000
	print("That would cost", total_cost, "NGN")

elif users_choice == 2: # the double == is used to compare values
	print("Hi, a headphone cost 5000 NGN")
	print("How many would you like to buy?")
	qty = int(input("type here> "))
	total_cost = qty * 5_000
	print("That would cost", total_cost, "NGN")

elif users_choice == 3: # the double == is used to compare values
	print("Hi, a  Biology TextBook cost 2500 NGN")
	print("How many would you like to buy?")
	qty = int(input("type here> "))
	total_cost = qty * 2_500
	print("That would cost", total_cost, "NGN")

elif users_choice == 4: # the double == is used to compare values
	print("Hi, the diary of a wimp kid book cost 3000 NGN")
	print("How many would you like to buy?")
	qty = int(input("type here> "))
	total_cost = qty * 3_000
	print("That would cost", total_cost, "NGN")

elif users_choice == 5: # the double == is used to compare values
	print("Hi, the Cameras 5000 NGN")
	print("How many would you like to buy?")
	qty = int(input("type here> "))
	total_cost = qty * 50_000
	print("That would cost", total_cost, "NGN")
else:
	print("Invalid input")