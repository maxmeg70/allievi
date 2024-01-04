import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'root',
    database = 'scuoladb'
)

cursor=conn.cursor()

def visualizzaAllievi():
    query='SELECT * FROM allievi'
    cursor.execute(query)
    result=cursor.fetchall()

    for row in result:
        print(row)

def aggiungiAllievo():
    nome_allievo = input('Inserisci nome: ')
    cognome_allievo=input('Inserisci cognome: ')
    indirizzo_allievo=input('Inserisci indirizzo: ')
    telefono_allievo=input('Inserisci telefono: ')
    email_allievo=input('Inserisci indirizzo email: ')
    corso=input('Inserisci corso: ')
    data_iscrizione=input('Inserisci data iscrizione: ')
    try:
        query='INSERT INTO allievi(nome, cognome, indirizzo, telefono, email, corso, dataIscrizione) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        values=(nome_allievo, cognome_allievo,indirizzo_allievo, telefono_allievo,email_allievo, corso,data_iscrizione)
        cursor.execute(query, values)
        conn.commit()
        print('Allievo inserito correttamente')
    except mysql.connector.Error as e:
        print(f'Errore nella creazione del record : {e}')

def aggiornaAllievo():
    id_allievo=int(input('Inserisci id allievo da aggiornare: '))
    nome_allievo_m = input('Modifica nome: ')
    cognome_allievo_m=input('Modifica cognome: ')
    indirizzo_allievo_m=input('Modifica indirizzo: ')
    telefono_allievo_m=input('Modifica telefono: ')
    email_allievo_m=input('Modifica email: ')
    corso_m=input('Modifica corso: ')
    data_iscrizione_m=input('Modifica data iscrizione: ')
    data_disiscrizione_m=input('Inserisci data da disiscrizione: ')
    try:
        query='UPDATE allievi SET nome=%s, cognome=%s, indirizzo=%s, telefono=%s, email=%s, corso=%s, dataIscrizione=%s, dataDisiscrizione=%s WHERE id=%s'
        values=(nome_allievo_m, cognome_allievo_m, indirizzo_allievo_m, telefono_allievo_m, email_allievo_m, corso_m, data_iscrizione_m, data_disiscrizione_m, id_allievo)
        cursor.execute(query, values)
        conn.commit()
        print('Allievo modificato correttamente')
    except mysql.connector.Error as e:
        print(f'Errore nell\'aggiornamento del record: {e}')


def eliminaAllievo():
    id_allievo_da_eliminare=int(input('Inserisci id allievo da eliminare: '))
    try:
        query='DELETE FROM allievi WHERE id=%s'
        values=(id_allievo_da_eliminare, )
        cursor.execute(query, values)
        conn.commit()
        print('Allievo eliminato correttamente')
    except mysql.connector.Error as e :
        print(f'Errore durante l\'eliminazione del record: {e}')
              
def menu():
    while True:
        print('**Menù Principale**')
        print('1. Visualizza allievi')
        print('2. Aggiungi allievi')
        print('3. Aggiorna allievi')
        print('4. Elimina allievi')
        print('5. Esci')

        scelta=input('Inserisci un opzione: ')

        if scelta=="1":
            visualizzaAllievi()
        elif scelta =="2":
            aggiungiAllievo()
        elif scelta=="3":
            aggiornaAllievo()
        elif scelta=="4":
            eliminaAllievo()
        elif scelta=="5":
            print('Grazie per aver utilizzzato il programma')
            break
        else:
            print("Scelta non consentita")


if __name__=='__main__':
    menu()                                

cursor.close()
conn.close()   
    
