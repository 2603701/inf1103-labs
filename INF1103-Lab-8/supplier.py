class Supplier:
    """Represent a supplier who provides products."""

    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        """Display supplier information."""
        print(
            f"Supplier ID: {self.__supplier_id} | "
            f"Name: {self.__name} | "
            f"Email: {self.__contact_email}"
        )