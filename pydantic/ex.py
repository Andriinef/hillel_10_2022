from pydantic import BaseModel, ValidationError


class City(BaseModel):
    city_id: int
    name: str
    population: int


input_json = """
{
    "city_id": 123,
    "name": "Kiev",
    "population": 1000000
}
"""


if __name__ == "__main__":
    try:
        city = City.parse_raw(input_json)
        print(city)
    except ValidationError as e:
        print(e.json())
    # print(city)
    # print(City.name)
