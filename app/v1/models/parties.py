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

    def update_party(self,new_party,id):
        party = next(filter(lambda x: x['id'] == id, parties), None)
        party.update(new_party)
        return(party)

    def delete_party(self,party):
        parties.remove(party)



   