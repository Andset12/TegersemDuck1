from flask import Flask, render_template
import datetime

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    current_year = datetime.datetime.now().strftime("%Y")
    artickals=[
        {'title': 'Чёртова дюжина ошибок начинающего программиста',
    'text': 'У каждого из нас имеется собственный компьютер на углеродной основе — головной мозг. Мощный, продуктивный и чрезвычайно сложный. Но, увы, подверженный сбоям и ошибкам. Баги заметили ещё в античности, а древние римляне запротоколировали их в краткой и ёмкой формуле: «Человеку свойственно ошибаться».',
    'img': 'blog-photo-1.png'},
    {'title': 'Как учить Python: девять кратких практических советов',
    'text': 'Python уже не один год уверенно занимает место среди самых популярных языков программирования. На нём можно писать любые программы, но сегодня основной сферой для него стал искусственный интеллект и всё, что с ним связано — data science, машинное обучение, анализ данных, нейронные сети. Кроме того, Python популярен в веб-разработке. Среди новейших направлений Python является лидером в квантовых вычислениях и квантовом машинном обучении.',
    'img':'blog-photo-2.png'},
    {'title': f'Тренды среди языков программирования в {current_year} году',
    'text': 'Все, кто хочет связать свою жизнь с программированием, задумываются о том, на какой язык замахнуться. Здесь важно не только понимать, как обстоят дела сегодня, но и следить за трендами — ведь к тому времени, как обучение закончится, что-нибудь в картине мира наверняка поменяется.',
    'img': 'blog-photo-3.png'}]
    return render_template('blog.html',artickals = artickals)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')






app.run()
