class Aluno:

    def __init__(self, nome, curso, tempoSemDormir):
        self._Nome = nome
        self._Curso = curso
        self._TempoSemDormir = tempoSemDormir

    @property
    def nome(self):
        return self._Nome
    @nome.setter
    def nome(self, nome):
        self._Nome = nome

    @property
    def curso(self):
        return self._Curso
    @curso.setter
    def curso(self, curso):
        self._Curso = curso

    @property
    def tempoSemDormir(self):
        return self._TempoSemDormir
    @tempoSemDormir.setter
    def tempoSemDormir(self, tempoSemDormir):
        self._TempoSemDormir = tempoSemDormir

    def estudar(self, qtdHorasEstudo):
        self._TempoSemDormir += qtdHorasEstudo

    def dormir(self, qtdHorasSono):
        self._TempoSemDormir -= qtdHorasSono
        if(self._TempoSemDormir < 0):
            self._TempoSemDormir = 0
            print('\nVocê não está sem dormir.')