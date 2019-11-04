import UI
import processing
import copy


def main():
    """
     Programul principal
    """
    elements = processing.readData()
    undo = []
    while True:
        UI.showMenu()
        command = input('Comanda: ')
        # 1 - Afisarea elementelor
        if command == '1':
            UI.showList(elements)
        else:
            # 2 - Sub meniu comenzi
            if command == '2':
                UI.showMenuPack1()
                command = input('Comanda: ')
                # a - Adaugare element nou
                if command == 'a':
                    undo = elements.copy()
                    processing.addFlat(elements)
                else:
                    # b - Stergere element dupa numarul facturii
                    if command == 'b':
                        undo = elements.copy()
                        while True:
                            elements = processing.delFlat(undo)
                            if elements != 0:
                                break
                    else:
                        # c - Modificare date element dupa numarul facturii
                        if command == 'c':
                            undo = copy.deepcopy(elements)
                            elements = processing.changeData(elements)
            else:
                # 3 - Adaugare suma la o data specifica
                if command == '3':
                    undo = elements.copy()
                    processing.changePrice(elements)
                else:
                    # 4 - Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială
                    if command == '4':
                        undo = elements.copy()
                        UI.maxPriceByType(elements)
                    else:
                        # 5 - Ordonarea cheltuielilor descrescător după sumă.
                        if command == '5':
                            undo = elements.copy()
                            print('Lista sortata dupa Suma')
                            processing.sumSorted(elements)
                        else:
                            # 6 - Afișarea sumelor lunare pentru fiecare apartament
                            if command == '6':
                                undo = elements.copy()
                                UI.showDates(processing.sumByMonth(elements))
                            else:
                                # 7 - Undo
                                if command == '7':
                                    elements = undo
                                else:
                                    if command == '8':
                                        print(undo)


main()
