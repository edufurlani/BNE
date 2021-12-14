from Extrator_bne import *

extrator = Descritor(r"C:\Users\DuduCuco\Segundo semestre\chromedriver.exe")
extrator.prox_pag()
extrator.salvar_csv('vagas.csv')
print(extrator.candidaturaLivre())
print(extrator.candidaturaPaga())
print(extrator.presencial())
print(extrator.homeOffice())
print(extrator.combinar())

