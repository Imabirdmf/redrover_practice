from dataclasses import dataclass

@dataclass
class RegistrationData:
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None
    repeated_password: str = None
