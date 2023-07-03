import csv
from tabulate import tabulate
import pyttsx3
import inflect


def main():
    country = choose_country()
    tickets_price = choose_tickets(country)
    accommodation_price = choose_accommodation(country)
    attractions_price = choose_attractions(country)
    p = inflect.engine()
    text = f"A vacation to {country.capitalize()} for one week and for one person will cost around " \
           f"{(tickets_price + accommodation_price + attractions_price):,.2f} dollars. " \
           f"Enjoy your summer vacation!!!"
    print(text)
    p.number_to_words(tickets_price + accommodation_price + attractions_price)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[17].id)
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()


def choose_country():
    countries = {'1': 'italy', '2': 'turkey', '3': 'thailand'}
    while True:
        try:
            country = input("Which country would you like to visit? Type '1' for Italy, '2' for Turkey, "
                            "'3' for Thailand: ").rstrip()
            return countries[country]
        except KeyError as err:
            print(f"Key {err} does not exist. Try again")


def get_table(csv_for_table):
    with open(csv_for_table) as file:
        reader = csv.reader(file)
        my_list = [row for row in reader]
        print(tabulate(my_list[1:], my_list[0], tablefmt="double_grid"))


def choose_tickets(chosen_country):
    while True:
        csv_name = f"{chosen_country}_tickets.csv"
        get_table(csv_name)
        flight = input("You can choose a flight (enter '1', '2' or '3'): ")
        if flight in ['1', '2', '3']:
            return tickets_csv(csv_name, flight)
        else:
            print("You pressed an invalid key. Please try again")


def tickets_csv(new_file, flight_key):
    with open(new_file) as t_file:
        ticket_reader = csv.DictReader(t_file)
        for row in ticket_reader:
            if row['key'] == flight_key:
                print(f"Your airline is {row['airline']}.\nThe price is {int(row['price']):,}$.\nThe outbound flight "
                      f"takes {row['outbound time']}.\nThe inbound flight takes {row['return time']}.\n")
                return int(row['price'])


def choose_accommodation(country_you_chose):
    while True:
        csv_file = f"{country_you_chose}_accommodation.csv"
        get_table(csv_file)
        choose_lodging = input("Now please choose an accommodation (enter '1', '2' or '3'): ").rstrip()
        if choose_lodging in ['1', '2', '3']:
            return accommodation_csv(csv_file, choose_lodging)
        else:
            print("You pressed an invalid key. Please try again")


def accommodation_csv(lodging_file, lodging_choice):
    with open(lodging_file) as a_file:
        accommodation_reader = csv.reader(a_file)
        for row in accommodation_reader:
            if row[2] == lodging_choice:
                print(f"One week in {row[0]} costs {row[1]}$\n")
                return int(row[1])


def choose_attractions(location):
    print(f"Final step! Choose places to visit in {location.capitalize()}.")
    attractions_sum = 0
    while True:
        try:
            free_or_paid = input("If you prefer to visit places for free, type 'Free', otherwise, "
                                 "type 'Paid': ").rstrip().lower()
            csv_making_up = location + '_' + free_or_paid + ".csv"
            get_table(csv_making_up)
            while True:
                try:
                    place = input("Choose a tourist attraction, press a number key(from 1 through 10): ")
                    if 1 <= int(place) <= 10:
                        my_sum = attractions_csv(csv_making_up, place)
                        attractions_sum += my_sum
                        question = input("Total cost for attractions is {:.2f}$.\nWould you like to continue (enter 'C') "
                                         "or to return to the previous options (enter 'R') or to quit (enter 'Q'): "
                                         .format(attractions_sum)).lower()
                        if question == 'c':
                            continue
                        elif question == 'r':
                            break
                        elif question == 'q':
                            return attractions_sum
                except ValueError as ex:
                    print(f"{ex} is a wrong input. Try again")
        except FileNotFoundError as exc:
            print(f"{exc}. Please try again.")


def attractions_csv(c_name, place_to_visit):
    with open(c_name) as new_file:
        new_reader = csv.reader(new_file)
        for row in new_reader:
            if row[2] == place_to_visit:
                return float(row[1])


if __name__ == "__main__":
    main()
