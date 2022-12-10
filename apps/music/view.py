from flask import  Blueprint,request
import  os
import time

music_bp=Blueprint('music',__name__,url_prefix='/user')
@music_bp.route('/music',methods=["POST","GET"])
def music():
    if request.method=='POST':
        upload_file=request.files['file']
        path = 'static/video/'
        filename=upload_file.filename
        name=os.path.splitext(filename)[0]
        path_filename=path+filename
        if filename!='':
            upload_file.save(path_filename)
            music_url='static/music/'+name+'.m4a'
            os.system('ffmpeg -i {} -vn -y -acodec copy {} -loglevel quiet'.format(path_filename,music_url))
            time.sleep(2)
            return  {
                'video_url':'http://127.0.0.1:5000/'+path_filename,
                'music_url':'http://127.0.0.1:5000/'+music_url,
            }







