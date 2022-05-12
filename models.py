import psycopg2


class Database:
    def __init__(self):

        self.conn = psycopg2.connect(
            "host=127.0.0.1 dbname=covid_data user=abdurrafay password=test123"
        )
        # print("connecting to the database...")

    def get_data_by_id(self, id):
        query = f"""
        SELECT * 
        FROM owid_covid_data 
        where id={id};
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            row = cur.fetchone()
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
        return row
    
    def insert_data(self, data):
        count = 0
        query = f"INSERT INTO public.owid_covid_data VALUES ("
        # 'AFG', 'ASIA', 999999);
        for i in data:
            if isinstance(i, str):
                if count == len(data)-1:
                    query += f"'{i}'"
                else:
                    query += f"'{i}'" + ","
            else:
                if count == len(data)-1:
                    query += str(i)
                else:
                    query += str(i) + ","
            count += 1
        query += ");"
        # print(query)
        # execute query
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def delete_data_by_id(self, id):
        query = f"""
        DELETE
        FROM owid_covid_data 
        where id={id};
        """
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def update_data_by_id(self, id, data):
        
        query = """
        UPDATE owid_covid_data
        SET"""
        last_value = list(data.values())[-1]
        for i in data:
            if data[i] == last_value:
                query += f" {i} = '{data[i]}' "
                break
            query += f" {i} = '{data[i]}', "
        
        query += f"""WHERE id = {id};"""
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

if __name__ == "__main__":
    obj = Database()
    # print(obj.get_data_by_id(5))
    # data = ['TESTASIA', 'TESTAFRICA', 8267372]
    # obj.insert_data(data)
    # obj.delete_data_by_id(185211)
    # update
    data = {'iso_code':'BBB',
                'continent': 'ZZZZ',
                'location': 'PAK',
                }
    obj.update_data_by_id(100, data)