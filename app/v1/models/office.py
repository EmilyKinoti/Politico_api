office= []

class Political_Office:
    def save_office(self, office):
        office.append(office)
        return ({
            "id":office['id'],
            "name":office['name']
        })