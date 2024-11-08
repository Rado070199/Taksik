# Aplikacja Checklist z Integracją w Trayu 📝

## Spis Treści
- [Opis Projektu](#opis-projektu)
- [Funkcje](#funkcje)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Jak Uruchomić](#jak-uruchomić)
- [Dostosowanie](#dostosowanie)
- [Zrzuty Ekranu](#zrzuty-ekranu)
- [Plany na Przyszłość](#plany-na-przyszłość)
- [Licencja](#licencja)

---

## Opis Projektu 🌟

**Aplikacja Checklist** to prosta, lekka aplikacja stworzona w języku Python z użyciem Tkinter, która pozwala użytkownikom zarządzać zadaniami za pomocą graficznej listy kontrolnej. Aplikacja działa w tle jako aplikacja tray i może być łatwo dostępna z ikony w zasobniku systemowym. Dzięki temu jest wygodna dla użytkowników, którzy chcą nieinwazyjnie zarządzać swoimi zadaniami.

Projekt łączy **Tkinter** do interfejsu użytkownika, **pystray** do funkcjonalności zasobnika oraz **Pillow** do tworzenia lub ładowania ikon. Użytkownicy mogą zaznaczać i odznaczać zadania oraz minimalizować okno, mając jednocześnie możliwość zarządzania aplikacją z poziomu trayu.

---

## Funkcje ✅

- **Graficzna Lista Kontrolna**: Wyświetla listę zadań, które można zaznaczać i odznaczać.
- **Ikona w Tray**: Aplikacja działa w trayu, umożliwiając szybki dostęp do listy kontrolnej.
- **Możliwość Zamykania i Pokazywania Okna**: Użytkownik może ukryć okno aplikacji, pozostawiając je w zasobniku.
- **Prosta i Lekka**: Aplikacja jest łatwa w użyciu i nie zajmuje dużo zasobów systemowych.

---

## Wymagania ⚙️

Upewnij się, że masz zainstalowane:
- Python 3.x
- Wymagane biblioteki Pythona: `tkinter`, `pystray`, `Pillow`

### Instalacja Zależności
Aby zainstalować wymagane biblioteki, użyj poniższego polecenia:
```bash
pip install pystray pillow
```

### Plany na Przyszłość 🔮
* Dodanie Funkcjonalności Zapisywania Stanu: Umożliwienie użytkownikom zapisywania i wczytywania stanu listy kontrolnej między sesjami.
* Możliwość Dodawania i Usuwania Zadań: Dodanie opcji do dynamicznego dodawania lub usuwania zadań z listy.
* Przypomnienia: Implementacja funkcji przypomnień dla użytkowników, aby nie zapomnieli o zadaniach.
* dostosowanie Wyglądu: Umożliwienie użytkownikom zmiany kolorów i stylów aplikacji dla lepszego dopasowania do ich preferencji.
* Obsługa wielojęzyczna: Dodanie wsparcia dla wielu języków, aby aplikacja była dostępna dla szerszego kręgu użytkowników.

* Dodać opcje w ustawieniach samopoczucie dzisiaj i trudność zadań umysłowych
