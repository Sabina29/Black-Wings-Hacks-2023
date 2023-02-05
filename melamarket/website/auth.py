from flask import Blueprint, render_template

auth= Blueprint('auth', __name__)

@auth.route('/explore')
def explore():
    return render_template('explore.html', dress= "Green Dress", page= "@alexa_shops", text= "Buy", text1="Connect", nice= "I love it!")

@auth.route('/your-posts')
def your_posts():
    return render_template('your-posts.html', text="pretty in pink<3", text1="loved it so much, i had to double it XD")

