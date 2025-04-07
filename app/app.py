from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Liste partielle des icônes disponibles (vous pouvez l'étendre)
MATERIAL_ICONS = [
    'home', 'search', 'menu', 'close', 'settings', 'done', 'favorite',
    'delete', 'add', 'star', 'arrow_back', 'arrow_forward', 'chevron_right',
    'expand_more', 'cancel', 'check_circle', 'warning', 'info', 'print',
    'share', 'email', 'phone', 'person', 'shopping_cart', 'credit_card',
    'work', 'school', 'public', 'cake', 'flight', 'hotel', 'restaurant',
    'music_note', 'movie', 'book', 'computer', 'smartphone', 'headset'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    icon_name = None
    if request.method == 'POST':
        search_term = request.form.get('text', '').strip().lower()
        if search_term:
            # Trouver la première icône qui contient le terme recherché
            for icon in MATERIAL_ICONS:
                if search_term in icon:
                    icon_name = icon
                    break
    
    return render_template('index.html', icon_name=icon_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/suggest')
def suggest():
    term = request.args.get('term', '')
    suggestions = [icon for icon in MATERIAL_ICONS if term in icon]
    return jsonify(suggestions[:5])