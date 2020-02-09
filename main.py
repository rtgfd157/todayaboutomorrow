from flask import Flask
from flask import render_template,request,redirect,session,Session
from datetime import time
from random import randint
import work_with_db_record
import work_with_db_category
import datetime
import category_controller
app = Flask(__name__)


#Session(app)


# @app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
    #    return name
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber = randint(0, len(quotes) - 1)
    print("num ",randomNumber)
    quote = quotes[randomNumber]



    return render_template(
        'test.html', **locals())



# @app.route("/hello/<string:name>")
@app.route("/" ,methods=['GET', 'POST'])
def root():


    if request.method == 'POST':
        category_name = request.form['category_name']
        ans=work_with_db_category.select_all_categories()
        category_id=work_with_db_category.return_id_by_category(category_name)
        ans_category=work_with_db_record.select_all_category_recorde_by_category_id(category_id)

        return render_template(
            'show_category_data.html', **locals())

        print("cstegory",category_name)
        pass


    ans=work_with_db_category.select_all_categories()

    #date=datetime.datetime()
    # i = datetime.datetime.now()
    # checktime = str(i)
    # checktime = checktime[0:19]
    return render_template(
        'main.html', **locals())



#add machine to db
@app.route('/delete_category', methods=['GET', 'POST'])
def delete_category():



    if request.method == 'POST':

        category_name = request.form['category_name']

        #print(dut_fpga)

        #last_update= datetime.datetime.now()

        id_category =work_with_db_category.return_id_by_category(category_name)
        work_with_db_record.delete_all_records_by_id_category(id_category)

        ans=work_with_db_record.select_all_category_recorde_by_category_id(id_category)
        #print("ans ",ans)
        work_with_db_category.delete_task(id_category)


        return redirect('/management246')


        print(category_name,category_description,pic_link)



    else:

        ans=work_with_db_category.select_all_categories()
        return render_template(
            'delete_category.html',**locals())



#add machine to db
@app.route('/add_category', methods=['GET', 'POST'])
def add_category():



    if request.method == 'POST':

        category_name = request.form['category_name']

        category_description = request.form['category_description']
        #print(dut_card)

        pic_link = request.form['pic_link']
        #print(dut_card_nvm)


        #print(dut_fpga)

        print(category_name,category_description,pic_link)


        #last_update= datetime.datetime.now()

        id =work_with_db_category.return_id_by_category(category_name)

        if id is  None :
                category_data=[category_name,category_description,pic_link]
                work_with_db_category.add_category(category_data)
                return redirect('/management246/')

        elif id==-1:
            category_data = [category_name, category_description, pic_link]
            work_with_db_category.add_category(category_data)
            return redirect('/management246/')


        else:
            # print("there already val ",id)
            return redirect('/management246/')

        print(category_name,category_description,pic_link)



    else:


        return render_template(
            'insert_category.html',**locals())



#add machine to db
@app.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    print("dfdsfsdf----------4444444444")

    if request.method == 'POST':

        #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        id_category=category_name = request.form['id_category']
        category_name = request.form['category_name']
        category_description = request.form['category_description']
        pic_link = request.form['pic_link']
        #print(category_name,category_description,pic_link)

        #id=work_with_db_category.return_id_by_category(category_name)

        category_data = (category_name, category_description, pic_link,id_category)
        work_with_db_category.update_record(category_data)

        return redirect ('/management246/')


        #print(category_name,category_description,pic_link)

    else:

        #print("from get-------k")
        ans = session['message']
        #print(ans)

        return render_template(
            'edit_category.html',**locals())



#add machine to db
@app.route('/choose_edit_category', methods=['GET', 'POST'])
def choose_edit_category():

    #print("from edit category")

    if request.method == 'POST':

        print("esdfsdfsd")
        category_name = request.form['category_name']
        #ans=work_with_db_category.select_all_categories()
        id=work_with_db_category.return_id_by_category(category_name)

        ans=work_with_db_category.return_category_data_by_id(id)
        #print("id---",id)
        session['message'] = ans

        return redirect ('/edit_category')



    else:

        #print("from choose get")

        ans= work_with_db_category.select_all_categories()
        return render_template(
            'choose_edit_category.html',**locals())




#add machine to db
@app.route('/insert_record_to_category', methods=['GET', 'POST'])
def insert_record_to_category():
    #print("dfdsfsdf----------insert to record")

    if request.method == 'POST':

        #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        id_category=category_name = request.form['id_category']
        #category_name = request.form['category_name']
        name_of_record=request.form['name_of_record']
        record_destenation_date = request.form['record_destenation_date']
        archive = request.form['archive']

        show_counter = request.form['show_counter']
        record_description = request.form['record_description']
        link1 = request.form['link1']
        link2 = request.form['link2']
        link3 = request.form['link3']



        #print(id_category,record_description,record_destenation_date,link1,link2,link3)

        #id=work_with_db_category.return_id_by_category(category_name)

        category_data = (id_category,name_of_record,record_destenation_date,archive,show_counter,record_description,link1,link2,link3)
        work_with_db_record.add_record_to_category(category_data)

        return redirect ('/management246')


        #print(category_name,category_description,pic_link)

    else:

        #print("from get-------k")
        ans = session['message']
        print(ans)

        return render_template(
            'insert_record_to_category.html',**locals())


