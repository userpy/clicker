import requests
import random
import re
#text-digital generator for short links, not recommended for use with passwords

class RandomCodeGen(object):
    def __init__(self, width: 'int', auto=False):
        self.width = int(width)
        self.litera = ''
        if auto:
            self.textDigital()
    #по умолчанию генерирует текст и цифры
    def __literalgen(self, start, stop):
        for i in range(self.width):
            random_choice = random.randrange(start, stop)

            if random_choice == 0:
                # _
                symbol = chr(95)
            elif random_choice == 1:
                #DIGITAL
                symbol = chr(random.randrange(48, 57))
            elif random_choice == 2:
                #UPPER_CASE
                symbol = chr(random.randrange(65, 90))
            elif random_choice == 3:
                #LOVER_CASE
                symbol = chr(random.randrange(97, 122))
            self.litera += symbol

    def textDigital(self):
        self.__literalgen(0,4)

    def text(self):
        self.__literalgen(2, 4)

    def textUperCase(self):
        self.__literalgen(2,3)

    def textLowerCase(self):
        self.__literalgen(3,4)

    def data(self):
        return self.litera

    def __str__(self):
        # for print and str
        return self.litera
    def __repr__(self):
        # for json
        return  self.litera

    def __doc__(self):
        return '''
        text-digital generator for short links,do not recommended for use with passwords
         *******************************************************************************
         Функции:
            textDigital() - Цифры и буквы верхнего и нижнего регистра
            text() - буквы верхнего и нижнего регистра
            textUperCase(s) - буквы верхнего регистра
            textLowerCase() - буквы  нижнего регистра
        '''

class LinkCreator(RandomCodeGen):
    def __init__(self, width, url, model, template):
        RandomCodeGen.__init__(self, width, auto=True)
        self.url = url
        self.model = model
        self.template = template
        self.__getlink()


    def __getlink(self):
        Links =  self.model
        link = Links.objects.filter(code=self.litera)
        if len(link) > 0:
            self.__textDigital()
            self.__getlink()
        else:
            link_save = Links(code=self.litera, url=self.url)
            link_save.save()


    def data(self):
        return self.template + self.litera


    def __doc__(self):
        return '''
            Создание ссылки
        '''




class LinkControl:
    # Проверка работоспособности ссылки
    def __init__(self, link):
        self.link = link
        self.status = None
        self.__requests()
    def __requests(self):
        try:
            requests.get(self.link)
            self.status = True
        except:
            self.status = False
    def __bool__(self):
        return self.status