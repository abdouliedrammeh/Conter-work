import questionary


from db import get_db
from counter import counter
from analysis import calculate_count


def cli():
    db = get_db()
    questionary.confirm("are you ready?").ask()

    stop = False
    while not stop:
        choice = questionary.select(
            " what do you want to do",
            choices=["create","incerement","analsis","exist"]
        ).ask()

        name = questionary.text(" what's the name of your counter?").ask()
        


        if choice == "created":
            date = questionary.text(" what's the description of your counter?").ask()
            counter = counter(name, date)
            counter.store(db)
        elif choice ==  "incerement":
            counter_obj = counter(name, "no description")
            counter_obj.increment()
            counter_obj.add_event(db)

        elif choice == "analsis":
            count = calculate_count(db, name)
            print(f"{name} has been increment {count} times")
        else:
             print("bye")
        
             stop = True


if __name__ == "__main__":
    cli()



