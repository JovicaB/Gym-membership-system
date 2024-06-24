from data_access.sqlite_handler import SQLiteHandler
from gym_access import GymRegistration

def main():
    database_path = "data/gym_data.sqlite"
    
    load_data = SQLiteHandler(database_path).load_data("SELECT * FROM members_data")

    print(GymRegistration(load_data).generate_unique_memberid())

class MemberRegistration:
    def __init__(self) -> None:
        pass