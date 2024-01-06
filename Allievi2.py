import mysql.connector

def database_connection():
    try:
        conn=mysql.connector.connect(
            host = 'localhost',
            user='root',
            password = 'root',
            database = 'scuoladb'
        )
        return conn
    except mysql.connector.Error as e:
        print(f'Errore nella connsessione al database: {e}')

def chiudi_connessione(conn, cursor):
    if conn:
        cursor.close()
        conn.close()
        print('Connessione al database chiusa correttamente')

def visualizza_allievi(conn,cursor):
    try:
        query="SELECT * FROM allievi"
        cursor.execute(query)
        risultato=cursor.fetchall()
        for row in risultato:
            print(row)
    except mysql.connector.Error as e:
        print(f'Errore nella connessiona al database: {e}')

def aggiungi_allievo(conn, cursor):
    nome_allievo=input('Inserisci nome: ')
    cognome_allievo = input('Inserisci cognome: ')
    telefono = input('Inserisci numero di telefono: ')
    email_allievo=input('Inserisci indirizzo email: ')
    corso=input('Inserisci corso: ')
    data_iscrizione = input('Inserisci data iscrizione: ')
    try: 
        query = "INSERT INTO allievi(nome, cognome, telefono, email, corso, dataIscrizione) VALUES(%s,%s,%s,%s,%s,%s)"
        values=(nome_allievo, cognome_allievo, telefono, email_allievo, corso, data_iscrizione)
        cursor.execute(query, values)
        conn.commit()
        print('Record aggiunto correttamente')        
    except mysql.connector.Error as e:
        print(f'Errore connessione al database: {e}')

def aggiorna_allievo(conn, cursor):
    id_allievo= int(input('Inserisci id allievo da modificare: '))
    nome_allievo_m = input('Inserisci nome da modificare: ')
    cognome_allievo_m = input('Inserisci cognome da modificare: ')
    telefono_allievo_m = input('Inserisci numero di telefono da modificare: ')
    email_allievo_m = input('Inserisci email da modificare: ')
    corso_allievo_m = input('Inserisci nuovo corso: ')
    dataiscrizione_m = input('Inserisci nuova data: ')
    try:
        query="UPDATE allievi SET nome=%s, cognome=%s, telefono=%s, email=%s, corso=%s, dataIscrizione=%s WHERE id=%s"
        values=(nome_allievo_m, cognome_allievo_m, telefono_allievo_m,  email_allievo_m, corso_allievo_m, dataiscrizione_m,  id_allievo)
        cursor.execute(query, values)
        conn.commit()
        print('Record aggiornato con successo')
    except mysql.connector.Error as e:
        print(f'Errore connessiona la database: {e}')

def elimina_record(conn,cursor):
    id_allievo = int(input('Inserisci id allievo da eliminare: '))
    try:
        query="DELETE FROM allievi WHERE id=%s"
        values=(id_allievo, )
        cursor.execute(query, values)
        conn.commit()
        print('Record eliminato con successo')
    except mysql.connector.Error as e:
        print(f'Errore connessione al database: {e}')

def menu():
    conn=database_connection()

    if not conn:
        return 'Errore nella connessione al database, rivedi e controlla'

    cursor=conn.cursor()

    while True:
        print('**MENU**')
        print('1. Visualizza allievi')
        print('2. Aggiungi allievo')
        print('3. Aggiorna allievo')
        print('4. Elimina allievo')
        print('5. Esci')

        scelta = input('Scegli opzione: ')

        if scelta=="1":
            visualizza_allievi(conn, cursor)
        elif scelta =="2":
            aggiungi_allievo(conn,cursor)
        elif scelta=="3" : 
            aggiorna_allievo(conn, cursor)
        elif scelta == '4':
            elimina_record(conn, cursor)
        elif scelta == '5':
            break
        else:
            print('Opzione non disponibile !')
    
    chiudi_connessione(conn, cursor)

if __name__=='__main__':
    menu()                            
