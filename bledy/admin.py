from django.contrib import admin
from .models import RodzajeBledu, GrupaRobocza, Klient, Wiazka, Dzial, Pracownik, Autor, Bledy, RodzajReklamacji, Csv


@admin.register(RodzajeBledu)
class BladAdmin(admin.ModelAdmin):
    list_display = ('blad', 'aktywny')
    list_filter = ('blad', 'aktywny')
    search_fields = ('blad', 'aktywny')


@admin.register(GrupaRobocza)
class GrupaRoboczaAdmin(admin.ModelAdmin):
    list_display = ('nr_grupy', 'aktywna')
    list_filter = ('nr_grupy', 'aktywna')
    search_fields = ('nr_grupy', 'aktywna')


@admin.register(Klient)
class KlientAdmin(admin.ModelAdmin):
    list_display = ('nazwa_klienta', 'aktywny')
    list_filter = ('nazwa_klienta', 'aktywny')
    search_fields = ('nazwa_klienta', 'aktywny')


@admin.register(Wiazka)
class WiazkaAdmin(admin.ModelAdmin):
    list_display = ('nazwa_wiazki', 'nazwa_klienta', 'aktywny')
    list_filter = ('nazwa_wiazki', 'nazwa_klienta', 'aktywny')
    search_fields = ('nazwa_wiazki', 'nazwa_klienta', 'aktywny')


@admin.register(Dzial)
class DzialAdmin(admin.ModelAdmin):
    list_display = ('dzial', 'aktywny')
    list_filter = ('dzial', 'aktywny')
    search_fields = ('dzial', 'aktywny')


@admin.register(Pracownik)
class PracownikAdmin(admin.ModelAdmin):
    list_display = ('nr_pracownika', 'imie', 'nazwisko', 'dzial', 'zatrudniony')
    list_filter = ('nr_pracownika', 'imie', 'nazwisko', 'dzial', 'zatrudniony')
    search_fields = ('nr_pracownika', 'imie', 'nazwisko', 'dzial', 'zatrudniony')


@admin.register(RodzajReklamacji)
class RodzajReklamacji(admin.ModelAdmin):
    list_display = ('rodzaj', 'aktywny')
    list_filter = ('rodzaj', 'aktywny')
    search_fields = ('rodzaj', 'aktywny')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'dzial')
    list_filter = ('user', 'dzial')
    search_fields = ('user', 'dzial')


@admin.register(Bledy)
class BledyAdmin(admin.ModelAdmin):
    list_display = (
            'nr_wiazki',
            'nr_grupy_roboczej',
            'nr_zlecenia',
            'nr_kontrolera',
            'nr_budujacego',
            'ilosc_skontrolowanych',
            'ilosc_bledow',
            'blad',
            'autor_wpisu',
            'komputer_user',
            'komputer',
            'data_dodania',
            'skasowany'
    )
    list_filter = (
            'nr_wiazki',
            'nr_grupy_roboczej',
            'nr_zlecenia',
            'nr_kontrolera',
            'nr_budujacego',
            'ilosc_skontrolowanych',
            'ilosc_bledow',
            'blad',
            'autor_wpisu',
            'komputer_user',
            'komputer',
            'data_dodania',
            'skasowany'
    )
    search_fields = (
            'nr_wiazki',
            'nr_grupy_roboczej',
            'nr_zlecenia',
            'nr_kontrolera',
            'nr_budujacego',
            'ilosc_skontrolowanych',
            'ilosc_bledow',
            'blad',
            'autor_wpisu',
            'komputer_user',
            'komputer',
            'data_dodania',
            'skasowany'
    )


# -- TEST CSV ------------------------------------------------
admin.site.register(Csv)

