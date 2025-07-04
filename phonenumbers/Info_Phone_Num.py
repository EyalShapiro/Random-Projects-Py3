import phonenumbers
from phonenumbers import timezone, geocoder, carrier, PhoneNumberMatcher, PhoneNumberType


def get_phone_info(number_input):
    """
    Retrieves and prints detailed timezone, location, service provider,
    and number type information for a given phone number.
    """
    try:
        # Attempt to parse the phone number.
        # It's good practice to provide a default region for numbers without a '+'
        # if you expect local numbers without country codes, but for international,
        # the '+' is crucial. We'll default to 'US' if no explicit country code.
        # However, for accuracy with global numbers, encouraging '+' is best.
        try:
            phoneNumber = phonenumbers.parse(number_input, "US")  # "US" as a default region if no country code
        except Exception:
            # If parsing with a default region fails, try without it
            phoneNumber = phonenumbers.parse(number_input)

        if not phonenumbers.is_valid_number(phoneNumber):
            print(
                f"Error: '{number_input}' is not a valid phone number. Please include the country code (e.g., +12025550123)."
            )
            return

        print(
            f"\n--- Information for {phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)} ---"
        )
        print(f"  E.164 Format: {phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"  National Format: {phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)}")
        print(f"  Country Code: +{phoneNumber.country_code}")
        print(f"  National Number: {phoneNumber.national_number}")
        print(f"  Possible Number: {phonenumbers.is_possible_number(phoneNumber)}")

        # 1. Phone Number Type
        number_type = phonenumbers.number_type(phoneNumber)
        type_description = "Unknown"
        if number_type == PhoneNumberType.FIXED_LINE:
            type_description = "Fixed Line"
        elif number_type == PhoneNumberType.MOBILE:
            type_description = "Mobile"
        elif number_type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
            type_description = "Fixed Line or Mobile"
        elif number_type == PhoneNumberType.TOLL_FREE:
            type_description = "Toll-Free"
        elif number_type == PhoneNumberType.PREMIUM_RATE:
            type_description = "Premium Rate"
        elif number_type == PhoneNumberType.SHARED_COST:
            type_description = "Shared Cost"
        elif number_type == PhoneNumberType.VOIP:
            type_description = "VoIP"
        elif number_type == PhoneNumberType.PERSONAL_NUMBER:
            type_description = "Personal Number"
        elif number_type == PhoneNumberType.PAGER:
            type_description = "Pager"
        elif number_type == PhoneNumberType.UAN:
            type_description = "Universal Access Number"
        elif number_type == PhoneNumberType.VOICEMAIL:
            type_description = "Voicemail"
        print(f"  Number Type: {type_description}")

        # 2. Timezone
        timeZone = timezone.time_zones_for_number(phoneNumber)
        if timeZone:
            print("  Timezone:", ", ".join(timeZone))
        else:
            print("  Timezone: Not found")

        # 3. Geolocation
        geolocation = geocoder.description_for_number(phoneNumber, "en")
        if geolocation:
            print("  Location:", geolocation)
        else:
            print("  Location: Not found")

        # 4. Service Provider (Carrier)
        service = carrier.name_for_number(phoneNumber, "en")
        if service:
            print("  Service Provider:", service)
        else:
            print("  Service Provider: Not found")

    except Exception as error:
        print(f"An error occurred: {error}. Please ensure the number is correctly formatted (e.g., +12025550123).")


# Corrected type hint: Use a string literal for the return type, or Union[str, None]
def choice_menu() -> str:  # Or -> Optional[str] if it could return None
    print("\n--- Phone Number Information Tool ---")
    print("1. Look up a phone number (all available info)")
    print("2. Validate if a number is possible/valid")  # New Option!
    print("3. Extract numbers from a block of text")  # New Option!
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        number = input("Enter the phone number with country code (e.g., +12025550123): ").strip()
        if not number:
            print("Phone number cannot be empty.")
            return
        get_phone_info(number)
    elif choice == "2":
        # Example for new option: Validate
        num_to_validate = input("Enter number to validate: ").strip()
        try:
            parsed_num = phonenumbers.parse(num_to_validate)
            print(f"Is possible: {phonenumbers.is_possible_number(parsed_num)}")
            print(f"Is valid: {phonenumbers.is_valid_number(parsed_num)}")
        except Exception as e:
            print(f"Could not parse: {e}")
    elif choice == "3":
        # Example for new option: Extract from text
        text_input = input("Enter text containing phone numbers: ").strip()
        # Using "US" as a default region for matching, adjust if your common region is different (e.g., "IL" for Israel)
        for match in PhoneNumberMatcher.find_numbers(text_input, "US"):
            print(
                f"Found: {match.raw_string} (Parsed: {phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)})"
            )
    elif choice == "4":
        print("Exiting script. Goodbye!")
        return True  # Return a string indicating "break"
    else:
        print("Invalid choice. Please select from the menu options.")
    return


def main_menu():
    """
    Displays a menu and handles user choices for phone number lookup.
    """
    while True:
        action = choice_menu()
        if action is True:
            break


if __name__ == "__main__":
    main_menu()
