# ProjektMonikaStrzelec

NAJWAŻNIEJSZE UŻYTE METODY

TRYB DEBUGOWANIA:
Ostatnia linijka kodu zawarta na zrzucie ukazuje programowo włączony tryb debugowania. W aplikacji korzystającej z flask można uruchamiać w trybie debugowania. W tym trybie domyślnie włączone są dwa bardzo wygodne moduły serwera roboczego, o nazwie reloader i debugger. Debugger to narzędzie internetowe, które pojawia się w przeglądarce, gdy aplikacja zgłosi nieobsłużony wyjątek. Okno przeglądarki internetowej przekształca się w interaktywny stos wywołań, który umożliwia sprawdzanie kodu źródłowego aplikacji. Wielokrotnie przydała mi się ta opcja.

RENDEROWANIE I PRZEKIEROWANIE: 
Renderowanie to operacja, która przekształca szablon w pełną stronę HTML. Aby wyrenderować szablon, musiałem zaimportować funkcję, która jest dostarczana z frameworkiem Flask o nazwie render_template().Ta funkcja przyjmuje nazwę pliku szablonu i listę zmiennych argumentów szablonu i zwraca ten sam szablon, ale ze wszystkimi zawartymi w nim symbolami zastępczymi zastąpionymi rzeczywistymi wartościami. Działa to dzięki Jinja2.

Flask-Moment
Ciekawą opcja jest również wykorzystanie tutaj zmiennej current_time=datetime.utcnow(). Jest ona elementem pakietu Flask-Moment i umożliwia pracę, ze znacznikami czasu. Zdecydowałam się skorzystać z możliwości ukazywania czasu na niektórych z podstron przez mnie programowanych.
 
DZIEDZICZENIE SZABLONOW:
Jinja2 ma funkcję dziedziczenia szablonów. Dzięki niemu można przenieść części układu strony, które są wspólne dla wszystkich szablonów, do szablonu podstawowego (base.html), z którego pochodzą wszystkie inne szablony. To właśnie ten plik zajmie się u mnie ogólną strukturą strony.
To blok {% extends „base.html” %} ustanawia związek między dziedziczącymi po sobie szablonami. Oba szablony mają pasujące bloki- instrukcje, z nazwą containt, właśnie w ten sposób Jinja2 wie, jak połączyć oba szablony w jeden. Wykorzystałam ten mechanizm do tworzenia wszystkich stron aplikacji, tak by tworzyły spójną całość bez powielania kodu.

Flask-WTF i SECRET_KAY: 
SECRET_KAY jest to zmienna konfiguracji która jest ważnym elementem w flask-WTF. Flask i niektóre z jego rozszerzeń wykorzystują wartość tajnego klucza jako klucza kryptograficznego, przydatnego do generowania podpisów lub tokenów. Rozszerzenie Flask-WTF używa go do ochrony formularzy internetowych przed różnymi atakami.

FORMULARZ INTERNETOWY: 
Rozszerzenie Flask-WTF używa klas Pythona do reprezentowania formularzy internetowych. Klasa formularza po prostu definiuje pola formularza jako zmienne klasy. Powyżej ukazana klasa służy do przechowywania struktury formularza, który jest następnie używany w pliku .html. Ważne jest by przynajmniej jedna zmienna odpowiadała za przycisk (submit).
W klasie Questionnaire można zaobserwować walidator InputRequired. Jest to niezwykle przydatna opcja która pozwala na sprawdzenie czy dane pole zostało wypełnione. Jeśli dane pole nie zostanie zaznaczone, to przy próbie zapisania formularza na stronie wyświetlają się komunikaty nie pozwalające na zapisanie go.
To również na tym etapie można ograniczyć podawane dane przez użytkowania. Ja akurat użyłam tego tylko przy podawaniu wieku przez użytkownika, zawężając zakres ankietowanych od 5 do 100. (NumberRange(min=5, max=100)). Jednocześnie w wieku używam walidator IntigerField, który sprawia, że użytkownik może wpisać jedynie liczby całkowite.
Inne używane przeze mnie waalidatory to RadioFieled służący do umieszczaniu w formularzu przycisków jednokrotnego wyboru opcji oraz SubmitFieled służącego do odtworzenia przycisku którego jest zadaniem w class Questionnaire przesyłania danych a w class MainSiteForm wywołanie ankiety.

