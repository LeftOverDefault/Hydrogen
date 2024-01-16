class Human {
    def __initiate__(self, first_name, last_name, year_born) {
        self.first_name = first_name;
        self.last_name = last_name;
        self.year_born = year_born;
    }

    def getFullName(self) {
        return self.first_name + " " + self.last_name;
    }
}

class Man(Human) {
    def __initiate__(self, first_name, last_name, year_born) {
        super.__initiate__(first_name, last_name, year_born);
        self.gender = "male";
    }
}

const doug = Man("Douglas", "Adams", 1951);
doug.first_name = "Doug";

let full_name = doug.getFullName();
print(full_name);
print("Gender:", doug.gender);