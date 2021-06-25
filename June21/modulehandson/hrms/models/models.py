from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: str
    dep: str
    email_id: str
    mobile_number: str


@dataclass
class Company:
    name: str
    website: str
    contact_nos: list
    


