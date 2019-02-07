class Expense():

    def __init__(self, date, amount, perGallon, location, details):
        self.date = date
        self.amount = amount
        self.perGallon = perGallon
        self.location = location
        self.details = details

    #----------EDIT EXPENSE----------#
    def edit_expense(self, date, amount, perGallon, location, details):
        self.date = date
        self.amount = amount
        self.perGallon = perGallon
        self.location = location
        self.details = details

    def edit_date(self, date):
        self.date = date

    def edit_amount(self, amount):
        self.amount = amount
    
    def edit_perGallon(self, perGallon):
        self.perGallon = perGallon

    def edit_location(self, location):
        self.location = location

    def edit_details(self, details):
        self.details = details

    #----------GET EXPENSE----------#
    def get_expense(self):
        return self

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount
    
    def get_perGallon(self):
        return self.perGallon

    def get_location(self):
        return self.location

    def get_details(self):
        return self.details