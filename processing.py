import datetime
import tryTests

def readData():
    """
    Citeste datele din fisier
    :return: Dictionarul cu datele elementului
    """
    vector = {}
    f = open('DATA', 'r')
    data2 = f.readline()
    counter = 1
    while data2:
        data = data2.split('/')
        if tryTests.tryDate(data) == 0:
            return 0
        if tryTests.tryNumber(data) == 0:
            return 0
        if tryTests.trySum(data) == 0:
            return 0
        if tryTests.tryType(data) == 0:
            return 0
        if data[3][-1:] == '\n':
            data[3] = data[3][:-1]
        copy = data[2]
        day, month, year = map(int, copy.split('-'))
        date2 = datetime.date(day, month, year)
        date1 = str(date2)
        if checkIfExists(vector, data, date1) == 0:
            dic = {
                'NR': data[0],
                'Suma': data[1],
                'Data': str(date1),
                'Tipul': data[3],
            }
            vector[counter] = dic
            counter = counter + 1
        else:
            print('Date asemanatoare, cititi din nou')
        data2 = f.readline()
    return vector

def checkIfExists(elements, newData, date):
    """
    Verifica daca in lista mai exista acelasi element cu aceleasi detalii
    :param date: String, data ce trebuie verificata
    :param newData: vectorul cu elemente pentru verificare
    :param elements: lista cu elemente
    :return: 1 daca exista, 0 daca nu
    """
    for index in range(len(elements)):
        if elements[index + 1]['NR'] == newData[0] and elements[index + 1]['Data'] == date and \
                elements[index + 1]['Tipul'] == newData[3]:
            return 1
    return 0


def flatCreate(elements, vector):
    """
    Adauga in dictionarul principal noul element
    :param elements: lista cu elemente principale
    :param vector: Lista cu noile date
    :return: Dictionarul cu noile date
    """
    copy = vector[2]
    day, month, year = map(int, copy.split('-'))
    date2 = datetime.date(day, month, year)
    date1 = str(date2)
    if checkIfExists(elements, vector, date1) == 0:
        dic = {
            'NR': vector[0],
            'Suma': vector[1],
            'Data': str(date1),
            'Tipul': vector[3]
        }
        return dic
    else:
        return 0

def readFlat():
    """
    Citeste un nou element de la tastatura
    :return: Returneaza datele
    """
    data = input('Cititi datele noii cheltuieli dupa formatul NR/Suma/Data (AAAA-LL-ZZ)/Tipul: ')
    data2 = data.split('/')
    if tryTests.tryDate(data2) == 0:
        return 0
    if tryTests.tryNumber(data2) == 0:
        return 0
    if tryTests.trySum(data2) == 0:
        return 0
    if tryTests.tryType(data2) == 0:
        return 0
    return data2

def addFlat(elements):
    """
    Adauga un nou element in lista
    :param elements: Lista elementelor
    """
    newPoz = len(elements) + 1
    while True:
        data = readFlat()
        if data == 0:
            break
        if flatCreate(elements, data) != 0:
            elements[newPoz] = flatCreate(elements, data)
            break
        else:
            print('Aceste date exista deja, cititi din nou')

def checkIfExistsNR(data, vector):
    """
    Verifica daca exista un NR dat in lista cu elemente
    :param data: String, NR-ul ce trebuie verificat
    :param vector: Lista cu elemente
    :return: Locatia daca exista elementul cu NR-ul citit, altfel 0
    """
    for index in range(len(vector)):
        if vector[index + 1]['NR'] == data:
            return index + 1
    return 0

def checkIfExistsNR3(data, vector):
    """
    Verifica daca exista un NR dat in lista cu elemente
    :param data: String, NR-ul ce trebuie verificat
    :param vector: Lista cu elemente
    :return: Locatia daca exista elementul cu NR-ul citit, altfel 0
    """
    for index in range(len(vector)):
        if vector[index] == data:
            return index
    return 0

def checkIfExistsNR2(data, vector):
    """
    Verifica daca exista un NR dat in lista cu elemente
    :param data: String, NR-ul ce trebuie verificat
    :param vector: Lista cu elemente
    :return: Locatia daca exista elementul cu NR-ul citit, altfel 0
    """
    for index in range(len(vector)):
        if vector[index] == data:
            return index + 1
    return 0

