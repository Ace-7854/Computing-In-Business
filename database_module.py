import oracledb

class database_manager:
    def __init__(self, conn_str):
        # Establish connection once during initialization
        self.__conn = oracledb.connect(conn_str)
        print("✅ Database connection established.")

    def create_department(self): #creates department table
        query = """
CREATE TABLE Department_tbl(
    DepartmentID INTEGER,
    Department_name VARCHAR2(50),
    Department_email VARCHAR2(50),
    PRIMARY KEY(DepartmentID)
)
"""
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ Department Table has been successfully made!")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ Department Table failed: {e}")
        finally:
            cursor.close()

    def create_user(self): # User table
        query = """
CREATE TABLE User_tbl(
    UserID INTEGER,
    full_name VARCHAR2(50),
    email VARCHAR2(50),
    password VARCHAR2(50),
    DepartmentID INTEGER,
    PRIMARY KEY (UserID),
    FOREIGN KEY (DepartmentID) REFERENCES Department_tbl(DepartmentID)
)
"""
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ User Table has been successfully made!")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ User Table failed: {e}")
        finally:
            cursor.close()

    def create_referral(self): #creates a referral table
        query = """
CREATE TABLE Referral_tbl(
    ReferralID INTEGER,
    UserID INTEGER,
    DepartmentID INTEGER,
    Referral_subject VARCHAR2(100),
    User_notes VARCHAR2(50),
    hr_notes VARCHAR2(50),
    confidential INTEGER,
    expense VARCHAR2(50),
    PRIMARY KEY (ReferralID),
    FOREIGN KEY (UserID) REFERENCES User_tbl(UserID),
    FOREIGN KEY (DepartmentID) REFERENCES Department_tbl(DepartmentID)
)
"""
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ Referral Table has been successfully made!")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ Referral Table failed: {e}")
        finally:
            cursor.close()

    def get_data(self, table):
        lst_of_rec = []
        query = f"SELECT * FROM {table}"
        cursor = self.__conn.cursor()  # Keep cursor open across function calls
        try:
            cursor.execute(query)
            for rec in cursor:
                lst_of_rec.append(rec)
        except Exception as e:
            print(f"❌ Error in get_data: {e}")
        finally:
            return lst_of_rec

    def get_record(self, table, field, cond):
        query = f"SELECT * FROM {table} WHERE {field} = '{cond}'" #grabs a specific record based on a field and a criteria
        cursor = self.__conn.cursor()
        temp = ""
        try:
            cursor.execute(query)
            for rec in cursor:
                temp = rec
        except Exception as e:
            print(f"❌ Error in get_record: {e}")
        finally: 
            return temp

    def delete_record(self, table, field, cond):
        query = f"DELETE FROM {table} WHERE {field} = '{cond}'"
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()  # Committing the delete
        except Exception as e:
            print(f"❌ Error in DELETE: {e}")
            self.__conn.rollback()  # Rollback if error occurs
        finally:
            cursor.close()
    
    def empty_data(self, table):
        query = f"DELETE FROM {table}"
        cursor = self.__conn.cursor()

        try:
            cursor.execute(query)
            self.__conn.commit()
        except Exception as e:
            print(f"❌ Error in DELETE: {e}")
            self.__conn.rollback()
        finally:
            cursor.close()

    def close_connection(self):
        # Manually close the connection when done
        if self.__conn:
            self.__conn.close()
            print("❌ Database connection closed.")


    def insert_new_user(self, userid, full_name, email, password, departmentid):
        query = f""" 
        INSERT INTO user_tbl(userid, full_name, email, password, departmentid) 
        VALUES ({userid}, '{full_name}', '{email}', '{password}', {departmentid})"""
        
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ New User Made successfully")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ New user failed:\nquery: {query}\nError: {e}")
        finally:
            cursor.close()            

    def insert_new_department(self, deptid:int, dept_name:str, dept_email:str):
        query = f""" INSERT INTO department_tbl(departmentid, department_name, department_email) VALUES ({deptid}, '{dept_name}', '{dept_email}')"""

        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ New department made successfully")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ New department failed:\nquery: {query}\nError: {e}")
        finally:
            cursor.close()

    def insert_new_referral(self, referralid:int, userid:int, departmentid:int, ref_sub:str, user_notes:str, hr_notes:str, confidential:int, expense:str):
        query = f"""INSERT INTO referral_tbl(referralid, userid, departmentid, referral_subject, user_notes, hr_notes, confidential, expense) VALUES ({referralid}, {userid}, {departmentid}, '{ref_sub}', '{user_notes}', '{hr_notes}', {confidential}, '{expense}')"""

        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print("✅ New referral made successfully")
        except Exception as e:
            self.__conn.rollback()
            print(f"❌ New referral failed:\nquery: {query}\nError: {e}")
        finally:
            cursor.close()

    def get_all_tables(self):
            query = """
            SELECT table_name FROM user_tables 
            """
            #gets all tables from the oraacle database that user can access
            cursor = self.__conn.cursor()
            tables = []
            try:
                cursor.execute(query)
                tables = [row[0] for row in cursor.fetchall()]  # Get table names
            except Exception as e:
                print(f"❌ Error retrieving tables: {e}")
            finally:
                cursor.close()
            return tables
    
    def get_user_by_email(self, email):
        query = f"SELECT * FROM user_tbl WHERE email = '{email}'"

        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                userid, full_name, email, password, departmentid = row
                print(f"UserID: {userid}, DepartmentID: {departmentid}, Name: {full_name}, Email: {email}, Password: {password}")

                diction = { #a dictionary based on user data
                    'id': userid,
                    'dept_id' : departmentid,
                    'name': full_name,
                    'email': email,
                    'pass': password
                }
                return diction
            else:
                print("No user found with that email.")

        except Exception as e:
            print(f"❌No user could be retrieved: {e}")
        finally:
            cursor.close()    

    def drop_tbl(self, table_name):
        query = f"DROP TABLE {table_name}" #Drops a table, done for testing and errors in tables during trial phases
        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            self.__conn.commit()
            print(f"✅ Successfully dropped {table_name}")
        except Exception as e:
            print(f"❌ Error dropping table {table_name}: {e}")
        finally:
            cursor.close()

    def get_referral_by_user(self, userid):
        query = f"SELECT * FROM referral_tbl WHERE userid = {userid}" #gets the referral details via the userid 

        cursor = self.__conn.cursor()
        try:
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                referralid, user_id, departmentid, ref_subject, usr_notes, hr_notes, confidential, expense = row

                diction = {
                    'ref':referralid,
                    'userid' : user_id,
                    'departmentid' : departmentid,
                    'ref_sub' : ref_subject,
                    'user_notes' : usr_notes, 
                    'hr_notes' : hr_notes,
                    'confidential' : confidential,
                    'expense' : expense
                }

                return diction
        except Exception as e:
            print(f"Could not get record, or no records found: {e}")
        finally: 
            cursor.close()