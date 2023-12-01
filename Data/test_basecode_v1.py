import unittest
def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if maximum >= users_input >= mini:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only. !")
        except ValueError:
            print("Sorry! Number only please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Sorry! Number only please")


def runners_data():
    with open("runners.txt") as input_file:
        lines = input_file.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.strip().split(",")
        runners_name.append(split_line[0])
        runner_id = split_line[1].strip()
        runners_id.append(runner_id)
    return runners_name, runners_id


def relevant_runner_info(runners_name, runners_id):
    if not runners_name or not runners_id or len(runners_name) != len(runners_id):
        print("Error: Runners data is not valid.")
        return None, None

    for i, name in enumerate(runners_name, start=1):
        print(f"{i}: {name}")

    while True:
        user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
        if 1 <= user_input <= len(runners_name):
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    runner = runners_name[user_input - 1]
    runner_id = runners_id[user_input - 1]
    return runner, runner_id


def race_results(races_location):
    for i, location in enumerate(races_location, start=1):
        print(f"{i}: {location}")

    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("races.txt") as input_file:
        lines = input_file.readlines()
    races_location = [line.strip().split(',')[0] for line in lines]
    return races_location


def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def display_races(id, time_taken, venue, fastest_runner):
    MINUTE = 60
    print(f"Results for {venue}")
    print("=" * 37)
    minutes = [t // MINUTE for t in time_taken]
    seconds = [t % MINUTE for t in time_taken]

    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break

    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []

    for runner_id in runners_id:
        time_taken_for_runner = read_integer(f"Time for {runner_id} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runner_id)
            print(f"{runner_id},{time_taken_for_runner},", file=connection)

    connection.close()


def updating_races_file(races_location):
    with open("races.txt", "w") as connection:
        for location in races_location:
            print(location, file=connection)


def competitors_by_county(name, id):
    print("Cork runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")

    print("Kerry runners")
    print("=" * 20)

    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results(location):
    try:
        with open(f"{location}.txt") as input_type:
            lines = input_type.readlines()
    except FileNotFoundError:
        print(f"Results for {location} not found.")
        return [], []

    id = []
    time_taken = []

    for line_num, line in enumerate(lines, start=1):
        split_line = line.strip().split(",")
        if len(split_line) >= 2:  # Check if the line has at least two elements
            id.append(split_line[0])
            time_str = split_line[1]
            if time_str.isdigit():
                time_taken.append(int(time_str))
            else:
                print("No available information")
        else:
            print("No available information")

    return id, time_taken




def sorting_where_runner_came_in_race(location, time):
    try:
        with open(f"{location}.txt") as input_type:
            lines = input_type.readlines()
    except FileNotFoundError:
        print(f"Results for {location} not found.")
        return None

    time_taken = []

    for line_num, line in enumerate(lines, start=1):
        split_line = line.strip().split(",")
        if len(split_line) >= 2:
            t_str = split_line[1]
            if t_str.isdigit():
                t = int(t_str)
                time_taken.append(t)
            else:
                print("No available information")
        else:
            print("No available information")

    time_taken.sort()

    try:
        position = time_taken.index(time) + 1
    except ValueError:
        print(f"Runner time {time} not found in the results for {location}.")
        return None

    return position, len(lines)



def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 60
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


def reading_race_results_of_relevant_runner(location, runner_id):
    try:
        with open(f"{location}.txt") as input_type:
            lines = input_type.readlines()
    except FileNotFoundError:
        print(f"Results for {location} not found.")
        return None

    id = []
    time_taken = []

    for line_num, line in enumerate(lines, start=1):
        split_line = line.strip().split(",")
        if len(split_line) >= 2:
            id.append(split_line[0])
            time_str = split_line[1]
            if time_str.isdigit():
                time_taken.append(int(time_str))
            else:
                print("No available information")
        else:
            print("No available information")

    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner

    print(f"Runner ID {runner_id} not found in the results for {location}.")
    return None



def displaying_winners_of_each_race(races_location):
    print("Venue             Winner")
    print("=" * 24)

    for location in races_location:
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{location:<18s}{fastest_runner}")


def display_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-" * 35)

    for location in races_location:
        time_taken = reading_race_results_of_relevant_runner(location, id)

        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(location, time_taken)
            print(f"{location} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    for i in range(len(id)):
        if fastest_runner == id[i]:
            return runners_name[i]


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print("The following runners have all won at least one race:")
    print("-" * 55)

    winners = []

    for location in races_location:
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_winner = finding_name_of_winner(fastest_runner, runners_id, runners_name)

        if fastest_runner not in winners:
            winners.append(fastest_runner)
            print(f"{name_of_winner} ({fastest_runner})")


def display_runners_without_podium(races_location, runners_name, runners_id):
    print("The following runners have not taken a podium position in any race:")
    print("-" * 65)

    for i in range(len(runners_id)):
        podium_positions = []

        for location in races_location:
            id, _ = reading_race_results(location)
            if runners_id[i] in id:
                position, _ = sorting_where_runner_came_in_race(location, reading_race_results_of_relevant_runner(location, runners_id[i]))
                podium_positions.append(position)

        if not any(position <= 3 for position in podium_positions):
            print(f"{runners_name[i]} ({runners_id[i]})")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all competitors who have not taken a podium position in any race \n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 8)

    while input_menu != 8:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            print("Show the race times for each competitor:")
            runner, id = relevant_runner_info(runners_name, runners_id)
            display_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            print("Testing")
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            print("testing 2  ")
            display_runners_without_podium(races_location, runners_name, runners_id)

        print()
        input_menu = read_integer_between_numbers(MENU, 1, 8)

    updating_races_file(races_location) 


if __name__ == "__main__":
    main()
