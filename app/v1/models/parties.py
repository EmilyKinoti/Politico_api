parties = []

class Political_Party:

    def save_party(self, party):
        parties.append(party)
        return ({
            "id":party['id'],
            "name":party['name']
        })

    def get_all_parties(self):
        return(parties)
    
    def get_by_id(self, id):
        party = next(filter(lambda x: x['id'] == id, parties), None)
        return party