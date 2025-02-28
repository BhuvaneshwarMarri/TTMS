from flask import *
from forms import CustomForm

app = Flask(__name__)
app.secret_key = 'secret form'

@app.route('/',methods=["GET","POST"])
def index():
    formx = CustomForm()
    if formx.validate_on_submit():
        print(f" The data is {request.form}")
        print(formx.value.data)
    else:
        print("Data is invalid")
        print(f"{formx.errors}")
        print(f"{formx.value.errors}")
    return render_template('index.jinja.html',form = formx )

# In inputrequired we can give spaces , in datarequired we cannot give spaces 
# Filters will add from beginning of list to end of list.