from data_access.sqlite_handler import SQLiteHandler
from gym_access import GymRegistration

def main():

    # Step 2. load data
    database_path = "data/gym_data.sqlite"
    table_name = "members_data"
    load_data_query = f"SELECT * FROM {table_name}"
    
    db_handler = SQLiteHandler(database_path)
    members_data = db_handler.load_data(load_data_query)


    new_member_data = GymRegistration(
            members_registration_data=members_data,
            name="John",
            surname="Doe",
            gender="M",
            birth_date = "05/05/1995",
            address="123 Street",
            city="City",
            document_id="123456789",
            jmbg="3107974800145",
            note="No notes"
        )

    result = new_member_data.register_member()
    
    db_handler.save_data(new_member_data.members_registration_data, table_name)

    # print(load_data)

if __name__ == "__main__":
    main()