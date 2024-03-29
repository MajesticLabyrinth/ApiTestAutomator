class geeks:
    course = 'DSA'

    def purchase(self):
        print('Purchase course : ', self.course)

geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()