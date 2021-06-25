from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: str
    dep: str
    email_id: str
    mobile_number: str

    def __str__(self) :
        return f"name {self.name}, id {self.id}, dept {self.dep}, email {self.email_id}"


@dataclass
class Company:
    name: str
    website: str
    contact_nos: list



