import datetime


def tryDate(elements):
    """
    Verifica tipul de data
    :param elements: lista cu elementele citite
    :return: 0 daca nu indeplineste conditia
    """
    try:
        copy = elements[2]
        day, month, year = map(int, copy.split('-'))
        date2 = datetime.date(day, month, year)
    except ValueError:
        print('Data introdusa gresita')
        return 0
    except IndexError:
        print('Nu ati citit destule date (4)')
        return 0

def tryDate2():
    """
    Verifica tipul de data
    :return: 0 daca nu indeplineste conditia
    """
    try:
        date = input('Data (AAAA-LL-ZZ) : ')
        day, month, year = map(int, date.split('-'))
        date2 = datetime.date(day, month, year)
    except ValueError:
        print('Data introdusa gresita')
        return 0
    except IndexError:
        print('Nu ati citit destule date (4)')
        return 0
    else:
        return str(date2)

def tryNumber(elements):
    """
        Verifica tipul de data
        :param elements: lista cu elementele citite
        :return: 0 daca nu indeplineste conditia
        """
    try:
        copy = int(elements[0])-1
    except ValueError:
        print('Nu ati introdus un numar la NR')
        return 0
    except IndexError:
        print('Nu ati citit destule date (4)')
        return 0


def trySum(elements):
    """
        Verifica tipul de data
        :param elements: lista cu elementele citite
        :return: 0 daca nu indeplineste conditia
        """
    try:
        copy = int(elements[1])
    except ValueError:
        print('Nu ati introdus un numar la Suma')
        return 0


def tryType(elements):
    """
        Verifica tipul de data
        :param elements: lista cu elementele citite
        :return: 0 daca nu indeplineste conditia
        """
    try:
        if elements[3].isdigit():
            print('Nu ati introdus un cuvant la Tipul')
            return 0
    except IndexError:
        print('Nu ati citit destule date (4)')
        return 0


def tryNumber2():
    """
        Verifica tipul de data
        :return: 0 daca nu indeplineste conditia
        """
    try:
        number = int(input('Cate elemente cititi?: '))
    except ValueError:
        print('Nu ati introdus o cifra')
        return 0
    else:
        return number

def tryNumber3():
    """
        Verifica tipul de data
        :return: 0 daca nu indeplineste conditia
        """
    try:
        elements = input('Apartamentul: ')
        copy = int(elements)
    except ValueError:
        print('Nu ati introdus un numar de apartament')
        return 0
    else:
        return str(copy)

def tryType2(data):
    element = input('Ce modificati la factura ' + str(data) + ' ?: ')
    if element.lower() == 'nr':
        return element
    if element.lower() == 'suma':
        return element
    if element.lower() == 'tipul':
        return element
    print('Nu ati introdus corect modificarea (NR sau Suma sau Tipul)')
    return 0

def tryNumber4():
    """
        Verifica tipul de data
        :return: 0 daca nu indeplineste conditia
        """
    try:
        elements = input('Suma: ')
        copy = int(elements)
    except ValueError:
        print('Nu ati introdus un numar')
        return 0
    else:
        return str(copy)
