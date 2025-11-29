import requests

class GenshinAPI:
    BASE_URL = "https://genshin.jmp.blue"

    @staticmethod
    def get_character(name: str):
        """
        Download character info from Genshin API.
        Name must be lowercase.
        """
        try:
            url = f"{GenshinAPI.BASE_URL}/characters/{name.lower()}"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print("Character not found in API.")
                return None

            data = response.json()
            return data

        except Exception as e:
            print(f"API error: {e}")
            return None

    @staticmethod
    def list_characters():
        try:
            url = f"{GenshinAPI.BASE_URL}/characters"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return []

            return response.json()

        except:
            return []
