from flask import  Blueprint,request
import easyocr

ocr_bp=Blueprint('ocr',__name__,url_prefix='/user')

@ocr_bp.route('/ocr',methods=["POST","GET"])
def ocr():
    if request.method=='POST':
        upload_file=request.files['file']
        filename=upload_file.filename
        print(filename)
        if filename!='':
            upload_file.save('static/images/ocr/'+filename)
        reader=easyocr.Reader(['ch_sim','en'])
        results=reader.readtext('static/images/ocr/{}'.format(filename))
        text=' '
        for result in results:
            text+=result[1]+''
        print(text)
        return {'text':text,"url":"http://127.0.0.1:5000/static/images/ocr/"+filename}