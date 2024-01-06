import mysql.connector
import email_validator

class Allievo():
    def __init__(self,conn):
        self.conn=conn
        self.cursor=conn.cursor()

    def visualizza_allievi(self):
        query="SELECT * FROM allievi"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        for rows in result:
            print(rows) 

    def validazione_email(self, email):
        try:
            email_validator.validate_email(email)
            return True
        except email_validator.EmailNotValidError as e:
            print(f'Formato email non valido: {e}')
            return False        

    def aggiungi_allievo(self):
        nome_allievo=input("Inserisci nome allievo: ")
        cognome_allievo=input("Inserisci cognome allievo: ")
        indirizzo_allievo=input("Inserisci indirizzo allievo: ")
        telefono_allievo=input("Inserisci telefono allievo: ")
        while True:
            try:
                email_allievo=input("Inserisci email allievo: ")
                if self.validazione_email(email_allievo):
                    print("Formato email valido")
                    break
                else:
                    print("Formato email non valido, riprova e controlla")
            except email_validator.EmailSyntaxError as e:
                print(f'Formato email non valido: {e}')
        
        corso_allievo=input("Inserisci corso allievo: ")
        data_iscrizione = input("Inserisci data iscrizione: ")
        try:
            query="INSERT INTO allievi(nome, cognome, indirizzo, telefono, email, corso, dataIscrizione) VALUES(%s,%s,%s,%s,%s,%s,%s)"  
            values=(nome_allievo, cognome_allievo, indirizzo_allievo, telefono_allievo, email_allievo, corso_allievo, data_iscrizione) 
            self.cursor.execute(query,values)
            self.conn.commit()
            print("Record inserito correttamente")
        except mysql.connector.Error as e:
            print(f'Errore nello stabilire una connessione al database: {e}')
    
    def aggiorna_allievo(self):
        id_allievo=int(input("Inserisci id allievo da modificare: "))
        nome_allievo=input("Inserisci nome allievo: ")
        cognome_allievo=input("Inserisci cognome allievo: ")
        indirizzo_allievo=input("Inserisci indirizzo allievo: ")
        telefono_allievo=input("Inserisci telefono allievo: ")
        while True:
            try:
                email_allievo=input("Inserisci email allievo: ")
                if self.validazione_email(email_allievo):
                    print("Formato email valido")
                    break
                else:
                    print("Formato email non valido, riprova e controlla")
            except email_validator.EmailSyntaxError as e:
                print(f'Formato email non valido: {e}')
        corso_allievo=input("Inserisci corso allievo: ")
        data_iscrizione = input("Inserisci data iscrizione: ")      
        try:
            query="UPDATE allievi SET nome=%s, cognome=%s, indirizzo=%s, telefono=%s, email=%s, corso=%s, dataIscrizione=%s WHERE id=%s"
            values=(nome_allievo, cognome_allievo, indirizzo_allievo, telefono_allievo, email_allievo, corso_allievo, data_iscrizione, id_allievo)
            self.cursor.execute(query,values)
            self.conn.commit()
            print("Record aggiornato correttamente")
        except mysql.connector.Error as e:
            print(f'Errore nello stabilire una connessione al database: {e}')   


    def elimina_allievo(self):
        allievo_id=int(input("Inserisci id allievo da eliminare: "))
        try:
            query="DELETE FROM allievi WHERE id=%s"
            values=(allievo_id, )
            self.cursor.execute(query,values)
            self.conn.commit()
            print("Record eliminato correttamente")
        except mysql.connector.Error as e:
             print(f'Errore nello stabilire una connessione al database: {e}')  

    def menu(self):
        while True:
            print("**MENU**")
            print("1. Visualizza allievi")
            print("2. Aggiungi allievo")
            print('3. Aggiorna Allievo')
            print('4. Elimina allievo')
            print('5. Esci')

            scelta=input('Scegli opzione: ')
            if scelta=="1":
                self.visualizza_allievi()
            elif scelta=="2":
                self.aggiungi_allievo()
            elif scelta=="3":
                self.aggiorna_allievo()
            elif scelta=="4":
                self.elimina_allievo()
            elif scelta=="5":
                break
            else:
                print("Scelta non valida")

if __name__=="__main__":
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='scuoladb'

    ) 

scuola_manager=Allievo(conn)
scuola_manager.menu()
scuola_manager.cursor.close()
scuola_manager.conn.close()                                                              



    
         
