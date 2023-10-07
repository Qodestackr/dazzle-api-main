class UserCompliance:

    @staticmethod
    def subject_is_adult(user, country_code):
        """
        Check if the user is of legal adult age in their country.

        Args:
        - user: The user for whom you want to check compliance.
        - country_code: The user's country code (e.g., 'FR' for France).

        Returns:
        - True if the user is an adult, False otherwise.
        """
        # Implement age-based compliance checks specific to the user's country
        # Example: Check the legal age for adulthood in the user's country
        legal_adult_age = UserCompliance.get_legal_adult_age(country_code)
        user_age = user.get_age()  # Replace with your actual logic to get the user's age
        return user_age >= legal_adult_age

    @staticmethod
    def subject_is_not_adult(user, country_code):
        """
        Check if the user is not of legal adult age in their country.

        Args:
        - user: The user for whom you want to check compliance.
        - country_code: The user's country code (e.g., 'FR' for France).

        Returns:
        - True if the user is not an adult, False otherwise.
        """
        return not UserCompliance.subject_is_adult(user, country_code)

    @staticmethod
    def get_legal_adult_age(country_code):
        """
        Get the legal age for adulthood in a specific country.

        Args:
        - country_code: The country code for which you want to retrieve the legal adult age.

        Returns:
        - The legal age for adulthood in the specified country.
        """
        # Implement logic to fetch the legal adult age for the specified country
        # Example: Use a dictionary of legal adult ages by country code
        legal_adult_age_by_country = {
            'FR': 18,  # Legal adult age in France
            # Add more countries and legal adult ages as needed
        }
        # Default to 18 if not found
        return legal_adult_age_by_country.get(country_code, 18)

    # Additional compliance checks and methods specific to EU regulations