#add machine to db
@app.route('/choose_category_for_adding_record', methods=['GET', 'POST'])
def choose_category_for_adding_record():

    #print("from edit category")

    if request.method == 'POST':

        #print("esdfsdfsd")
        category_name = request.form['category_name']
        #ans=work_with_db_category.select_all_categories()
        id=work_with_db_category.return_id_by_category(category_name)

        ans=work_with_db_category.return_category_data_by_id(id)
        #print("id---",id)
        session['message'] = ans

        return redirect ('/insert_record_to_category')


        print(category_name,category_description,pic_link)



    else:

        #print("from choose get")

        ans= work_with_db_category.select_all_categories()
        return render_template(
            'choose_category_for_adding_record.html',**locals())



#add machine to db
@app.route('/choose_category_for_editing_record', methods=['GET', 'POST'])
def choose_category_for_editing_record():

    #print("from edit category")

    if request.method == 'POST':

        #print("llllllll")
        category_name = request.form['category_name']
        #ans=work_with_db_category.select_all_categories()
        id=work_with_db_category.return_id_by_category(category_name)

        ans=work_with_db_category.return_category_data_by_id(id)
        #print("id---",id)
        session['message'] = ans

        return redirect ('/choose_records_for_edit')



    else:

        #print("from choose get")

        ans= work_with_db_category.select_all_categories()
        return render_template(
            'choose_category_for_editing_record.html',**locals())


@app.route('/record_edit_form', methods=['GET', 'POST'])
def record_edit_form():

    if request.method == 'POST':
        name_of_record=request.form['name_of_record']
        record_destenation_date = request.form['record_destenation_date']
        archive = request.form['archive']


        id_category=category_name = request.form['category_id']
        id_record = request.form['id_record']

        show_counter = request.form['show_counter']
        record_description = request.form['record_description']
        link1 = request.form['link1']
        link2 = request.form['link2']
        link3 = request.form['link3']

        print(name_of_record,record_destenation_date,archive,show_counter,record_description,link1,link2,link3, id_record, id_category)

        #id=work_with_db_category.return_id_by_category(category_name)

        category_data = (name_of_record,record_destenation_date,archive,show_counter,record_description,link1,link2,link3, id_record, id_category)
        print("category data",category_data)
        work_with_db_record.update_record(category_data)
        #work_with_db_record.add_record_to_category(category_data)

        return redirect ('/management246')

    else:

        ans = session['message']

        return render_template(
            'record_edit_form.html', **locals())


@app.route('/choose_records_for_edit', methods=['GET', 'POST'])
def choose_records_for_edit():

    if request.method == 'POST':


        record_id = request.form['record_id']
        category_id = request.form['category_id']

        #print("REcord name",record_name , "catregory id",category_id)
        ans=work_with_db_record.select_record_by_id(record_id)
        #print("ans after ..",ans)
        print("----")
        print("record name",record_id)
        print("category id",category_id)
        print("---------")
        #ww=work_with_db_record.looping_record_by_record_name(record_name)

        #print("ww",ww)


        session['message']=ans


        return redirect ('/record_edit_form')
        #flask.redirect(flask.url_for('operation'), code=307)



    else:

        ans = session['message']
        ans=work_with_db_record.select_all_category_recorde_by_category_id(ans[0])

        return render_template(
            'choose_records_for_edit.html',**locals())



#add machine to db
@app.route('/delete_record_from_category', methods=['GET', 'POST'])
def delete_record_from_category():

    if request.method == 'POST':

        record_name = request.form['record_name']
        category_id = request.form['category_id']

        print(record_name,category_id)


        work_with_db_record.delete_record_by_name_of_record_and_id_category(record_name,category_id)

        #id=work_with_db_category.return_id_by_category(category_name)

        #category_data = (id_category,name_of_record,record_destenation_date,archive,show_counter,record_description,link1,link2,link3)
        #work_with_db_record.add_record_to_category(category_data)

        return redirect ('/management246')


        #print(category_name,category_description,pic_link)

    else:

        ans = session['message']

        return render_template(
            'delete_record_from_category.html',**locals())


#add machine to db
@app.route('/choose_category_for_deleting_record', methods=['GET', 'POST'])
def choose_category_for_deleting_record():


    if request.method == 'POST':

        print("esdfsdfsd")
        category_name = request.form['category_name']
        #ans=work_with_db_category.select_all_categories()
        id=work_with_db_category.return_id_by_category(category_name)

        ans=work_with_db_category.return_category_data_by_id(id)
        #print("id---",id)
        print("anssssss:",ans)
        ans=work_with_db_record.select_all_category_recorde_by_category_id(ans[0])

        session['message'] = ans

        return redirect ('/delete_record_from_category')


        print(category_name,category_description,pic_link)

    else:

        ans= work_with_db_category.select_all_categories()
        return render_template(
            'choose_category_for_deleting_record.html',**locals())


@app.route('/management246/', methods=['GET', 'POST'])
def management246():

    print("from manage")

    ans=work_with_db_category.select_all_categories()

    return render_template(
            'management246.html',**locals())




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True, threaded = True,host='0.0.0.0', port=8000)