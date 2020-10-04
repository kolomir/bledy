from django.shortcuts import render, get_object_or_404, redirect
from .models import Bledy, Klient, GrupaRobocza, Dzial, RodzajeBledu, Wiazka, Pracownik, Autor, RodzajReklamacji
from .forms import KlientForm, SkasowacKlienci, GrupaRoboczaForm, SkasowacGrupaRobocza, DzialForm, SkasowacDzial, \
                BladForm, SkasowacBlad, WiazkaForm, SkasowacWiazka, PracownikForm, SkasowacPracownik, BledyForm, SkasowacBledy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def get_author(user):
    qs = Autor.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def wszystkie_wpisy(request):
    wszystkie_wpisy = Bledy.objects.filter(skasowany=False).order_by('id').reverse()

    context = {
        'wszystkie_wpisy': wszystkie_wpisy
    }

    return render(request, 'bledy/wszystkie_wpisy.html', context)


@login_required
def nowy_klient(request):
    form_klienci = KlientForm(request.POST or None, request.FILES or None)

    if form_klienci.is_valid():
        form_klienci.save()
        return redirect(wpisyKlient)

    context = {
        'form_klienci': form_klienci
    }

    return render(request, 'bledy/form_klient.html', context)


@login_required
def edytuj_klient(request, id):
    wpis = get_object_or_404(Klient, pk=id)

    form_klienci = KlientForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_klienci.is_valid():
        form_klienci.save()
        return redirect(wpisyKlient)

    context = {
        'form_klienci': form_klienci,
        'wpis': wpis
    }

    return render(request, 'bledy/form_klient_ed.html', context)


