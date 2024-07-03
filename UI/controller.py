import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._currentCountry = None

    def handleCalcolaRaggiungibili(self, e):
        raggiungibili = self._model.getRaggiungibili(self._currentCountry)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Da {self._currentCountry} è "
                                                       f"possibile raggiungere a piedi {len(raggiungibili)} stati"))
        for r in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{r}"))

        self._view.update_page()


    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        try:
            anno1 = int(anno)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un valore numerico"))
            self._view.update_page()
            return

        if anno1 < 1816 or anno1 > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un anno tra il 1816 e il 2016"))
            self._view.update_page()
            return

        self._model.buildGraph(anno1)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato!"))
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumCompConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        for n in self._model.getNodes():
            self._view._txt_result.controls.append(ft.Text(f"{n} -- {self._model.getNumConfinanti(n)} vicini"))

        self._view._ddStato.disabled = False
        self._view._btnRaggiungibili.disabled = False

        self.populate_stati()
        self._view.update_page()

    def populate_stati(self):
        stati = self._model.getNodes()
        for stato in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(text=stato.StateNme,
                                                 data=stato,
                                                 on_click=self.leggi_stato))
        self._view.update_page()

    def leggi_stato(self, e):
        print("read_DD_Stato called ")
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data

        print(self._currentCountry)


