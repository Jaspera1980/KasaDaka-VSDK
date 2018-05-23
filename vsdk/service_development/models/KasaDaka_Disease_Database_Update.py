import sqlalchemy
from collections import Counter


class update_datebase():
    """Update disease diagnosis in database"""
    con = sqlalchemy.create_engine('postgresql://postgres:123@abc@127.0.0.1:5432/KasaDaka')
    # Select items from service_development_callsessionstep
    q0 = con.execute("SELECT _visited_element_id, session_id FROM service_development_callsessionstep")
    q1 = q0.fetchall()

    # Counter of unique id's
    count_list = []
    for item in q1:
        count_list.append(item[1])

    def update_disease(self):
        # Update for loop
        count = 0
        for item in self.q1:
            # Count number of same id's
            no_of_ids = self.count_list.count(item[1])
            # Match on session_id
            matching_id = str(item[1])
            # PK number with matching diagnosis
            disease_dict = {16: "Bursal Disease", 17: "Fowl Pox", 18: "Mareks Disease", 19: "Newcastle Disease"}
        # If pk=x then state the diagnosis
        if item[0] in disease_dict.keys():
            disease = str("'" + disease_dict[item[0]] + "'" + " ")
        # If no diagnosis is found return 'No diagnosis'
        else:
            count += 1
            if count == no_of_ids:
                count = 0
                disease = "'No diagnosis' "
        query_stmt_1 = "UPDATE service_development_callsession SET disease = " + disease + "WHERE id = " + matching_id
        self.con.execute(query_stmt_1)
        return

    def update_vet(self):
        count = 0
        for item in self.q1:
            # Count number of same id's
            no_of_ids = self.count_list.count(item[1])
            # Match on session_id
            matching_id = str(item[1])
            # PK number with matching diagnosis
            vet_dict = {25: "Veterinarian 1", 26: "Veterinarian 2", 27: "Veterinarian 3"}
        # If pk=x then state the diagnosis
        if item[0] in vet_dict.keys():
            vet = str("'" + vet_dict[item[0]] + "'" + " ")
        # If no diagnosis is found return 'No diagnosis'
        else:
            count += 1
            if count == no_of_ids:
                count = 0
                vet = "'No choice' "
        query_stmt_2 = "UPDATE service_development_callsession SET veterinarian = " + vet + "WHERE id = " + matching_id
        self.con.execute(query_stmt_2)
        return

    def update_medicine(self):
        count = 0
        for item in self.q1:
            # Count number of same id's
            no_of_ids = self.count_list.count(item[1])
            # Match on session_id
            matching_id = str(item[1])
            # PK number with matching diagnosis
            vet_dict = {16: "Methionine", 17: "Avatec", 18: "Neotetravit", 19: "Anticoc Super"}
        # If pk=x then state the diagnosis
        if item[0] in vet_dict.keys():
            vet = str("'" + vet_dict[item[0]] + "'" + " ")
        # If no diagnosis is found return 'No diagnosis'
        else:
            count += 1
            if count == no_of_ids:
                count = 0
                vet = "'Not available' "
        query_stmt_3 = "UPDATE service_development_callsession SET medicines = " + vet + "WHERE id = " + matching_id
        self.con.execute(query_stmt_3)
        return

    def update_vaccine(self):
        count = 0
        for item in self.q1:
            # Count number of same id's
            no_of_ids = self.count_list.count(item[1])
            # Match on session_id
            matching_id = str(item[1])
            # PK number with matching diagnosis
            vet_dict = {16: "Gumboro Vaccination", 17: "Fowl Pox Vaccination", 18: "No vaccine available",
                        19: "Newcastle Vaccination"}
        # If pk=x then state the diagnosis
        if item[0] in vet_dict.keys():
            vet = str("'" + vet_dict[item[0]] + "'" + " ")
        # If no diagnosis is found return 'No diagnosis'
        else:
            count += 1
            if count == no_of_ids:
                count = 0
                vet = "'Not available' "
        query_stmt_4 = "UPDATE service_development_callsession SET vaccines = " + vet + "WHERE id = " + matching_id
        self.con.execute(query_stmt_4)
        return
    print("database updated")