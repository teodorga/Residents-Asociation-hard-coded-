import processing
import copy
import time
import UI


def test_checkIfExists():
    """
    Testeaza functia checkIfExists din PROCESSING
    """
    elements = {
        1: {
            'NR': '1',
            'Suma': '20',
            'Data': '2000-01-01',
            'Tipul': 'canal'
        },
        2: {
            'NR': '2',
            'Suma': '20',
            'Data': '2000-01-01',
            'Tipul': 'apa'
        }
    }
    newData = ['1', '01', '01', 'canal']
    data = '2000-01-01'
    newData2 = ['2', '01', '01', 'canal']
    data2 = '2000-01-02'
    time.sleep(1)
    print('FUNCTIA checkIfExists() verificata cu SUCCES <!>')
    print('\n')
    assert processing.checkIfExists(elements, newData, data) == 1
    assert processing.checkIfExists(elements, newData2, data2) == 0


def test_sumSorted():
    vector = processing.readData()
    time.sleep(1.5)
    print('\n')
    print('SORTARE DATE DUPA FISIERUL DATA.TXT <!>')
    print('-------------------------------------------')
    assert processing.sumSorted(vector) != 0


def test_changeData():
    vector = processing.readData()
    vector2 = copy.deepcopy(vector)
    time.sleep(1.5)
    print('FUNCTIA changeData() SE VERIFICA <!!!>')
    for index in vector:
        print(vector[index])
    assert processing.changeData(vector) != vector2
    for index in vector:
        print(vector2[index])


test_checkIfExists()
test_changeData()
test_sumSorted()
