# Generated by Django 4.0.4 on 2022-06-24 10:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('estate_type', models.CharField(choices=[('H', 'Дом'), ('F', 'Картира')], max_length=1, verbose_name='Вид собственности')),
                ('slug', models.SlugField(max_length=256)),
                ('description', models.TextField(verbose_name='Описание')),
                ('location', models.CharField(choices=[('B', 'Бишкек'), ('AD', 'Ак-Джол'), ('AB', 'Ала-Бука'), ('AT', 'Ала-Тоо'), ('AN', 'Аламедин'), ('AU', 'Алмалуу'), ('AO', 'Ананьево'), ('AR', 'Араван'), ('ARSH', 'Арашан'), ('AI', 'Арчалы'), ('ABI', 'Ат-Башы'), ('BT', 'Бает'), ('BV', 'Баетов'), ('BKN', 'Базар-Коргон'), ('BK', 'Байтик'), ('BAI', 'Бакай-Ата'), ('BDU', 'Бактуу-Долоноту'), ('BI', 'Балыкчы'), ('BN', 'Баткен'), ('BE', 'Беловодское'), ('BKI', 'Беш-Кюнгей'), ('BIK', 'Бирдик'), ('BO', 'Боконбаево'), ('BOI', 'Бостери'), ('BA', 'Буденовка'), ('BSU', 'Булан-Соготту'), ('VAA', 'Военно-Антоновка'), ('GA', 'Гавриловка'), ('GMA', 'Горная Маевка'), ('GEA', 'Григорьевка'), ('GLA', 'Гульча'), ('DKN', 'Дароот-Коргон'), ('D', 'Дачное(ГЕС-5)'), ('DZH', 'Джал мкр.'), ('DZHA', 'Джалал-Абад'), ('DZHD', 'Джаны-Джер'), ('DA', 'Дмитриевка'), ('ZHV', 'Жаркынбаев'), ('ZE', 'Заречное'), ('Z', 'Заря'), ('I', 'Ивановка'), ('IA', 'Исфана'), ('KAI', 'Кадамжай'), ('KSI', 'Каджи-Сай'), ('KN', 'Казарман'), ('KI', 'Каинды'), ('KA', 'Каирма'), ('K', 'Кант'), ('KKI', 'Каныш-Кия'), ('KB', 'Кара-Балта'), ('KK', 'Кара-Кульджа'), ('KO', 'Кара-Ой'), ('KS', 'Кара-Суу'), ('KKU', 'Кара-Куль'), ('KL', 'Каракол'), ('KT', 'Кашат'), ('KSU', 'Кашка-Суу'), ('KIN', 'Кемин'), ('KEN', 'Кербен'), ('KOE', 'Кировское'), ('KR', 'Кожояр'), ('KTSH', 'Кой-Таш'), ('KDZH', 'Кой-Джар'), ('KOI', 'Кок-Ой'), ('KKA', 'Константиновка'), ('KU', 'Корумду'), ('KOR', 'Кочкор'), ('KORA', 'Кочкор-Ата'), ('KRA', 'Красная Речка'), ('KTU', 'Кунтуу'), ('KAR', 'Кызыл-Адыр'), ('KKIA', 'Кызыл-Кия'), ('KLSU', 'Кызыл-Суу'), ('KLTU', 'Кызыл-Туу'), ('LA', 'Лебединовка'), ('LE', 'Ленинское'), ('LGE', 'Луговое'), ('MA', 'Маевка'), ('MSU', 'Майлуу-Суу'), ('ME', 'Маловодное'), ('MS', 'Манас'), ('MI', 'Массы'), ('MN', 'Милянфан'), ('MKA', 'Михайловка'), ('M', 'Мыкан'), ('N', 'Нарын'), ('NN', 'Нижний Норус'), ('NA', 'Новопавловка'), ('NKA', 'Новопокровка'), ('NT', 'Ноокат'), ('NS', 'Норус'), ('OA', 'Орловка'), ('OS', 'Орто-Сай'), ('O', 'Ош'), ('PA', 'Покровка'), ('PE', 'Пригородное'), ('PN', 'Пульгон'), ('RE', 'Раздольное'), ('SE', 'Садовое (ГЭС-3)'), ('SOE', 'Селекционное'), ('SA', 'Семеновка'), ('S', 'Сокулук'), ('SK', 'Сретенка'), ('STOE', 'Студенческое'), ('SAK', 'Сузак'), ('STA', 'Сулюкта'), ('T', 'Талас'), ('TI', 'Тамчы'), ('TMK', 'Таш-Мойнок'), ('TR', 'Темир'), ('TA', 'Теплоключенка'), ('TB', 'Тогул Булак'), ('TK', 'Токмок'), ('TL', 'Токтогул'), ('TIK', 'Тынчтык'), ('TUP', 'Тюп'), ('U', 'Узген'), ('CH', 'Чаек'), ('CHR', 'Чалдавар'), ('CHK', 'Чат Кёль'), ('CHT', 'Чок-Тал'), ('CHA', 'Чолпон-Ата'), ('CHSI', 'Чон Сары-Ой'), ('CHAK', 'Чон-Арык'), ('CHD', 'Чон-Далы'), ('CHT', 'Чон-Таш'), ('CHCHK', 'Чункурчак'), ('SHO', 'Шевченко'), ('SHV', 'Шопоков'), ('U', 'Юрьевка'), ('PD', 'пос. Дачный')], max_length=5, verbose_name='Местонахождение')),
                ('posted_on', models.DateField(auto_now=True, verbose_name='Опубликовано')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('area', models.IntegerField(verbose_name='Площадь')),
                ('photo', models.ImageField(upload_to='estate_photos', verbose_name='Изображение')),
                ('video', models.FileField(null=True, upload_to='estate_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Видео')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Имущество',
                'verbose_name_plural': 'Имущества',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('kind', models.CharField(choices=[('HF', 'Пол с подогревом'), ('PO', 'Двор'), ('GN', 'Сад'), ('SP', 'Бассейн')], max_length=3)),
                ('bathrooms', models.IntegerField(verbose_name='Ванные комнаты')),
                ('bedrooms', models.IntegerField(verbose_name='Спальни')),
                ('garages', models.IntegerField(null=True, verbose_name='Гаражи')),
                ('floors', models.IntegerField(verbose_name='Количество этажей')),
                ('floor_on', models.IntegerField(verbose_name='Этаж')),
                ('estate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='estates.estate')),
            ],
            options={
                'verbose_name': 'Особенности',
                'verbose_name_plural': 'Особенности',
            },
        ),
    ]