def checkIfExistsDateAndFlat(data, vector, flat):
    """
    Verifica daca exista data citita in lista cu elemente
    :param flat: numar ce reprezinta id-ul apartamentului ce trebuie verificat
    :param data:  String, Data ce trebuie verificata
    :param vector: Lista cu elemente
    :return: Locatia daca exista elementul cu Data citita, altfel 0
    """

    for index in range(len(vector)):
        if vector[index + 1]['Data'] == data and vector[index + 1]['NR'] == flat:
            return index + 1
    return 0

def checkIfExistsType(data, vector):
    """
    Verifica daca exista Tipul citit in lista cu elemente
    :param data:  String, Tipul ce trebuie verificat
    :param vector: Lista cu elemente
    :return: Locatia daca exista elementul cu Tipul primit, altfel 0
    """
    for index in range(len(vector)):
        if vector[index] == data:
            return index + 1
    return 0


def dates(data, elements):
    vector = []
    for index in range(len(elements)):
        if elements[index + 1]['NR'] == data:
            vector.append(elements[index + 1]['Data'])
            vector.append(elements[index + 1]['Suma'])
    return vector


def sumByMonth(elements):
    """
    Calculeaza suma fiecarui apartament pe luna
    :param elements: Lista elementelor
    """
    vector = []
    flats = []
    sums = []
    counter = 0
    for index in elements:
        flats.append(elements[index]['NR'])
    for index in elements:
        OK = 0
        if elements[index]['NR'] == flats[counter]:
            data = elements[index]['Data'].split('-')
            year = data[0]
            month = data[1]
            for index2 in vector:
                if index2['NR'] == flats[counter] and index2['Anul'] == year and index2['Luna'] == month:
                    OK = 1
            if OK == 0:
                dic = {
                    'NR': flats[counter],
                    'Anul': year,
                    'Luna': month,
                }
                vector.append(dic)
            counter = counter + 1
    for index in vector:
        flat = index['NR']
        year = index['Anul']
        month = index['Luna']
        sumFinal = 0
        for index2 in elements:
            data = elements[index2]['Data'].split('-')
            if elements[index2]['NR'] == flat and data[0] == year and data[1] == month:
                sumFinal = sumFinal + int(elements[index2]['Suma'])
        dic2 = {
            'NR': flat,
            'Anul': year,
            'Luna': month,
            'Suma': sumFinal
        }
        sums.append(dic2)
    return sums

def changePrice(elements):
    """
    Adauga o suma citita la elementele ce au aeeasi data cu cea citita
    :param elements: Lista elementelor
    """
    OK = 0
    while True:
        date = tryTests.tryDate2()
        if date != 0:
            break
    while True:
        addSum = tryTests.tryNumber4()
        if addSum != 0:
            break
    for index in range(len(elements)):
        if elements[index + 1]['Data'] == date:
            elements[index + 1]['Suma'] = int(elements[index + 1]['Suma']) + int(addSum)
            OK = 1
    if OK == 0:
        print('Aceasta data nu exista')

def delFlat(elements):
    """
    Sterge un element din lista
    :param elements: Lista cu elemente
    """
    try:
        flat = int(input('Numarul: '))
        data = elements.copy()
        del data[flat]
        return data
    except KeyError:
        print('Nu exista')
        return 0
    except ValueError:
        print('Nu ati introdus o cifra')
        return 0

def changeData(elements2):
    """
    Modifica datele unui element citit
    :param elements2: Lista cu elemente
    """
    OK = 0
    elements = elements2.copy()
    position = int(input('Factura: '))
    for index in elements2:
        if position == index:
            OK = 1
            while True:
                change = tryTests.tryType2(position)
                if change == 0:
                    break
                change2 = input('Medicare noua: ')
                elements[position][change] = change2
                answer = input('Modificati incontinuare? (Da/Nu):')
                if answer != 'Da':
                    return elements
    if OK == 0:
        print('Aceasta factura nu exista')
    return elements

def sumSorted(data):
    """
    Sorteaza cheltuielele descrescator dupa suma
    :param data: Lista cu elemente
    """
    vector = []
    for index in data:
        vector.append(int(data[index]['Suma']))
    vector.sort(reverse=True)
    for _ in vector:
        for index in data:
            if data[index]['Suma'] == str(_):
                print('Factura', index, ': NR', data[index]['NR'], ', Suma:',
                      data[index]['Suma'], ', Data:', data[index]['Data'], ', Tipul:', data[index]['Tipul'])
