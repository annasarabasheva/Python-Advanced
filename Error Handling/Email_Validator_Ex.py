class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAt(Exception):
    pass
#TODO: Blalalala

while True:
    email = input()
    if email == "End":
        break
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if email.count("@") > 1:
        raise MustContainOnlyOneAt("Email cant contain more than one @!")
    if "@" in email:
        main_name = []
        for el in email:
            if el == "@":
                break
            main_name.append(el)

        idx_at = email.index("@")
        domain_name = email[idx_at + 1:]
        if len(main_name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if not email.endswith(".com") and not email.endswith(".bg") and not email.endswith(".net") and not email.endswith(".org"):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

