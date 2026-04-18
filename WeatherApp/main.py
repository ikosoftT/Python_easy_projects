import requests
from pydantic import BaseModel, Field, model_validator



KEY = "23155ec384e6e65e3bd7d9e2d1ebff43"


class UserData(BaseModel):
    city_name: str = Field(..., min_length=5, max_length=30)

    @model_validator(mode='after')
    def check_city(self):
        if not self.city_name:
            raise ValueError("Please Provide Valid name!")
        try:
            URL = f"https://api.weatherstack.com/current?access_key={KEY}&query={self.city_name}"
            res = requests.get(URL)

            # Check Req Status
            if res.status_code == 200:
                data = res.json()
                print(
                    f"temperature: {data['current']['temperature']}C\nLocation: {data['location']['country']}")
                currentTime = data['location']['localtime']
                exactTime = currentTime.split(" ")[1]
                if ":" in exactTime:
                    fdig = int(exactTime.split(":")[0])
                    if fdig <= 12:
                        print(f"Current time: {exactTime} AM")
                    else:
                        print(f"Current time: {exactTime} PM")
                else:
                    print("Current time: kayn chi err")
                print(f"Local Time: {data['location']['localtime']}")
                print("Weather Details:")
                for k, v in data['current']['astro'].items():
                    if ":" in str(v):
                        print(f"- {k}: {v}")
            else:
                raise ValueError("Error 404!")

        except Exception as e:
            print(f"Unknown City: {e}")
        return self


def main():
    print("\nWelcome to Weather app\n")
    user_city = input("Enter Your City name:")
    try:
        UserData(city_name=user_city)
    except Exception as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
        main()
