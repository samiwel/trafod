from flask import Flask, render_template, abort, request, redirect, flash, url_for
from flask_pymongo import PyMongo

from models import Topic

app = Flask(__name__)
app.secret_key = 'some_secret'

app.config['MONGO_HOST'] = 'mongodb'

app.config['MONGO_DBNAME'] = 'trafod'
mongo = PyMongo(app)


@app.route('/')
@app.route("/topics")
def get_topics():
    topics = list(mongo.db.topics.find())
    return render_template("topics.html", topics=topics)


@app.route('/topics/create', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        new_topic = Topic(request.form['title'])
        mongo.db.topics.insert_one(new_topic.__dict__)
        flash('Topic created successfully')
        return redirect('/topics')

    return render_template('topic_create.html')


@app.route("/topic/<topic_id>")
def get_topic(topic_id):
    topic = mongo.db.topics.find_one_or_404({'topic_id': topic_id})
    return render_template('topic_detail.html', topic=topic)


@app.route('/topic/<topic_id>/threads/create', methods=['GET', 'POST'])
def create_thread(topic_id):
    # topic = mongo.db.topics.find_one_or_404({"topic_id": topic_id})
    back_url = url_for('get_topic', topic_id=topic_id)
    if request.method == 'POST':
        flash('Topic created successfully')
        return redirect('/topics')

    return render_template('thread_create.html', back_url=back_url)

# @app.route("/topic/<int:topic_id>/threads")
# def get_topic_threads(topic_id):
#     topic = mongo.db.topics.find_one_or_404({"topicId": topic_id})
#     return dumps(topic.get('threads', []))
#
#
# @app.route("/topic/<int:topic_id>/thread/<int:thread_id>")
# def get_topic_thread(topic_id, thread_id):
#     topic = mongo.db.topics.find_one_or_404({"topicId": topic_id})
#     for thread in topic.get('threads'):
#         if thread.get('threadId') == thread_id:
#             return dumps(thread)
#
#     abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
