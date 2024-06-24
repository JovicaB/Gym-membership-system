from dataclasses import dataclass, field
from typing import Literal

import pandas as pd


@dataclass
class GymRegistration:
    members_registration_data: pd.DataFrame
    name: str
    surname: str
    gender: str
    birth_date: str
    address: str
    city: str
    document_id: str
    jmbg: str
    note: str

    def is_member_registered(self) -> bool:
        return not self.members_registration_data[self.members_registration_data['jmbg'] == self.jmbg].empty

    def generate_unique_memberid(self) -> str:
        if self.members_registration_data.empty:
            return "0001"
        else:
            max_id = max(self.members_registration_data['id'].astype(int).tolist())
            new_id = f"{max_id + 1:04d}"
            return new_id

    def validate_document_id(self) -> bool:
        return self.document_id.isalnum() and len(self.document_id) == 9

    def validate_jmbg(self) -> bool:
        return self.jmbg.isdigit() and len(self.jmbg) == 13

    def register_member(self) -> Literal["User registered successfully", "User already registered", "Invalid document ID", "Invalid JMBG"]:
        if self.is_member_registered():
            return "User already registered"

        if not self.validate_document_id():
            return "Invalid document ID"

        if not self.validate_jmbg():
            return "Invalid JMBG"

        new_id = self.generate_unique_memberid()

        new_member = {
            'id': new_id,
            'name': self.name,
            'surname': self.surname,
            'gender': self.gender,
            "birth_date": self.birth_date,
            'address': self.address,
            'city': self.city,
            'document_id': self.document_id,
            'jmbg': self.jmbg,
            'note': self.note
        }

        new_member_df = pd.DataFrame([new_member])
        self.members_registration_data = pd.concat([self.members_registration_data, new_member_df], ignore_index=True)
        return "User registered successfully"




# ## USAGE ##
# members_data = [
#     {
#         'id': '0001',
#         'name': 'Jovica',
#         'surname': 'Božić',
#         'gender': 'M',
#         'birth_date': '7/31/1974',
#         'address': 'Almaška 1',
#         'city': 'Novi Sad',
#         'document_id': '00111111',
#         'jmbg': '3107974800144',
#         'phone_num': '+38162111111',
#         'e-mail': 'jovicab@gmail.com',
#         'note': 'test note'
#     }
# ]
# df = pd.DataFrame(members_data)


# registration = GymRegistration(
#     df,
#     name="John",
#     surname="Doe",
#     gender="M",
#     address="123 Street",
#     city="City",
#     document_id="123456789",
#     jmbg="3107974800145",
#     note="No notes"
# )

# result = registration.register_member()
# print(result)
# print(registration.members_registration_data)

