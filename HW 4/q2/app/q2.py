import re
from flask import Flask, render_template, flash, request, redirect, url_for
from forms import SubmissionForm
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="test",
))


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    form = SubmissionForm()
    print('hello')
    if request.method == 'POST':
        flash('Text Submitted!')
        if form.radio1.data == 'wordcount':
            textform = request.form['text']
            wordCount = textform.replace('\r\n', ' ')
            wordCount = wordCount.strip()
            delims = request.form['delimtext']
            if delims is None or delims == '':
                words = wordCount.split(' ')
                return "Number of words: " + str(len(words))
            else:
                wordlist = re.split('['+ delims + ']', wordCount)
                return "Number of words: " + str(len(wordlist))
            # delimtosplit = " " + delims
            
        elif form.radio1.data == 'charactercount':
            textform = request.form['text']
            charCount = textform.replace('\r\n', '')
            return "Number of chars: " + str(len(charCount))
        elif form.radio1.data == '5mostfrequent':
            textform = request.form['text']
            wordCount = textform.replace('\r\n', ' ')
            wordCount = wordCount.strip()
            delims = request.form['delimtext']
            delimtosplit = " " + delims
            words = wordCount.split(delimtosplit)
            dict2 = {}
            for word in words:
                if word in dict2:
                    dict2[word] += 1
                else:
                    dict2[word] = 1
            count = 0
            strtoprint = ""
            for (key) in (sorted(dict2, key=dict2.__getitem__, reverse=True)):
                strtoprint += key
                strtoprint += " "
                count += 1
                if count == 5:
                    break
            
            return "5 Most frequent words: " + strtoprint
        return redirect(url_for('result', optionname=form.radio1.data))
        
    return render_template('submit.html', form=form)

@app.route('/result/<optionname>', methods=['GET', 'POST'])
def result(optionname):
    if request.method == 'POST':
        if optionname == 'wordcount':
            textform = request.form['text']
            wordCount = textform.replace('\r\n', ' ')
            wordCount = wordCount.strip()
            delims = request.form['delimtext']
            if delims is None or delims == '':
                words = wordCount.split(' ')
                return "Number of words: " + str(len(words))
            else:
                wordlist = re.split('['+ delims + ']', wordCount)
                return "Number of words: " + str(len(wordlist))
            # delimtosplit = " " + delims
            
        elif optionname == 'charactercount':
            textform = request.form['text']
            charCount = textform.replace('\r\n', '')
            return "Number of chars: " + str(len(charCount))
        elif optionname == '5mostfrequent':
            textform = request.form['text']
            wordCount = textform.replace('\r\n', ' ')
            wordCount = wordCount.strip()
            delims = request.form['delimtext']
            delimtosplit = " " + delims
            words = wordCount.split(delimtosplit)
            dict2 = {}
            for word in words:
                if word in dict2:
                    dict2[word] += 1
                else:
                    dict2[word] = 1
            count = 0
            strtoprint = ""
            for (key) in (sorted(dict2, key=dict2.__getitem__, reverse=True)):
                strtoprint += key
                strtoprint += " "
                count += 1
                if count == 5:
                    break
            
            return "5 Most frequent words: " + strtoprint
        
# @app.route('/result')

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()