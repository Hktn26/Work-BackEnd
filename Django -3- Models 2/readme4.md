# python manage.py shell -> Test etme yerimiz Giris <- exit()

    from appname.models import Customer
    s1 = Customer(first_name = 'Emir', last_name = 'Coskuner', age = 22) ->instance olusturduk
    s1.save() -> veritabanina kaydettik
    s1 -> Emir Coskuner 22
    s1.age = 23
    s1.save() -> veritabaninda update yaptik
    s1 -> Emir Coskuner 23

    s2 = Customer.objects.create(first_name = 'Mehmet', last_name = 'Coskuner', age = 55) -> save gerekmez
    s2 -> Mehmet Coskuner 55

    all = Customer.objects.all() -> Emir Coskuner 23, Mehmet Coskuner 55, ... -> Butun objeleri getir.

    get ==> Tek bir kayit icin ya da id ler icin (benzersiz kayitlar icin) kullanilir.
    get = Customer.objects.get(age = 23) -> Emir Coskuner 23

    filter ==> Coklu kayitlar icin kullanilir.
    filter = Customer.objects.filter(last_name='Coskuner') -> Emir Coskuner 23, Mehmet Coskuner 55

    exclude ==> Olmayanlari listeler
    exclude = Customer.objects.exculude(age = 23) -> yasi 23 olmayanlari getirir. Mehmet Coskuner 55

    strswth = Customer.object.fliter(last_name__startswith = 'C') -> E.Coskuner 23, M.Coskuner 55
    endswth = Customer.object.fliter(last_name__endswith = 'r') -> E.Coskuner 23, M.Coskuner 55

    s1.delete() -> instance silindi


# RelationsApp

    on_delete properties:
        # CASCADE -> if primary deleted, delete foreing too
        # PROTECT -> if foreign is exist, can not delete primary.
        # SET_NULL -> if primary deleted, set foreing to NULL. (null=True)
        # SET_DEFAULT -> if primary deleted, set default value of foreing field.
        # DO_NOTHING -> if primary deleted, do nothing

    on_delete properties:
        CASCADE -> Eğer birincil öğe silinirse, bağlı öğeyi de sil.
        PROTECT -> Eğer bağlı öğe varsa, birincil öğeyi silemezsin.
        SET_NULL -> Eğer birincil öğe silinirse, bağlı öğeyi NULL olarak ayarla (null=True).
        SET_DEFAULT -> Eğer birincil öğe silinirse, bağlı alanın varsayılan değerini ayarla.
        DO_NOTHING -> Eğer birincil öğe silinirse, hiçbir şey yapma.