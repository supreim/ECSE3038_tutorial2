from fastapi import FastAPI

app = FastAPI()

data = [
      {
          "name": "John Doe",
              "occupation": "Software Engineer",
                  "address": "123 Main St"
                    },
                      {
                          "name": "Jane Smith",
                              "occupation": "Data Scientist",
                                  "address": "456 Elm St"
                                    },
                                      {
                                          "name": "Michael Johnson",
                                              "occupation": "Web Developer",
                                                  "address": "789 Oak St"
                                                    },
                                                      {
                                                            "name": "Emily Brown",
                                                                "occupation": "UX Designer",
                                                                    "address": "101 Maple Ave"
                                                                      },
                                                                        {
                                                                            "name": "David Lee",
                                                                                "occupation": "Product Manager",
                                                                                    "address": "202 Pine St"
                                                                                      },
                                                                                        {
                                                                                            "name": "Sarah Taylor",
                                                                                                "occupation": "Marketing Specialist",
                                                                                                    "address": "303 Cedar St"
                                                                                                      },
                                                                                                        {
                                                                                                            "name": "Chris Evans",
                                                                                                                "occupation": "Graphic Designer",
                                                                                                                    "address": "404 Walnut St"
                                                                                                                      },
                                                                                                                        {
                                                                                                                            "name": "Jessica White",
                                                                                                                                "occupation": "Financial Analyst",
                                                                                                                                    "address": "505 Birch St"
                                                                                                                                      },
                                                                                                                                        {
                                                                                                                                            "name": "Matthew Miller",
                                                                                                                                                "occupation": "Systems Administrator",
                                                                                                                                                    "address": "606 Spruce St"
                                                                                                                                                      },
                                                                                                                                                        {
                                                                                                                                                            "name": "Amanda Martinez",
                                                                                                                                                                "occupation": "HR Coordinator",
                                                                                                                                                                    "address": "707 Chestnut St"
                                                                                                                                                                      }
                                                      
]

names = []
occupations = []
addresses = []
for person in data:
    names.append(person["name"])
    occupations.append(person["occupation"])
    addresses.append(person["address"])

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/name")
async def name():
    return {"names": names}

@app.get("/address")
async def address():
    return {"message": addresses}

@app.get("/occupation")
async def occupation():
    return {"message": occupations}