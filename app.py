from flask import Flask, render_template, request

app = Flask(__name__)

activities = {
    'спорт': [
        'игра в футбол', 'велосипед', 'плавание', 'бег', 'йога',
        'скейтбординг', 'теннис', 'гимнастика', 'прыжки на батуте',
        'фитнес', 'пешеходные прогулки', 'картинг', 'скалолазание'
    ],
    'творчество': [
        'рисование', 'лепка', 'музыка', 'фотография', 'танцы',
        'выпечка', 'создание украшений', 'вязаные изделия',
        'каллиграфия', 'видео монтаж', 'декупаж', 'создание комиксов'
    ],
    'природа': [
        'поход', 'пикник', 'садоводство', 'наблюдение за птицами',
        'поездка на природу', 'плавание на байдарках', 'рыбалка',
        'кемпинг', 'экскурсия по заповедникам', 'поездка на лошадях'
    ],
    'игры': [
        'настольные игры', 'видеоигры', 'карты', 'пазлы',
        'квесты', 'шахматы', 'игры на свежем воздухе',
        'игры с мячом', 'развивающие игры', 'игры с карточками'
    ],
    'наука': [
        'эксперименты', 'посещение музеев', 'научные проекты',
        'изучение астрономии', 'проведение химических опытов',
        'изучение экологии', 'посещение планетария',
        'изучение биологии', 'изучение физики'
    ],
    'культура': [
        'поход в театр', 'кино', 'выставка', 'чтение книг',
        'поездка в исторические места', 'посещение концертов',
        'участие в культурных мероприятиях', 'изучение языков',
        'посещение художественных галерей'
    ],
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/interests', methods=['POST'])
def interests():
    family_count = int(request.form['family_count'])
    return render_template('interests.html', family_count=family_count)


@app.route('/result', methods=['POST'])
def result():
    interests_lists = request.form.getlist('interests[]')

    all_interests = set()
    for interests in interests_lists:
        all_interests.update(interests.split(','))

    selected_activities = []
    for interest in all_interests:
        if interest in activities:
            selected_activities.extend(activities[interest])

    selected_activities = sorted(set(selected_activities))

    return render_template('result.html', activities=selected_activities)


if __name__ == '__main__':
    app.run(debug=True)