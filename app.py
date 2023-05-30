from flask import Flask,render_template,request

FAI=Flask(__name__)


@FAI.route('/data',methods=['GET','POST'])
def data():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data['na']
    return render_template('data.html')


if __name__=='__main__':
    FAI.run(debug=True)