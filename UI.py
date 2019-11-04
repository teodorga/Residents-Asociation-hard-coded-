import processing


def showMenu():
    """
    Afisarea meniului
    """
    print('1 - Afisare')
    print('2 - Adaugare / Stergere / Modificare')
    print('3 - Adaugare suma la o data specifica')
    print('4 - Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială')
    print('5 - Ordonarea cheltuielilor descrescător după sumă')
    print('6 - Afișarea sumelor lunare pentru fiecare apartament')
    print('7 - Undo')


def showMenuPack1():
    """
    Afiseaza pachetul de meniu 1
    """
    print('a - Adaugare')
    print('b - Stergere')
    print('c - Modificare')


def showList(elements):
    """
    Afisarea elementelor
    :param elements: Lista elementelor
    """

    for index in elements:
        vector = elements[index]
        print('Factura', index, ': NR', vector['NR'], ', Suma:', vector['Suma'], ', Data:', vector['Data'], ', Tipul:',
              vector['Tipul'])


def showDates(elements):
    """
    Afisarea sumelor in fiecare luna per apartament
    :param elements: Lista cu elemente
    """
    data = []
    for index in range(len(elements)):
        OK = 0
        for index2 in data:
            if elements[index]['NR'] == index2:
                OK = 1
        if OK == 0:
            data.append(elements[index]['NR'])
    for flat in data:
        print('Apartamentul:', flat)
        for index in range(len(elements)):
            if flat == elements[index]['NR']:
                print('Anul:', elements[index]['Anul'], 'luna', elements[index]['Luna'], '| Suma:',
                      elements[index]['Suma'])


def maxPriceByType(elements):
    """
    Calculeaza suma maxima pentru fiecare Tip
    :param elements: Lista elementelor
    """
    try:
        vector = []
        for index in range(len(elements)):
            location = processing.checkIfExistsType(elements[index + 1]['Tipul'], vector)
            if location == 0:
                vector.append(elements[index + 1]['Tipul'])
                vector.append(elements[index + 1]['Suma'])
            else:
                if int(elements[index + 1]['Suma']) > int(vector[location]):
                    vector[location] = elements[index + 1]['Suma']
        for index in range(0, len(vector), 2):
            print('Tipul:', vector[index], '| Suma maxima:', vector[index + 1])
    except KeyError:
        pass