PRZEKIEROWANIE I SESJA UŻYTKOWNIKÓW: 
Widoczna na zrzucie ukazującym element pliku app.py z funkcją @app.route to kolejny obszar, w którym Flask-WTF sprawia, że praca z formularzami staje się prostsza. Na slajdzie widać argument methods w dekoratorze trasy. Informuje to Flaska, że ta funkcja widoku akceptuje żądania GET i POST. Protokół HTTP stwierdza, że żądania GET to te, które zwracają informacje do przeglądarki internetowej. Zapytania POST są zaś zwykle używane, gdy przeglądarka przesyła dane formularza na serwer.
Metoda from.validate_on_submit() służy za przetwarzanie formularza. Kiedy przeglądarka wysyła żądanie GET odebrania strony internetowej z formularzem, ta metoda zwróci false, więc w takim przypadku funkcja pomija instrukcję if i przechodzi bezpośrednio do renderowania szablonu w ostatnim wierszu funkcji. Gdy przeglądarka wyśle żądanie POST w wyniku naciśnięcia przez użytkownika przycisku przesyłania, from.validate_on_submit() zbierze wszystkie dane, uruchomi wszystkie walidatory dołączone do pól i jeśli wszystko jest w porządku, zwróci true wskazując, że dane są prawidłowe i mogą być przetwarzane przez aplikację. Ale jeśli przynajmniej jedno pole nie przejdzie walidacji, funkcja zwróci false, a to spowoduje, że formularz zostanie ponownie wyświetlony użytkownikowi.
Kolejną zastosowana tu funkcja jest redirect() która instruuje przeglądarkę internetową klienta, aby automatycznie przechodziła do innej strony podanej jako argument. Ta funkcja widoku używa go do przekierowania użytkownika do strony /success.html aplikacji.
To również na powyższym slajdzie widać zapisywanie do bazy danych (db.session.add(recort) db.session.commit() ).

RENDEROWANIE FORMULARZA HTML: 
Na powyższym slajdzie widać element .html <form> który jest używany jako kontener dla formularza internetowego.
Można w tym pliku znaleźć atrybut action który służy by poinformować przeglądarkę który element wszedł w formularzu. Gdy akcja jest ustawiona na pusty ciąg, formularz jest przesyłany pod adres URL znajdujący się obecnie w pasku adresu, czyli adres URL, który wyrenderował formularz na stronie. Atrybut method określa metody żądania HTTP, który powinien być używany podczas składania formularza do serwera. Ja skorzystałam tutaj z zapytania post ponieważ zapewnia lepsze wrażenia użytkownika, ponieważ tego typu zapytania mogą przesyłać dane formularza w treści żądania. Atrybut novalidate  który jest opcjonalny, u mnie jest używany, aby powiedzieć przeglądarkę internetową, aby nie stosować do walidacji pól w tej formie, która skutecznie pozostawia to zadanie do wniosku aplikacj uruchomiony na serwerze. 
Form.hidden_tag() generuje ukryte pole, które zawiera znacznik, który jest używany do ochrony formularza przed atakami CSRF. To oraz zmienna SECRET_KEY wystarczają by formularz był chroniony dzięki flask-WTF.
Co ciekawe pola z obiektu formularza wiedzą, jak renderować się jako HTML. Wszystko, co musiałam zrobić, to podać, {{form.<nazwa_pytania>.label gdzie chcę etykietę pola i{{form.<nazwa_pytania>}} tam gdzie chciałam pytanie. W przypadku pól, które wymagają dodatkowych atrybutów HTML, można je przekazać jako argumenty. Ja skorzystałam tu z opcji przekazania błędu {{form.<nazwa_pytania>.errors}} gdzie określiłam kolor komunikatu.
Klasa utworzona powyżej dziedziczy z db.Model która jest klasa bazową dla wszystkich modeli z SQLAlchemy. Ta klasa definiuje kilka pól jako zmienne klasowe. Pola są tworzone jako instancje db.Column klasy, która przyjmuje typ pola jako argument, a także inne opcjonalne argumenty, które na przykład pozwalają wskazać, które pola są unikalne i indeksowane, co jest ważne, aby wyszukiwanie w bazie danych było wydajne.
Na powyższym slajdzie widać __tablename__ = ‘survey’. W SQLAlchemy nie tylko jawnie określamy klucze główne (primary_key=True), ale i podajemy nazwy tabel (__tablename__ = 'klasa').
 
MIGRACJA:
Relacyjne bazy danych są skupione wokół ustrukturyzowanych danych, więc gdy struktura zmienia dane, które już znajdują się w bazie danych, należy je migrować do zmodyfikowanej struktury. Flask-Migrate jest to rozszerzenie współpracujące ze strukturą migracji bazy danych dla SQLAlchemy. Za każdym razem, gdy wprowadzana jest zmiana w schemacie bazy danych, do repozytorium dodawany jest skrypt migracji zawierający szczegółowe informacje o zmianie. Aby zastosować migracje do bazy danych, te skrypty migracji są wykonywane w kolejności, w jakiej zostały utworzone.

OBSŁUGA BŁĘDÓW: 
Flask pozwala aplikacji na definiowanie niestandardowych stron błędów, które mogą bazować na szablonach, podobnie jak strony zwykłych tras. Dwa najczęściej występujące kody błędów to 404 oraz kod błędu 500. Procedury obsługi błędów zwracają odpowiedź, podobnie jak funkcje widoku, ale muszą również zwrócić liczbowy kod stanu odpowiadający błędowi, który Flask przyjmuje jako drugą wartość zwracaną. Tutaj również przydał się render_template.

ZAPYTANIA DO BAZY DANYCH:
Na powyższym slajdzie prezentuję wykorzystane przeze mnie zapytanie do bazy danych. Dzięki niemu wyświetlam użytkownikowi przeglądającemu bazę osób prze ankietowanych ile osób wypełniło ankietę. Można było by to rozwiązać również wypisując po prostu id jednak uznałam to za bardziej elegancki sposób.
