from pydantic import BaseModel


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
    city = City.parse_raw(input_json)
    print(city)
    # print(City.name)
