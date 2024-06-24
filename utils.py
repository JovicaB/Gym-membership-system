
class DayReset:
    def __init__(self) -> None:
        pass

    def reset_gzym_menagement_system(self):
        pass

    def reset_lockers(self):
        pass

    def start_process(self):
        pass


# class GetMembershipServiceDetails:

#     def __init__(self, ticket_type: str):
#         self.ticket_type = ticket_type
#         self.json_filename = MEMBERSHIP_DATA
        
#     def get_membership_price(self):
#         """
#         Gets membership price for the choosen period

#         Returns: 
#         float: membership price for the choosen membership period

#         Usage:
#         ```
#         membership_price = GymMembershipData().get_membership_price('3_months'))
#         print(membership_price)
#         ```

#         """
#         json_data = JSONData(self.json_filename).read_json(self.ticket_type)
#         return json_data['price']
    
#     def get_membership_duration(self):
#         """
#         gets membership duration from choosen membership type

#         Returns: 
#         int: duration of membership type in days

#         Usage:
#         ```
#         membership_duration = GymMembershipData().get_membership_duration('3_months'))
#         print(membership_duration)
#         ```

#         """
#         json_data = JSONData(self.json_filename).read_json(self.ticket_type)
#         return json_data['duration']