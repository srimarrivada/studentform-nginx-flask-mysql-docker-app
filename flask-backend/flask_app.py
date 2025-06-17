from flask import Flask, render_template, request, redirect
from db_operations import DBManager

app=Flask(__name__)

@app.route("/studentform")
def loadForm():
    return render_template('student_form.html')
    
@app.route("/insertdata", methods=['GET','POST'])
def insertData():
    if request.method == 'POST':
        id=request.form.get('roll_number')
        name=request.form.get('name')
        email=request.form.get('email')
        course=request.form.get('course')
        marks=request.form.get('marks')
        
        conn=DBManager()
        conn.insert_data(id, name, email, course, marks)
        return redirect("/querydata")
    else:
        return "There is some issue while submitting data. Please check and try again!!"

@app.route("/querydata")
def queryData():
    conn=DBManager()
    query_result=conn.query_data()

    # Prepare HTML code
    header = ['ID', 'Name', 'Email', 'Course', 'Marks', 'Submitted Date']
    table_header = '<tr>' + ''.join(f'<th style="border: 1px solid #ccc; background: #ddd;">{item}</th>' for item in header) + '</tr>'
    table_rows=''
    for row in query_result:
        table_rows = table_rows + '<tr>' + ''.join(f'<td style="border: 1px solid #ccc;">{item}</td>' for item in row) + '</tr>'
    
    response_html = f'''
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <h3 style="color: green;">Data has been submitted successfully!!</h3>
            <h4>Click <a href="./studentform" style="color: blue">here</a> to submit a new record</h4>
            <h4>For your reference, 5 most recently submitted records are listed below:</h4>
            <table style="margin: auto; max-width: 500px;">
                {table_header}
                {table_rows}
            </table>
        </body>
    '''
    return response_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8070)