@login_required
def usun_klient(request, id):
    wpis = get_object_or_404(Klient, pk=id)
    form_wpis = SkasowacKlienci(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 0
        kasuj.save()
        return redirect(wpisyKlient)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_klient.html', context)


@login_required
def przywroc_klient(request, id):
    wpis = get_object_or_404(Klient, pk=id)
    form_wpis = SkasowacKlienci(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 1
        kasuj.save()
        return redirect(wpisyKlient)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_klient.html', context)


def wpisyKlient(request):
    klienci = Klient.objects.all().order_by('nazwa_klienta')

    context = {
        'klienci': klienci
    }
    return render(request,'bledy/klienci.html',context)


@login_required
def nowa_grupa(request):
    form_grupy = GrupaRoboczaForm(request.POST or None, request.FILES or None)

    if form_grupy.is_valid():
        form_grupy.save()
        return redirect(wpisyGrupaRobocza)

    context = {
        'form_grupy': form_grupy
    }

    return render(request, 'bledy/form_grupa.html', context)


@login_required
def edytuj_grupa(request, id):
    wpis = get_object_or_404(GrupaRobocza, pk=id)

    form_grupy = GrupaRoboczaForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_grupy.is_valid():
        form_grupy.save()
        return redirect(wpisyGrupaRobocza)

    context = {
        'form_grupy': form_grupy,
        'wpis': wpis
    }

    return render(request, 'bledy/form_grupa_ed.html', context)


@login_required
def usun_grupa(request, id):
    wpis = get_object_or_404(GrupaRobocza, pk=id)
    form_wpis = SkasowacGrupaRobocza(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywna = 0
        kasuj.save()
        return redirect(wpisyGrupaRobocza)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_grupa.html', context)


@login_required
def przywroc_grupa(request, id):
    wpis = get_object_or_404(GrupaRobocza, pk=id)
    form_wpis = SkasowacGrupaRobocza(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywna = 1
        kasuj.save()
        return redirect(wpisyGrupaRobocza)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_grupa.html', context)


def wpisyGrupaRobocza(request):
    grupy_robocze = GrupaRobocza.objects.all().order_by('nr_grupy')

    context = {
        'grupy_robocze': grupy_robocze
    }
    return render(request, 'bledy/grupyrobocze.html', context)


@login_required
def nowy_dzial(request):
    form_dzial = DzialForm(request.POST or None, request.FILES or None)

    if form_dzial.is_valid():
        form_dzial.save()
        return redirect(wpisyDzialy)

    context = {
        'form_dzial': form_dzial
    }

    return render(request, 'bledy/form_dzial.html', context)


@login_required
def edytuj_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)

    form_dzial = DzialForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_dzial.is_valid():
        form_dzial.save()
        return redirect(wpisyDzialy)

    context = {
        'form_dzial': form_dzial,
        'wpis': wpis
    }

    return render(request, 'bledy/form_dzial_ed.html', context)


@login_required
def usun_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)
    form_wpis = SkasowacDzial(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 0
        kasuj.save()
        return redirect(wpisyDzialy)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_dzial.html', context)


@login_required
def przywroc_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)
    form_wpis = SkasowacDzial(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 1
        kasuj.save()
        return redirect(wpisyDzialy)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_dzial.html', context)


def wpisyDzialy(request):
    dzialy = Dzial.objects.all().order_by('dzial')

    context = {
        'dzialy': dzialy
    }
    return render(request,'bledy/dzialy.html',context)


@login_required
def nowy_blad(request):
    form_blad = BladForm(request.POST or None, request.FILES or None)

    if form_blad.is_valid():
        form_blad.save()
        return redirect(wpisyBlad)

    context = {
        'form_blad': form_blad
    }

    return render(request, 'bledy/form_bledy.html', context)


@login_required
def edytuj_blad(request, id):
    wpis = get_object_or_404(RodzajeBledu, pk=id)

    form_blad = BladForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_blad.is_valid():
        form_blad.save()
        return redirect(wpisyBlad)

    context = {
        'form_blad': form_blad,
        'wpis': wpis
    }

    return render(request, 'bledy/form_bledy_ed.html', context)


@login_required
def usun_blad(request, id):
    wpis = get_object_or_404(RodzajeBledu, pk=id)
    form_wpis = SkasowacBlad(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 0
        kasuj.save()
        return redirect(wpisyBlad)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_blad.html', context)


@login_required
def przywroc_blad(request, id):
    wpis = get_object_or_404(RodzajeBledu, pk=id)
    form_wpis = SkasowacBlad(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 1
        kasuj.save()
        return redirect(wpisyBlad)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdx_blad.html', context)


def wpisyBlad(request):
    bledy = RodzajeBledu.objects.all().order_by('blad')

    context = {
        'bledy': bledy
    }
    return render(request, 'bledy/bledy.html', context)


@login_required
def nowa_wiazka(request):
    form_wiazka = WiazkaForm(request.POST or None, request.FILES or None)
    klient = Klient.objects.all().order_by('nazwa_klienta')

    if form_wiazka.is_valid():
        form_wiazka.save()
        return redirect(wpisyWiazka)

    context = {
        'form_wiazka': form_wiazka,
        'klient': klient
    }

    return render(request, 'bledy/form_wiazka.html', context)


@login_required
def edytuj_wiazka(request, id):
    wpis = get_object_or_404(Wiazka, pk=id)
    klient = Klient.objects.all().order_by('nazwa_klienta')

    form_wiazka = WiazkaForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_wiazka.is_valid():
        form_wiazka.save()
        return redirect(wpisyWiazka)

    context = {
        'form_wiazka': form_wiazka,
        'wpis': wpis,
        'klient': klient
    }

    return render(request, 'bledy/form_wiazka_ed.html', context)


@login_required
def usun_wiazke(request, id):
    wpis = get_object_or_404(Wiazka, pk=id)
    form_wpis = SkasowacWiazka(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 0
        kasuj.save()
        return redirect(wpisyWiazka)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_wiazka.html', context)


@login_required
def przywroc_wiazke(request, id):
    wpis = get_object_or_404(Wiazka, pk=id)
    form_wpis = SkasowacWiazka(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 1
        kasuj.save()
        return redirect(wpisyWiazka)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_wiazka.html', context)


def wpisyWiazka(request):
    wiazka = Wiazka.objects.all().order_by('nazwa_wiazki')

    context = {
        'wiazka': wiazka
    }
    return render(request,'bledy/wiazka.html',context)


@login_required
def nowy_pracownik(request):
    form_pracownik = PracownikForm(request.POST or None, request.FILES or None)
    dzial = Dzial.objects.all().order_by('dzial')

    if form_pracownik.is_valid():
        form_pracownik.save()
        return redirect(wpisyPracownik)

    context = {
        'form_pracownik': form_pracownik,
        'dzial': dzial
    }

    return render(request, 'bledy/form_pracownik.html', context)


@login_required
def edytuj_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    dzial = Dzial.objects.all().order_by('dzial')
    form_pracownik = PracownikForm(request.POST or None, request.FILES or None, instance=wpis)
    print(form_pracownik)
    if form_pracownik.is_valid():
        form_pracownik.save()
        return redirect(wpisyPracownik)

    context = {
        'form_pracownik': form_pracownik,
        'wpis': wpis,
        'dzial': dzial
    }

    return render(request, 'bledy/form_pracownik_ed.html', context)


@login_required
def usun_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    form_wpis = SkasowacPracownik(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.zatrudniony = 0
        kasuj.save()
        return redirect(wpisyPracownik)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_pracownik.html', context)


@login_required
def przywroc_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    form_wpis = SkasowacPracownik(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.zatrudniony = 1
        kasuj.save()
        return redirect(wpisyPracownik)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz_pracownik.html', context)


def wpisyPracownik(request):
    pracownik = Pracownik.objects.all().order_by('nr_pracownika')

    context = {
        'pracownik': pracownik
    }
    return render(request,'bledy/pracownik.html',context)


@login_required
def nowy_blad_wpis(request):
    form_blad_wpis = BledyForm(request.POST or None, request.FILES or None)
    wiazka = Wiazka.objects.all().order_by('nazwa_wiazki')
    grupa = GrupaRobocza.objects.all().order_by('nr_grupy')
    budujacy = Pracownik.objects.all().order_by('nr_pracownika')
    rodzajBledu = RodzajeBledu.objects.all().order_by('blad')
    rodzajReklamacji = RodzajReklamacji.objects.all().order_by('rodzaj')

    if form_blad_wpis.is_valid():
        autor = get_author(request.user)
        form_blad_wpis.instance.autor_wpisu = autor
        form_blad_wpis.save()
        return redirect(wszystkie_wpisy)

    context = {
        'form_blad_wpis': form_blad_wpis,
        'wiazka': wiazka,
        'grupa': grupa,
        'budujacy': budujacy,
        'rodzajBledu': rodzajBledu,
        'rodzajReklamacji': rodzajReklamacji
    }

    return render(request, 'bledy/form_bledy_wpisy.html', context)


@login_required
def edytuj_blad_wpis(request, id):
    wpis = get_object_or_404(Bledy, pk=id)

    wpisy = BledyForm(request.POST or None, request.FILES or None, instance=wpis)
    wiazka = Wiazka.objects.all().order_by('nazwa_wiazki')
    grupa = GrupaRobocza.objects.all().order_by('nr_grupy')
    budujacy = Pracownik.objects.all().order_by('nr_pracownika')
    rodzajBledu = RodzajeBledu.objects.all().order_by('blad')
    rodzajReklamacji = RodzajReklamacji.objects.all().order_by('rodzaj')

    if wpisy.is_valid():
        wpisy.save()
        return redirect(wszystkie_wpisy)

    context = {
        'wpisy': wpisy,
        'wpis': wpis,
        'wiazka': wiazka,
        'grupa': grupa,
        'budujacy': budujacy,
        'rodzajBledu': rodzajBledu,
        'rodzajReklamacji': rodzajReklamacji
    }
    #print('rodzajReklamacji:', wpisy.instance.rodzaj_reklamacji)

    return render(request, 'bledy/form_bledy_wpisy_ed.html', context)


@login_required
def usun_blad_wpis(request, id):
    wpis = get_object_or_404(Bledy, pk=id)
    form_blad_wpis = SkasowacBledy(request.POST or None, request.FILES or None, instance=wpis)

    if form_blad_wpis.is_valid():
        kasuj = form_blad_wpis.save(commit=False)
        kasuj.skasowany = 1
        kasuj.save()
        return redirect(wszystkie_wpisy)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz.html', context)


@login_required
def przywroc_blad_wpis(request, id):
    wpis = get_object_or_404(Bledy, pk=id)
    form_blad_wpis = SkasowacBledy(request.POST or None, request.FILES or None, instance=wpis)

    if form_blad_wpis.is_valid():
        kasuj = form_blad_wpis.save(commit=False)
        kasuj.skasowany = 0
        kasuj.save()
        return redirect(wszystkie_wpisy)

    context = {
        'wpis': wpis
    }
    return render(request, 'bledy/potwierdz.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required
def filtrowanie(request):
    qs = Bledy.objects.all()
    nr_wiazki_contains_query = request.GET.get('nr_wiazki_contains')
    nr_grupy_roboczej_contains_query = request.GET.get('nr_grupy_roboczej_contains')
    nr_zlecenia_contains_query = request.GET.get('nr_zlecenia_contains')
    nr_kontrolera_contains_query = request.GET.get('nr_kontrolera_contains')
    nr_budujacego_contains_query = request.GET.get('nr_budujacego_contains')
    blad_contains_query = request.GET.get('blad_contains')
    data_od = request.GET.get('data_od')
    data_do = request.GET.get('data_do')
    eksport = request.GET.get('eksport')

    if is_valid_queryparam(nr_wiazki_contains_query):
        qs = qs.filter(nr_wiazki__icontains=nr_wiazki_contains_query)
    if is_valid_queryparam(nr_grupy_roboczej_contains_query):
        qs = qs.filter(nr_grupy_roboczej__icontains=nr_grupy_roboczej_contains_query)
    if is_valid_queryparam(nr_zlecenia_contains_query):
        qs = qs.filter(nr_zlecenia__icontains=nr_zlecenia_contains_query)
    if is_valid_queryparam(nr_kontrolera_contains_query):
        qs = qs.filter(nr_kontrolera__icontains=nr_kontrolera_contains_query)
    if is_valid_queryparam(nr_budujacego_contains_query):
        qs = qs.filter(nr_budujacego__icontains=nr_budujacego_contains_query)
    if is_valid_queryparam(blad_contains_query):
        qs = qs.filter(blad__icontains=blad_contains_query)
    if is_valid_queryparam(data_od):
        qs = qs.filter(data_dodania__gte=data_od)
    if is_valid_queryparam(data_do):
        qs = qs.filter(data_dodania__lt=data_do)

    if eksport == 'on':

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="eksport.csv"'
        response.write(u'\ufeff'.encode('utf8'))

        mojaData = datetime.now()
        formatedDate = mojaData.strftime("%Y-%m-%d")

        print(formatedDate)

        writer = csv.writer(response)
        writer.writerow(
            [
                'nr_wiazki',
                'nr_grupy_roboczej',
                'nr_zlecenia',
                'nr_kontrolera',
                'nr_budujacego',
                'ilosc_skontrolowanych',
                'ilosc_bledow',
                'blad',
                'rodzaj_reklamacji',
                'autor_wpisu',
                'data_dodania'
            ]
        )

        for obj in qs:
            writer.writerow(
                [
                    obj.nr_wiazki,
                    obj.nr_grupy_roboczej,
                    obj.nr_zlecenia,
                    obj.nr_kontrolera,
                    obj.nr_budujacego,
                    obj.ilosc_skontrolowanych,
                    obj.ilosc_bledow,
                    obj.blad,
                    obj.rodzaj_reklamacji,
                    obj.autor_wpisu,
                    obj.data_dodania
                ]
            )
        return response

    context = {
        'queryset': qs,
    }
    return render(request, 'bledy/eksport.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info( request, f"Witaj {username}! Właśnie się zalogowałeś.")
                return redirect("/")
            else:
                messages.error(request, f"Błędny login lub hasło")
        else:
            messages.error(request, f"- Błędny login lub hasło -")
    form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "bledy/login.html", context)



